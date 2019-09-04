#vigenereDecipher
                                                                                                #alphabetArray
cipher=[]
for i  in range(97,123,1):
        cipher.append(chr(i))
                                                                                                #eliminatingNonAlphabets
encrypted=str.lower(input("Enter the text to decrypt:"))
encryptedCopy=""
for i in range(0,len(encrypted)): 
        if  str.isalpha(encrypted[i]):
                encryptedCopy+=encrypted[i]
                                                                                                #eliminatingNonAlphabets
key=str.lower(input("Enter the key to decrypt:"))
keyCopy=""
for j in range(0,len(key)):
        if str.isalpha(key[j]):
                keyCopy+=key[j]
                                                                                                #decryption
rawTextCopy=""
rawText=""
for k in range(0,len(encryptedCopy)):
        rawTextCopy+=cipher[(cipher.index(encryptedCopy[k])-cipher.index(keyCopy[k%len(keyCopy)])-1)%26]

rawText=str.upper(rawTextCopy)
print(rawText)
