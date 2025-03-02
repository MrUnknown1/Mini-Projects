import random as rd
import string as st
import json
import time

# 🎨 Define Character Set
chars = " " + st.punctuation + st.digits + st.ascii_letters
chars = list(chars)  # Convert to list

# 🌟 Generate a New Key
def generate_key():
    key = chars.copy()
    rd.shuffle(key)
    return key

# 💾 Save Key to File
def save_key(key, filename="cipher_key.json"):
    with open(filename, "w") as file:
        json.dump(key, file)

# 🔓 Load Key from File
def load_key(filename="cipher_key.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# 🔐 Encrypt Function
def encrypt(text, key):
    return "".join(key[chars.index(letter)] if letter in chars else letter for letter in text)

# 🔓 Decrypt Function
def decrypt(text, key):
    return "".join(chars[key.index(letter)] if letter in key else letter for letter in text)

# 🎭 Fancy Printing Functions
def print_header():
    print("\n" + "="*40)
    print(" 🔐 SECURE TEXT ENCRYPTOR 🔐".center(40))
    print("="*40 + "\n")

def print_menu():
    print("\n" + "-"*40)
    print(" 1️⃣  Encrypt a Message")
    print(" 2️⃣  Decrypt a Message")
    print(" 3️⃣  Generate a New Key 🔑")
    print(" 4️⃣  Exit 🚪")
    print("-"*40)

# 🚀 Main Program
def main():
    print_header()
    
    key = load_key()
    if key is None:
        print("⚠️  No existing key found. Generating a new one... 🔄")
        key = generate_key()
        save_key(key)
        time.sleep(1)
        print("✅ New encryption key generated!")

    while True:
        print_menu()
        choice = input("\n👉 Choose an option (1-4): ")

        if choice == "1":
            print("\n🔏 ENCRYPTION MODE 🔏")
            plain_text = input("Enter the text to encrypt: ")
            cipher_text = encrypt(plain_text, key)
            print("\n🔒 Encrypted Message:")
            print("📜 " + cipher_text)
            print("-"*40)

        elif choice == "2":
            print("\n🔓 DECRYPTION MODE 🔓")
            cipher_text = input("Enter the text to decrypt: ")
            plain_text = decrypt(cipher_text, key)
            print("\n✅ Decrypted Message:")
            print("📜 " + plain_text)
            print("-"*40)

        elif choice == "3":
            key = generate_key()
            save_key(key)
            print("\n🔑 A new encryption key has been generated!")
            print("⚠️  Remember to save the key file for future decryption!")

        elif choice == "4":
            print("\n👋 Exiting... Stay Secure! 🔒")
            time.sleep(1)
            break

        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
