import unittest
from UnitTest import TestElefant
import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        suite = unittest.TestSuite()
        suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestElefant)

        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name="Test_one",
            report_title= "Test_one"
        )
        runner.run(suite)





