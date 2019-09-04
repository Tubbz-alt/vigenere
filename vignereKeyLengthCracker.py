import math
rawText=str.lower(input("Enter the intercepted text:"))
rawTextCopy=""
for i in range(0,len(rawText)): 
        if  str.isalpha(rawText[i]):
                rawTextCopy+=rawText[i]

numberList=[]
for j in range (len(rawTextCopy),3,-1):
        for k in range(0,len(rawTextCopy)-j+1,1):
                testText=rawTextCopy[k:k+j]
                for l in range(k+1,len(rawTextCopy)-j,1):
                        testText2=rawTextCopy[l:l+j]
                        if testText==testText2:
                                print(testText)
                                numberList.append(l-k)
print(math.lcm(numberList))
