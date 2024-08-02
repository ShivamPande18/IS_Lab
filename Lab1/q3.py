import numpy as np

def to_lower_case(text):
    return text.lower()

def remove_spaces(text):
    return text.replace(" ", "")

def generate_key_table(key):
    key = remove_spaces(to_lower_case(key))
    key = key.replace('j', 'i')
    key = ''.join(dict.fromkeys(key))  # Remove duplicate letters

    alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'j' is excluded
    key_table = [c for c in key if c in alphabet]

    for char in alphabet:
        if char not in key_table:
            key_table.append(char)

    key_table = np.array(key_table).reshape(5, 5)
    return key_table

def search(key_table, a, b):
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    p1 = p2 = None
    for i in range(5):
        for j in range(5):
            if key_table[i, j] == a:
                p1 = (i, j)
            elif key_table[i, j] == b:
                p2 = (i, j)
    return p1, p2

def decrypt(cipher, key):
    key_table = generate_key_table(key)
    deciphered = []

    for i in range(0, len(cipher), 2):
        p1, p2 = search(key_table, cipher[i], cipher[i+1])

        if p1[0] == p2[0]:
            deciphered.append(key_table[p1[0], (p1[1]-1)%5])
            deciphered.append(key_table[p2[0], (p2[1]-1)%5])
        elif p1[1] == p2[1]:
            deciphered.append(key_table[(p1[0]-1)%5, p1[1]])
            deciphered.append(key_table[(p2[0]-1)%5, p2[1]])
        else:
            deciphered.append(key_table[p1[0], p2[1]])
            deciphered.append(key_table[p2[0], p1[1]])

    return ''.join(deciphered)

# Driver code
if __name__ == "__main__":
    key = "Monarchy"
    print("Key Text:", key)

    cipher = "gatlmzclrqtx"
    print("Ciphertext:", cipher)

    decrypted_text = decrypt(cipher, key)
    print("Deciphered text:", decrypted_text)
