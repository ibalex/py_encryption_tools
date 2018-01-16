import unittest
from code.one_time_pad import OneTimePad
from builtins import ValueError


class TestOneTimePad(unittest.TestCase):
    
    def test_regression(self):
        self.assertTrue(True)
        potential_rounds = [0, 1, 2, 3, 11, 100, 101, -5]
        strings = [' ', 
                   'Foo', 
                   '123', 
                   '!', 
                   "\\", 
                   " \\!123Foo", 
                   'Foo$ $$%', 
                   'Something fairly long 123 to testTHISandTHAT for good MEASURE and great MEASURE!!! $$$',
                   '0x510Fd21108E7E3f4B1A7F610eFAB46980504A304']
        
        for rounds in potential_rounds:
            for clear_text in strings:
                for key in strings:
                    self._verify_encryption(clear_text, key, rounds)
    
    
    def _verify_encryption(self, clear_text, key, rounds=1):
        print("verifying - Clear Text: {0}, Key: {1}, Rounds: {2}".format(clear_text, key, rounds))
        cipher = OneTimePad.encrypt(clear_text, key, rounds)
        clear = OneTimePad.decrypt(cipher, key, rounds)
        self.assertEqual(clear_text, clear)

    def test_warn_bad_char_in_text(self):
        clear_text = "Foo {0} Bar".format(chr(1))
        self.assertRaises(ValueError, self._verify_encryption, clear_text, 'key', 1)

    def test_warn_bad_char_in_key(self):
        key = "Foo {0} Bar".format(chr(1))
        self.assertRaises(ValueError, self._verify_encryption, 'clear_text', key, 1)

