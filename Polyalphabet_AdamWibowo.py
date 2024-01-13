def polyalphabet_encrypt(text, key1, key2, key3):
    encrypted_text = ""
    key_length = len(key1)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = 0
            if char.islower():
                shift = ord('a')
            elif char.isupper():
                shift = ord('A')

            char_code = ord(char) - shift
            char_code = (char_code + (ord(key1[i % key_length]) - ord('a'))) % 26
            char_code = (char_code + (ord(key2[i % key_length]) - ord('a'))) % 26
            char_code = (char_code + (ord(key3[i % key_length]) - ord('a'))) % 26

            encrypted_char = chr(char_code + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


def polyalphabet_decrypt(text, key1, key2, key3):
    decrypted_text = ""
    key_length = len(key1)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = 0
            if char.islower():
                shift = ord('a')
            elif char.isupper():
                shift = ord('A')

            char_code = ord(char) - shift
            char_code = (char_code - (ord(key3[i % key_length]) - ord('a'))) % 26
            char_code = (char_code - (ord(key2[i % key_length]) - ord('a'))) % 26
            char_code = (char_code - (ord(key1[i % key_length]) - ord('a'))) % 26

            decrypted_char = chr(char_code + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

while True:
    print("Menu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Pilih tindakan (1/2/3): ")

    if choice == '1':
        plaintext = input("Masukkan teks yang akan dienkripsi: ")
        key1 = input("Masukkan kunci 1: ")
        key2 = input("Masukkan kunci 2: ")
        key3 = input("Masukkan kunci 3: ")
        encrypted_text = polyalphabet_encrypt(plaintext, key1, key2, key3)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == '2':
        ciphertext = input("Masukkan teks terenkripsi: ")
        key1 = input("Masukkan kunci 1: ")
        key2 = input("Masukkan kunci 2: ")
        key3 = input("Masukkan kunci 3: ")
        decrypted_text = polyalphabet_decrypt(ciphertext, key1, key2, key3)
        print("Teks terdekripsi:", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")