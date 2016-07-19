import unittest
import os
import subprocess
from lib.listener import PymonListener

class MonitorTestCase(unittest.TestCase):
    def setUp(self):
        global called
        called = False
        self.old_popen = subprocess.Popen
        subprocess.Popen = self.mocked_call
        self.listener = PymonListener("python", "tests/hello.py")
        self.assertIsNone(self.listener.proc)
        self.listener.start()

    def tearDown(self):
        self.listener = None
        subprocess.Popen = self.old_popen

    def mocked_call(*args, **kwargs):
        global called
        called = True
    
    def check_call(self):
        global called
        self.assertTrue(called)
        called = False

    def testRestartTouchFile(self):
        with open('tests/test_file.txt', 'a'):
            os.utime('tests/test_file.txt', None)
            self.check_call()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MonitorTestCase("testRestartTouchFile"))
    return suite
