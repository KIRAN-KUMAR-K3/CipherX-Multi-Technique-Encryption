import numpy as np

# -------------------- MONOALPHABETIC CIPHER --------------------
def monoalphabetic_encrypt(text, key):
    encrypted = ''.join(key[ord(c) - ord('A')] if c.isalpha() else c for c in text.upper())
    return encrypted

def monoalphabetic_decrypt(text, key):
    inverse_key = {v: k for k, v in enumerate(key)}
    decrypted = ''.join(chr(inverse_key[c] + ord('A')) if c.isalpha() else c for c in text.upper())
    return decrypted

# -------------------- VIGENÈRE CIPHER --------------------
def vigenere_encrypt(text, key):
    text, key = text.upper(), key.upper()
    encrypted = ''.join(chr((ord(t) + ord(k) - 2 * ord('A')) % 26 + ord('A'))
                        if t.isalpha() else t
                        for t, k in zip(text, (key * (len(text) // len(key) + 1))[:len(text)]))
    return encrypted

def vigenere_decrypt(text, key):
    text, key = text.upper(), key.upper()
    decrypted = ''.join(chr((ord(t) - ord(k) + 26) % 26 + ord('A'))
                        if t.isalpha() else t
                        for t, k in zip(text, (key * (len(text) // len(key) + 1))[:len(text)]))
    return decrypted

# -------------------- PLAYFAIR CIPHER --------------------
def preprocess_text(text):
    text = ''.join(filter(str.isalpha, text)).upper()
    if len(text) % 2 != 0:
        text += 'X'  # Padding
    return text

def create_key_table(key):
    key = ''.join(sorted(set(key.upper()), key=key.index)) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = ''.join(sorted(set(key), key=key.index))
    return [key[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_table):
    for i, row in enumerate(key_table):
        for j, c in enumerate(row):
            if char == c:
                return i, j
    return None

def playfair_encrypt(text, key):
    text = preprocess_text(text)
    key_table = create_key_table(key)
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    encrypted = ""
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_table)
        row2, col2 = find_position(pair[1], key_table)
        if row1 == row2:  # Same row
            encrypted += key_table[row1][(col1 + 1) % 5]
            encrypted += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted += key_table[(row1 + 1) % 5][col1]
            encrypted += key_table[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted += key_table[row1][col2]
            encrypted += key_table[row2][col1]
    return encrypted

# -------------------- HILL CIPHER --------------------
def hill_encrypt(text, key_matrix):
    text = preprocess_text(text)
    n = key_matrix.shape[0]
    while len(text) % n != 0:
        text += 'X'
    text_vector = np.array([ord(c) - ord('A') for c in text]).reshape(-1, n).T
    encrypted_vector = (np.dot(key_matrix, text_vector) % 26).T.flatten()
    encrypted = ''.join(chr(c + ord('A')) for c in encrypted_vector)
    return encrypted

# -------------------- MAIN --------------------
if __name__ == "__main__":
    print("Cipher Program - Choose a Cipher to Encrypt Text\n")
    print("1. Monoalphabetic Cipher")
    print("2. Vigenère Cipher")
    print("3. Playfair Cipher")
    print("4. Hill Cipher\n")

    choice = input("Enter the number corresponding to your choice: ").strip()

    if choice not in {'1', '2', '3', '4'}:
        print("Invalid choice. Please restart the program and try again.")
        exit()

    text = input("\nEnter the text to encrypt: ").strip()
    if not text:
        print("Input text cannot be empty!")
        exit()

    if choice == '1':
        mono_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
        encrypted = monoalphabetic_encrypt(text, mono_key)
        print(f"\nMonoalphabetic Encrypted Text: {encrypted}")

    elif choice == '2':
        key = input("Enter the Vigenère key: ").strip()
        encrypted = vigenere_encrypt(text, key)
        print(f"\nVigenère Encrypted Text: {encrypted}")

    elif choice == '3':
        key = input("Enter the Playfair key: ").strip()
        encrypted = playfair_encrypt(text, key)
        print(f"\nPlayfair Encrypted Text: {encrypted}")

    elif choice == '4':
        print("Enter a 3x3 Hill cipher key matrix (space-separated, 9 integers):")
        key_input = input().strip()
        try:
            key_values = list(map(int, key_input.split()))
            if len(key_values) != 9:
                raise ValueError("Matrix must have exactly 9 integers.")
            hill_key = np.array(key_values).reshape(3, 3)
            encrypted = hill_encrypt(text, hill_key)
            print(f"\nHill Cipher Encrypted Text: {encrypted}")
        except Exception as e:
            print(f"Error: {e}")
