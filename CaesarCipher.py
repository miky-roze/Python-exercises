# Create class CaesarCipher:
#   the init method takes 2 parameters 'alphabet' and 'key'
#   use @property to create a read-only attribute 'cipher' that contains encrypted alphabet
#   Add method encrypt that encrypts given message
#   Add method decrypt that decrypts given message


class CaesarCipher:

    @staticmethod
    def generate_cipher(alphabet, key=2):

        encryptedAlphabet = list()
        for char in alphabet:
            newIndex = (alphabet.index(char) + key) % len(alphabet)
            encryptedAlphabet.append(alphabet[newIndex])

        return ''.join(encryptedAlphabet)

    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key
        self.cipher = self.generate_cipher(self.alphabet, self.key)

    @property
    def cipher(self):
        return self.cipher

    @cipher.setter
    def cipher(self, value):
        self._cipher = value

    def encrypt(self, message):
        encryptedMessage = ''
        for letter in message:
            if letter.isalpha():
                encryptedMessage += self.cipher[self.alphabet.index(letter)]
            else:
                encryptedMessage += letter

        return encryptedMessage

    def decrypt(self, message):
        decryptedMessage = ''
        for letter in message:
            if letter.isalpha():
                decryptedMessage += self.alphabet[self.cipher.index(letter)]
            else:
                decryptedMessage += letter

        return decryptedMessage
