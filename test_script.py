import unittest
import sys
from unittest.mock import patch
from io import StringIO
from script import data_input

class functionTesting(unittest.TestCase):
    @patch('sys.stdin', StringIO('http://www.bbc.co.uk/iplayer'))
    
    def test_standard_input(self): 
        # Check input and output match
        expected_out = ['http://www.bbc.co.uk/iplayer']
        self.assertEqual(data_input(), expected_out)
        
    

if __name__ == "__main__":
    unittest.main()
