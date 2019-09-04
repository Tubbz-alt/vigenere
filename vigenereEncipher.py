# vigenereEncipher
# alphabetArray
cipher = []
for i in range(97, 123, 1):
    cipher.append(chr(i))
    # eliminatingNonAlphabets
rawText = str.lower(input("Enter the text to encrypt:"))
rawTextCopy = ""
for i in range(0, len(rawText)):
    if str.isalpha(rawText[i]):
        rawTextCopy += rawText[i]
        # eliminatingNonAlphabets
key = str.lower(input("Enter the key to encrypt:"))
keyCopy = ""
for j in range(0, len(key)):
    if str.isalpha(key[j]):
        keyCopy += key[j]
        # encryption
encryptedCopy = ""
encrypted = ""
for k in range(0, len(rawTextCopy)):
    if k % 4 == 0:
        encryptedCopy += " "
    encryptedCopy += cipher[(cipher.index(rawTextCopy[k]) + cipher.index(keyCopy[k % len(keyCopy)]) + 1) % 26]

encrypted = str.upper(encryptedCopy)
print(encrypted)
