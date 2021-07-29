# Implement a class 'MorseCode' that has 2 static methods responsible for encoding and decoding messages
# Mappings between character and sequence are hold in MORSE_CODE and MORSE_CODE_FLIPPED dictionaries
# Intervals between characters in a word are simulated by a single space (' ')
# Intervals between words are simulated by sequence: ' / '

MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}
MORSE_CODE_FLIPPED = dict(zip(MORSE_CODE.values(), MORSE_CODE.keys()))


class MorseCode:

    @staticmethod
    def encrypt(message: str):
        message = message.upper()
        encodedMessage = str()

        for char in message:
            if char == ' ':
                encodedMessage += '/ '
            else:
                encodedMessage += MORSE_CODE[char] + ' '

        return encodedMessage.strip()

    @staticmethod
    def decrypt(message: str):
        decodedMessage = str()
        sequences = message.split()

        for sequence in sequences:
            if sequence == '/':
                decodedMessage += ' '
            else:
                decodedMessage += MORSE_CODE_FLIPPED[sequence]

        return decodedMessage

