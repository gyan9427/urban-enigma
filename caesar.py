# This program creates a key to cipher ceasar encryption

# function for key

def key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[((cnt+n)%len(letters))]
        cnt += 1
    return key

def encode(key,message):
    cipher = ''
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def de_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

en_key = key(3)
print(en_key)
message = "THIS IS WHAT HAPPENS"
crypted = encode(en_key,message)
print(crypted)
dcrypt_key = de_key(en_key)
decode = encode(dcrypt_key,crypted)
print(decode)

for i in range(26):
    # insert code here
    fkey = key(i)
    dkey = de_key(fkey)
    message= encode(dkey,crypted)
    print(message)
