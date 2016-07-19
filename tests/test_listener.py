import unittest
from lib.listener import PymonListener

class ListenerTestCase(unittest.TestCase):
    def setUp(self):
        self.listener = PymonListener("python", "tests/hello.py")

    def tearDown(self):
        self.listener = None

    def testStart(self):
        self.assertIsNone(self.listener.proc)
        self.listener.start(True)
        self.assertIsNotNone(self.listener.proc)
        output = self.listener.proc.communicate()[0]
        self.assertEqual(output, "Hello World!\n")
    
    def testStop(self):
        self.assertIsNone(self.listener.proc)
        self.listener.stop()
        self.assertIsNone(self.listener.proc)
        self.listener.start(True)
        self.assertIsNotNone(self.listener.proc)
        output = self.listener.proc.communicate()[0]
        self.assertEqual(output, "Hello World!\n")
        self.assertIsNotNone(self.listener.proc)
        self.listener.stop()
        self.assertIsNone(self.listener.proc)
        
    def testRestart(self):
        self.assertIsNone(self.listener.proc)
        self.listener.restart(True)
        self.assertIsNotNone(self.listener.proc)
        output = self.listener.proc.communicate()[0]
        self.assertEqual(output, "Hello World!\n")
        self.listener.restart(True)
        self.assertIsNotNone(self.listener.proc)
        output = self.listener.proc.communicate()[0]
        self.assertEqual(output, "Hello World!\n")
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ListenerTestCase("testStart"))
    suite.addTest(ListenerTestCase("testStop"))
    suite.addTest(ListenerTestCase("testRestart"))
    return suite
