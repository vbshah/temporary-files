n = int(input("1) Encryption 2) Decryption : "))
s = input("Type string for  : ")
key = int(input("Type key value : "))
tmp = ""
if n == 1:
    for i in s:
        if i < 'a':
            tmp += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
        else:
            tmp += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
else:
    for i in s:
        if i < 'a':
            tmp += chr((ord(i) - ord('A') - key) % 26 + ord('A'))
        else:
            tmp += chr((ord(i) - ord('a') - key) % 26 + ord('a'))

print("Answer string is", tmp)
