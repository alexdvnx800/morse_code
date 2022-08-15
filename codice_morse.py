import webbrowser
while True:

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    def encrypt(mess):
        cipher = ''
        for letter in mess:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
        return cipher
    def decrypt(message):
        message += ' '
 
        decipher = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
        return decipher

    def main():
        message = input("put her the text: ")
        result = encrypt(message.upper())
        print (result)
        print("use this page to translate the Morse code")
        webbrowser.open('')#Here you can put your path file 
    if __name__ == '__main__':
        main()
    loop = input('do you want write anther word [y/n]: ')
    if loop == "y":
        continue
    elif loop == "n":   
      break
    