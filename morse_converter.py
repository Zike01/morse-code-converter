class MorseConverter:
    def __init__(self):
        self.MORSE_CODE_DICT = {'A': '.-',     'B': '-...',   'C': '-.-.',
                                'D': '-..',    'E': '.',      'F': '..-.',
                                'G': '--.',    'H': '....',   'I': '..',
                                'J': '.---',   'K': '-.-',    'L': '.-..',
                                'M': '--',     'N': '-.',     'O': '---',
                                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                                'S': '...',    'T': '-',      'U': '..-',
                                'V': '...-',   'W': '.--',    'X': '-..-',
                                'Y': '-.--',   'Z': '--..',

                                '0': '-----',  '1': '.----',  '2': '..---',
                                '3': '...--',  '4': '....-',  '5': '.....',
                                '6': '-....',  '7': '--...',  '8': '---..',
                                '9': '----.',

                                '.': '.-.-.-', ',': '--..--', '?': '..--..',
                                "'": '.----.', '!': '-.-.--', '/': '-..-.',
                                '(': '-.--.',  ')': '-.--.-', '&': '.-...',
                                ':': '---...', ';': '-.-.-.', '=': '-...-',
                                '+': '.-.-.',  '-': '-....-', '_': '..--.-',
                                '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
                                }

    def translate(self, text):
        """
        Converts the text input into morse code.
        :param text:
        """
        morse_translation = ""
        # Loop through characters in text input
        for char in text:
            # Compare with keys in morse code dictionary
            for key in self.MORSE_CODE_DICT:
                if char.upper() == key:
                    morse_translation += self.MORSE_CODE_DICT[key] + " "
        return morse_translation

