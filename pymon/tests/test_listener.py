import unittest
import subprocess
from lib.listener import PymonListener

class ListenerTestCase(unittest.TestCase):
    def setUp(self):
        global called, called_popen
        called = False
        called_popen = False
        self.old_popen = subprocess.Popen
        subprocess.Popen = self.mocked_popen
        self.listener = PymonListener("python", "tests/hello.py")

    def tearDown(self):
        self.listener = None
        subprocess.Popen = self.old_popen

    def mocked_popen(*args, **kwargs):
        global called_popen
        called_popen = True
    
    def check_popen(self):
        global called_popen
        self.assertTrue(called_popen)
        called_popen = False
    
    def mocked_call(*args, **kwargs):
        global called
        called = True
    
    def check_call(self):
        global called
        self.assertTrue(called)
        called = False
    
    def testStart(self):
        # Call start when program stopped
        self.assertIsNone(self.listener.proc)
        self.listener.start()
        self.check_popen()

        # Call start when program started
        self.listener.start()
    
    def testStop(self):
        # Calling stop when program stopped
        self.assertIsNone(self.listener.proc)
        self.listener.stop()
        self.assertIsNone(self.listener.proc)

        # Starting the program
        self.listener.start()
        self.check_popen()

        # Calling stop when program running
        self.listener.stop()
        self.assertIsNone(self.listener.proc)
        
    def testRestart(self):
        # Calling restart when program stopped
        self.assertIsNone(self.listener.proc)
        self.listener.restart()
        self.check_popen()
        
        # Calling restart when program running
        self.listener.restart()
        self.check_popen()

    def testPing(self):
        pass

    def testHandleStart(self):
        self.old_start = PymonListener.start
        PymonListener.start = self.mocked_call
        self.listener.handle_msg("start")
        self.check_call()
        PymonListener.start = self.old_start

    def testHandleStop(self):
        self.old_stop = PymonListener.stop
        PymonListener.stop = self.mocked_call
        self.listener.handle_msg("stop")
        self.check_call()
        PymonListener.stop = self.old_stop

    def testHandleRestart(self):
        self.old_restart = PymonListener.restart
        PymonListener.restart = self.mocked_call
        self.listener.handle_msg("restart")
        self.check_call()
        PymonListener.restart = self.old_restart

    def testHandlePing(self):
        self.old_ping = PymonListener.ping
        PymonListener.ping = self.mocked_call
        self.listener.handle_msg("ping")
        self.check_call()
        PymonListener.ping = self.old_ping

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ListenerTestCase("testStart"))
    suite.addTest(ListenerTestCase("testStop"))
    suite.addTest(ListenerTestCase("testRestart"))
    suite.addTest(ListenerTestCase("testPing"))
    suite.addTest(ListenerTestCase("testHandleStart"))
    suite.addTest(ListenerTestCase("testHandleStop"))
    suite.addTest(ListenerTestCase("testHandleRestart"))
    suite.addTest(ListenerTestCase("testHandlePing"))
    return suite
