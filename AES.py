from Crypto.Cipher import AES
import sys

class AESinterface:
    @staticmethod
    def setKey(key):
        asciiRange = (range(48,58) + range(97,103))
        if (all(ord(c) in asciiRange for c in key)) and (len(key) == 32):
            key = key.decode("hex")
            global aes
            aes = AES.new(key, AES.MODE_ECB)
        else:
            print "Wrong Key"
            sys.exit()

    @staticmethod
    def encrypt(plainText):
        cipherText = ""
        pad = 0
        padBlock = ""
        plainText = plainText.rstrip()
        blocks=[plainText[x:x+16] for x in range(0,len(plainText),16)]
        for elements in range(len(blocks)):
            while (len(blocks[elements]) % 16) != 0:
                blocks[elements] += '*'
                pad +=1
            cipherText += aes.encrypt(blocks[elements])
        cipherText += aes.encrypt(str(pad).zfill(16))
        return cipherText.rstrip()

    @staticmethod
    def decrypt(cipherText):
        plainText = ""
        pad = 0
        cipherText = cipherText.rstrip()
        blocks=[cipherText[x:x+16] for x in range(0,len(cipherText),16)]
        for elements in range(len(blocks)):
            if elements == (len(blocks) - 1):
                pad = aes.decrypt(blocks[elements])
            else:
                plainText += aes.decrypt(blocks[elements])
        if int(pad) == 0:
            return plainText.rstrip()
        else:
            return plainText[:-int(pad)].rstrip()

