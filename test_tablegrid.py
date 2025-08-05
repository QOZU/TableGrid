# test_tablegrid.py
"""
Tests for TableGrid module.
"""

import unittest
from tablegrid import TableGrid

class TestTableGrid(unittest.TestCase):
    """Test cases for TableGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TableGrid()
        self.assertIsInstance(instance, TableGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TableGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
