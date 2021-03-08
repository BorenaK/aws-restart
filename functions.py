#Double Alphabet function

def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet

alphabet = "ABC"

a = getDoubleAlphabet(alphabet)
print(a)

# get message to encrypt
def getMessage():
   stringToEncrypt = input("Please enter a message to encrypt: ")
   return stringToEncrypt

# Cipher Key
def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

# encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# main function
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #contains alphabet
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet) #double the alphabet to be able to shift the letters
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey() #get cipher key from user
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) #encrypt message
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)  #decrypt message
    print(f'Decypted Message: {myDecryptedMessage}')
    
#call the function
runCaesarCipherProgram()

