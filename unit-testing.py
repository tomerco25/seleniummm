import unittest
from test import test_support

class MyTestCase1(unittest.TestCase): #!!!MUST USE the word:test in all functions

    def nn_jj(self):
        self.vv=3/0

    def setUp(self): #code to execute in preparation for tests
        self.a = 5

    def tearDown(self): #code to execute to clean up after tests
        self.a=99

    def test_feature_one(self): #Test one
        print "will ERROR"
        a=3/0

    def test_feature_two(self): #Test two
        print "Will FAIL"
        tom=33
        self.failIf(tom==33)

    def test3(self): #Test two
        print self.a

class MyTestCase2(unittest.TestCase):
    def test111(self):
        print "will fail unless"
        un=22
        self.failUnless(un==21)

if __name__ == '__main__':
    unittest.main()