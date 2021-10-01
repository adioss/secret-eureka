import unittest

from secret_eureka.main import any_method


class DefaultMainTestCase(unittest.TestCase):
    """ Test module """

    def test_any_method(self):
        """ test """

        self.assertEqual(any_method(), 'changeme')
