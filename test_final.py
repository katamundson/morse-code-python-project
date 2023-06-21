"""
Kat Amundson
CIS 189
unit test for final
"""

import unittest
from final import eng_to_morse
from final import morse_to_eng

class FinalTestCase(unittest.TestCase):

    def test_eng_to_morse(self):
        message = 'SOS'
        result = eng_to_morse(message)
        self.assertEqual(result, '... --- ... ')

    def test_morse_to_eng(self):
        message = '... --- ... '
        result = morse_to_eng(message)
        self.assertEqual(result, 'SOS ')

    def test_eng_to_morse2(self):
        message = '! @ :'
        result = eng_to_morse(message)
        self.assertEqual(result, '-.-.--  .--.-.  ---... ')

    def test_morse_to_eng2(self):
        message = '-.-.--  .--.-.  ---...'
        result = morse_to_eng(message)
        self.assertEqual(result, '! @ :')

if __name__ == "__main__":
    unittest.main()
        
