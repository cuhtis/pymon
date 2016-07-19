import unittest
import tests.test_listener
import tests.test_transport

if __name__ == '__main__':
    listenerSuite = tests.test_listener.suite()
    transportSuite = tests.test_transport.suite()

    allSuites = unittest.TestSuite((
        listenerSuite,
        transportSuite
        ))

    runner = unittest.TextTestRunner()
    runner.run(allSuites)
