# encryption using cipher techniques
def encrypt_cipher(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    
    return result


text = "AttackOnTitan"
s = 5
print("Text:" + text)
print("Shift:" + str(s))
print("Cipher code:" + encrypt_cipher(text,s))
