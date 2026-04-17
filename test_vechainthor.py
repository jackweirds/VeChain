# test_vechainthor.py
"""
Tests for VeChainThor module.
"""

import unittest
from vechainthor import VeChainThor

class TestVeChainThor(unittest.TestCase):
    """Test cases for VeChainThor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VeChainThor()
        self.assertIsInstance(instance, VeChainThor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VeChainThor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
