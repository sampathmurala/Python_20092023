# Caesar cipher.
def caesar_cipher(text, num):
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        code = ord(char) + num
        if char.isupper() and code > ord('Z'):
            code = ord('A') + (code - ord('Z')-1)
        elif char.islower() and code > ord('z'):
            code = ord('a') + (code - ord('z') - 1)
        cipher += chr(code)
    return cipher


input_text = input("Enter your message to encrypt: ")
shift = int(input("Enter a num b/w 1...25: "))
cipher = caesar_cipher(input_text, shift)
print(cipher)
