import unittest;
from utils import  DBHelper;
import HtmlTestRunner
testRunner=HtmlTestRunner.HTMLTestRunner(output="c:/test/");

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("Preparing Test")

    def tearDown(self) -> None:
        print("Cleaning Up Tests")

    def test1(self):
        self.suite = unittest.TestSuite();
        self.suite.addTest([unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)])
        print("your test code goes here...")
        con = DBHelper.DBHelper().getConnection()
        self.assertIsNotNone(con);
        con.disconnect();
        self.assertFalse(con.is_connected())
        pass

    def test2(self):
        print("your test2 code coes here ")
        pass

if __name__ == '__main__':
    unittest.main(testRunner=testRunner);
