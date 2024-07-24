def caesar_cipher(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result

# Example usage
text = "Hello, World!"
shift = 8
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted: {encrypted_text}")

# Decrypting by using the negative of the same shift value
decrypted_text = caesar_cipher(encrypted_text, -shift)
print(f"Decrypted: {decrypted_text}")
