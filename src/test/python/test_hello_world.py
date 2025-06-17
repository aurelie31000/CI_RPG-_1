# src/test/python/test_hello_world.py
import unittest
# Utilise l'import absolu grâce aux fichiers __init__.py
from src.main.python.hello_world import get_message

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(get_message(), "Hello World")

    def test_true_equals_true(self):
        self.assertTrue(True == True)

if __name__ == '__main__':
    unittest.main()

