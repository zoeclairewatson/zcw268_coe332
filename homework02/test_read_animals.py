import unittest

from read_animals import new_functionality_breeding

class TestReadAnimals(unittest.TestCase):

    def test_new_functionality_breeding(self):
        
        self.assertRaises(AssertionError, new_functionality_breeding, 4)
        self.assertRaises(AssertionError, new_functionality_breeding, ['cat', 'dog'])
        self.assertRaises(AssertionError, new_functionality_breeding, {'bunny', 'bull', 'snake'}


if __name__ == '__main__':
    unittest.main()
