# test_agilesprint.py
"""
Tests for AgileSprint module.
"""

import unittest
from agilesprint import AgileSprint

class TestAgileSprint(unittest.TestCase):
    """Test cases for AgileSprint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgileSprint()
        self.assertIsInstance(instance, AgileSprint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgileSprint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
