from unittest import TestCase
from unittest import main
import os
import sys


sys.path.append(os.path.join(os.path.dirname('.')))


import downloader


class TestFoo(TestCase):

    def testFoo(self):
        self.assertEqual(5, downloader.foo(2, 3))


if __name__ == '__main__':
    main()
