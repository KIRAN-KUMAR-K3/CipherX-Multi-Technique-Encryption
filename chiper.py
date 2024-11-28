import numpy as np


# Monoalphabetic Cipher
def monoalphabetic_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution = key.upper()
    table = str.maketrans(alphabet, substitution)
    return plaintext.upper().translate(table)


def monoalphabetic_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution = key.upper()
    table = str.maketrans(substitution, alphabet)
    return ciphertext.upper().translate(table)


# Polyalphabetic Cipher (Vigenere)
def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    key = key.upper()
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext = ""
    for p, k in zip(plaintext, key):
        if p in alphabet:
            ciphertext += alphabet[(alphabet.index(p) + alphabet.index(k)) % 26]
        else:
            ciphertext += p
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    key = key.upper()
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = ""
    for c, k in zip(ciphertext, key):
        if c in alphabet:
            plaintext += alphabet[(alphabet.index(c) - alphabet.index(k)) % 26]
        else:
            plaintext += c
    return plaintext


# Playfair Cipher
def playfair_encrypt(plaintext, key):
    def format_key(key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is merged with I
        key = "".join(sorted(set(key.upper()), key=lambda x: key.index(x)))
        return "".join([c for c in key + alphabet if c not in key or key.count(c) == 1])

    def format_text(text):
        text = text.upper().replace("J", "I").replace(" ", "")
        result = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                result.append(text[i] + "X")
                i += 1
            else:
                result.append(text[i:i + 2])
                i += 2
        if len(result[-1]) == 1:
            result[-1] += "X"
        return result

    def find_position(char, table):
        for row, line in enumerate(table):
            for col, letter in enumerate(line):
                if char == letter:
                    return row, col

    key_table = [list(format_key(key)[i:i + 5]) for i in range(0, 25, 5)]
    pairs = format_text(plaintext)
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_table)
        row2, col2 = find_position(pair[1], key_table)
        if row1 == row2:
            ciphertext += key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_table[row1][col2] + key_table[row2][col1]
    return ciphertext


# Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper().replace(" ", "")
    n = key_matrix.shape[0]
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)
    chunks = [plaintext[i:i + n] for i in range(0, len(plaintext), n)]
    ciphertext = ""
    for chunk in chunks:
        chunk_vector = [alphabet.index(c) for c in chunk]
        result_vector = np.dot(key_matrix, chunk_vector) % 26
        ciphertext += "".join(alphabet[int(v)] for v in result_vector)
    return ciphertext


# Transposition Cipher
def single_transposition_encrypt(plaintext, key):
    key_order = sorted(list(key))
    columns = len(key)
    grid = [plaintext[i:i + columns] for i in range(0, len(plaintext), columns)]
    grid[-1] += "X" * (columns - len(grid[-1]))
    ciphertext = ""
    for column in key_order:
        index = key.index(column)
        ciphertext += "".join(row[index] for row in grid)
    return ciphertext


def double_transposition_encrypt(plaintext, key1, key2):
    first_pass = single_transposition_encrypt(plaintext, key1)
    second_pass = single_transposition_encrypt(first_pass, key2)
    return second_pass


# Example Usage
if __name__ == "__main__":
    # Monoalphabetic Cipher Example
    mono_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mono_encrypted = monoalphabetic_encrypt("HELLO WORLD", mono_key)
    mono_decrypted = monoalphabetic_decrypt(mono_encrypted, mono_key)
    print("Monoalphabetic Encrypted:", mono_encrypted)
    print("Monoalphabetic Decrypted:", mono_decrypted)

    # Polyalphabetic Cipher Example
    vigenere_encrypted = vigenere_encrypt("HELLO WORLD", "KEY")
    vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, "KEY")
    print("Vigenere Encrypted:", vigenere_encrypted)
    print("Vigenere Decrypted:", vigenere_decrypted)

    # Playfair Cipher Example
    playfair_encrypted = playfair_encrypt("HELLO WORLD", "KEYWORD")
    print("Playfair Encrypted:", playfair_encrypted)

    # Hill Cipher Example
    hill_key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix
    hill_encrypted = hill_encrypt("HELLO WORLD", hill_key)
    print("Hill Encrypted:", hill_encrypted)

    # Transposition Cipher Example
    single_encrypted = single_transposition_encrypt("HELLO WORLD", "SECRET")
    double_encrypted = double_transposition_encrypt("HELLO WORLD", "SECRET", "KEY")
    print("Single Transposition Encrypted:", single_encrypted)
    print("Double Transposition Encrypted:", double_encrypted)
