n=input("1) Encryption 2) Decryption : ")
s=raw_input("type string for encryption : ")
key=input("type key value : ")
tmp=""
if n==1:
    for i in s:
        if i<'a':
            tmp+=chr((ord(i)-ord('A')+key)%26+ord('A'))
        else:
            tmp+=chr((ord(i)-ord('a')+key)%26+ord('a'))
else:
    for i in s:
        if i<'a':
            tmp+=chr((ord(i)-ord('A')-key)%26+ord('A'))
        else:
            tmp+=chr((ord(i)-ord('a')-key)%26+ord('a'))

print tmp