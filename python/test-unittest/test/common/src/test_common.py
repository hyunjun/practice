from unittest import TestCase
from unittest import main
from unittest.mock import patch
import os
import sys


sys.path.append(os.path.join(os.path.dirname('.')))


from common.src import common


#   https://docs.python.org/3/library/unittest.html
#   https://docs.python.org/3/library/unittest.mock.html
#   https://github.com/testing-cabal/mock/issues/398
#   https://pypi.org/project/fakeredis/

#   https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
#   https://www.toptal.com/python/an-introduction-to-mocking-in-python
#   https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
#   https://www.phizzle.space/python/2017/03/31/practical-unit-testing-mocks-python-3.html#mocking_methods
#   https://stackoverflow.com/questions/38579535/how-to-supply-a-mock-class-method-for-python-unit-test
#   https://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
#   https://www.relaxdiego.com/2014/04/mocking-objects-in-python.html
#   https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2


class TestAdd(TestCase):

    def test_add_integers(self):
        result = common.add(3, 4)
        self.assertEqual(result, 7)

    @patch('common.src.common.add', return_value=7.2)
    def test_sum(self, add):
        self.assertEqual(add(3.1, 4.1), 7.2)


class TestCalculator(TestCase):

    @patch('common.src.common.Calculator.sum', return_value=7.2)
    def test_sum(self, sum):
        self.assertEqual(sum(3.1, 4.1), 7.2)


class TestMult(TestCase):

    def test_mult_integers(self):
        result = common.mult(3, 4)
        self.assertEqual(result, 12)


import fakeredis


#def mock_conn(self):
#    self.conn = fakeredis.FakeStrictRedis()


class TestRedis(TestCase):

    #def setUp(self):
    #    self.testRedis = common.TestRedis('127.0.0.1', 6379)

    #def testInfo(self):
    #    result = self.testRedis.info()
    #    self.assertIsNotNone(result)

    #   replace TestRedis#connect
    def mock_conn(self):
        self.conn = fakeredis.FakeStrictRedis()

    #@patch('common.src.common.TestRedis.connect', side_effect=mock_conn)
    @patch.object(common.TestRedis, 'connect', new=mock_conn)
    def testMockRedis(self):#, mock_conn):
        testRedis = common.TestRedis('127.0.0.1', 6379)
        #testRedis.mock_conn()
        #testRedis.connect = self.mock_conn
        #testRedis.connect()
        #result = testRedis.info()
        #self.assertIsNotNone(result)
        #self.assertIs(self.testRedis, testRedis)
        self.assertEqual(testRedis.echo('test'), b'test')


if __name__ == '__main__':
  main()
