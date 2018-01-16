from builtins import ValueError



class OneTimePad:
    
    CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()`~-_=+[{]}\\|;:\'",<.>/? '
    COUNT = len(CHARS)
    MAP = dict(zip(CHARS, range(COUNT)))

    @classmethod
    def encrypt(cls, clear_text, key, rounds=1):
        cls._check_for_chars(clear_text)
        cls._check_for_chars(key)        
        cipher_text = list(clear_text)
        for _ in range(abs(rounds)):
            for i in range(len(cipher_text)):
                cipher_text[i] = cls._shift(cipher_text[i], key[i % len(key)])
        return ''.join(cipher_text)
    
    @classmethod
    def decrypt(cls, cipher_text, key, rounds=1):
        clear_text = list(cipher_text)
        for _ in range(abs(rounds)):
            for i in range(len(clear_text)):
                clear_text[i] = cls._unshift(clear_text[i], key[i % len(key)])
        return ''.join(clear_text)

    @classmethod
    def _check_for_chars(cls, string):
        for char in string:
            if char not in cls.CHARS:
                raise ValueError("Supported character set is: {0}".format(cls.CHARS))

    @classmethod
    def _shift(cls, clear_char, key_char):
        return cls.CHARS[(cls.MAP[clear_char] + cls.MAP[key_char]) % cls.COUNT]
    
    @classmethod
    def _unshift(cls, cipher_char, key_char):
        return cls.CHARS[(cls.MAP[cipher_char] - cls.MAP[key_char])]

