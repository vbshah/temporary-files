n = int(input("1) Encryption 2) Decryption : "))
key = input("Type substitution string : ")
s = input("Type the string for encryption or decryption : ")
data = dict((chr(i + ord('A')), j) for i, j in enumerate(key))
ans = []
if n == 1:
    for i in s:
        try:
            ans.append(data[i])
        except:
            ans.append(i)

else:
    res = dict((v, k) for k, v in data.items())
    for i in s:
        try:
            ans.append(res[i])
        except:
            ans.append(i)

print("Answer string is", ''.join(ans))
