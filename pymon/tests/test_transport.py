import unittest
from lib.transport import PymonTransport, transport
from lib.listener import PymonListener

class TransportTestCase(unittest.TestCase):
    def setUp(self):
        self.transport = PymonTransport()

    def tearDown(self):
        self.transport = None

    def testAddListener(self):
        listener = PymonListener("prog", "args")
        self.transport.add_listener(listener)
        self.assertIn(listener, self.transport.listeners)

    def testAddListeners(self):
        listener1 = PymonListener("prog1", "args")
        listener2 = PymonListener("prog2", "args")
        self.transport.add_listeners([listener1, listener2])
        self.assertIn(listener1, self.transport.listeners)
        self.assertIn(listener2, self.transport.listeners)

    def testRemoveListener(self):
        listener = PymonListener("prog", "args")
        self.transport.add_listener(listener)
        self.assertIn(listener, self.transport.listeners)
        self.transport.remove_listener(listener)
        self.assertNotIn(listener, self.transport.listeners)

    def testStaticTransport(self):
        self.assertIsInstance(transport, PymonTransport)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TransportTestCase("testAddListener"))
    suite.addTest(TransportTestCase("testAddListeners"))
    suite.addTest(TransportTestCase("testRemoveListener"))
    suite.addTest(TransportTestCase("testStaticTransport"))
    return suite
