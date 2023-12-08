import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class TestElefant(unittest.TestCase):
    LINK = "https://www.elefant.ro/"
    driver = webdriver.Chrome()


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(2)
        accept_cookies = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        accept_cookies.click()

    def tearDown(self) -> None:
        print("Releasing the driver")
        self.driver.quit()


    def test_url(self):
        actual_url = self.driver.current_url
        self.assertEqual(self.LINK, actual_url, "Unexpected URL")

    def test_search_iphone(self):
        search_bar = self.driver.find_element(By.NAME, "SearchTerm")
        search_bar.send_keys("iphone 14")
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        # Version 1
        nr_products = self.driver.find_elements(By.CSS_SELECTOR, "[class='product-title']")
        quantity = len(nr_products)
        self.assertGreaterEqual(quantity, 10, "Not enough products found")

        # Version 2
        # nr_result = self.driver.find_element(By.CLASS_NAME, "element-count")
        # nr_result = int(nr_result.text.split()[0])
        # assert nr_result >= 10

        self.all_elements = self.driver.find_elements(By.CLASS_NAME, "current-price")
        first_ten_elements = []
        for i in range(10):
            first_ten_elements.append(self.all_elements[i].text)
            print(self.all_elements[i].text)
        print('-' * 40)
        print(len(first_ten_elements))
        print('-'*40)
        cheapest = min(first_ten_elements)
        print(cheapest)

    def test_correct_title(self):
        time.sleep(2)
        title = self.driver.title
        print(title)
        assert "elefant.ro - mallul online" in title

    def test_connect_with_invalid_data(self):
        first_connect_button = self.driver.find_element(By.XPATH, "//*[@id=\"HeaderRow\"]/div[4]/div/ul/li[1]/a[1]/span")
        error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
        first_connect_button.click()
        time.sleep(2)
        second_connect_button = self.driver.find_element(By.CLASS_NAME, "my-account-login")
        second_connect_button.click()
        time.sleep(2)
        all_in_one = self.driver.find_element(By.ID, "ShopLoginForm_Login")
        all_in_one.send_keys("user@user", Keys.TAB, "password", Keys.ENTER)
        time.sleep(2)

        generated_message = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        print(generated_message)

        assert generated_message == error, f"Expected: '{error}', Actual: '{generated_message}'"
        print("Test passed!")

    def test_connect_without_atSymbol(self):
        first_connect_button = self.driver.find_element(By.XPATH,"//*[@id=\"HeaderRow\"]/div[4]/div/ul/li[1]/a[1]/span")
        first_connect_button.click()
        time.sleep(2)
        second_connect_button = self.driver.find_element(By.CLASS_NAME, "my-account-login")
        second_connect_button.click()
        time.sleep(2)
        invaid_username = self.driver.find_element(By.ID, "ShopLoginForm_Login")
        invaid_username.send_keys("user-invalid")
        submit_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button")

        if submit_button.is_enabled():
            raise ValueError("Test failed! - The Submit-button is enable.")
        else:
            print("Test passed! - The Submit-button is disable.")