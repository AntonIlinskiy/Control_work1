import string


def encrypt(text, key):
    encrypted_text = ""
    alphabet = string.ascii_lowercase

    for char in text:
        if char.lower() in alphabet:
            if char.islower():
                index = (alphabet.index(char) + key) % len(alphabet)
                encrypted_text += alphabet[index]
            else:
                index = (alphabet.index(char.lower()) + key) % len(alphabet)
                encrypted_text += alphabet[index].upper()
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, key):
    return encrypt(encrypted_text, -key)


text = "Всем привет"
key = 3
encrypted_text = encrypt(text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Исходный текст:", text)
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)
