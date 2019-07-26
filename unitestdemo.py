import unittest;
import HtmlTestRunner
testRunner=HtmlTestRunner.HTMLTestRunner(output="c:/test/");

class MyTestExample(unittest.TestCase):
    def test(self):
        self.assertEqual(1,1);

    def test2(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main(testRunner)
