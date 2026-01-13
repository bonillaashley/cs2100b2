import unittest 
from unittest.mock import patch, Mock

from main import (
    greet_person
    is_cold_f
    THRESHOLD_TEMP_F
    
)

class TestMainApp(unittest.TestCase): 
 @patch('builtins.input', side_effect=['alice']) 
 @patch('builtins.input') 

 def test_greetperson(self, mock_print: Mock, _: Mock) -> None: 
        """"Say hello to ashley""" 
        greet_person()
        expected_calls= [ 
            unittest.mock.call("howdy, ashley"), 
        
        ]
        mock_print.assert_has_calls(expected_calls) 

    def test_iscoldf_abovethresh()-> None:
     "tests is_cold_f for 70"
     self.assertFalse(is_cold_f(70))


    def test_iscoldf_boiling(self)-> None:
     "tests is_cold_f for 212"
     self.assertFalse(is_cold_f(212))

    def test_isfreezingf_belowthresh(self)-> None:
     "tests is_freezing_f for 32"
          self.assertTrue(is_cold_f(32))
     



if __ name__== "__main__": 
     unittest.main()