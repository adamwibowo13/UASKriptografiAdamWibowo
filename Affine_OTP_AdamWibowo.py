def affine_encrypt(text, a, b):
    encrypted_text = ""
    m = 26  # Panjang alfabet

    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((a * (ord(char) - ord('a')) + b) % m + ord('a'))
            elif char.isupper():
                encrypted_text += chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
        else:
            encrypted_text += char

    return encrypted_text

def otp_encrypt(plain_text, key):
    encrypted_text = ""
    
    # Enkripsi menggunakan Affine Cipher
    affine_key = 5  # Ganti dengan nilai kunci Affine Cipher yang sesuai
    affine_result = affine_encrypt(plain_text, 3, 7)  # Ganti dengan nilai a dan b yang sesuai

    # Ubah hasil Affine Cipher ke ASCII
    affine_ascii = text_to_ascii(affine_result)

    # Ubah kunci ke ASCII
    ascii_key = text_to_ascii(key)

    # XOR hasil Affine Cipher dengan kunci
    for a, k in zip(affine_ascii, ascii_key):
        encrypted_text += chr(a ^ k)

    return encrypted_text

while True:
    print("Pilihan:")
    print("1. Enkripsi Affine + OTP")
    print("2. Keluar")

    choice = input("Masukkan pilihan (1/2): ")

    if choice == "1":
        plainteks_input = input("Masukkan plainteks: ")
        kunci_input = input("Masukkan kunci OTP: ")
        hasil_enkripsi = otp_encrypt(plainteks_input, kunci_input)
        print(f"Hasil Enkripsi Affine + OTP: {hasil_enkripsi}")
    elif choice == "2":
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")
