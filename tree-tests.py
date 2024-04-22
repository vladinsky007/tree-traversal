import unittest
from tree import Tree

class TestTreeMethods(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)

    def test_find_existing(self):
        result = self.tree._find(3, self.tree.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 3)

    def test_find_non_existing(self):
        result = self.tree._find(6, self.tree.root)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()