import unittest
import tests.test_transport

if __name__ == '__main__':
    transportSuite = tests.test_transport.suite()
    allSuites = unittest.TestSuite((transportSuite))
    runner = unittest.TextTestRunner()
    runner.run(allSuites)
