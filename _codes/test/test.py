import unittest

class TestSample(unittest.TestCase):
    def setUp(self):
        print("setUp()")

    def tearDown(self):
        print("tearDown()")

    def test_a(self):
        print("test a")
        self.assertEqual(1, 1)

    def test_b(self):
        print("test b")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
