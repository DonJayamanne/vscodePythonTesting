import unittest

class PassingTests(unittest.TestCase):

    def test_passing(self):
        self.assertEqual(42, 42)

    def test_passing_still(self):
        self.assertEqual("silly walk", "silly walk")


class FailingTests(unittest.TestCase):

    def test_failure(self):
        self.assertEqual(42, -13)

    def test_failure_still(self):
        self.assertEqual("I'm right!", "no, I am!")

def test_passing():
    assert 42 == 42
  
def test_failure():
    assert 42 == -13
