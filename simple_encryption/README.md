# 🔐 Secure Text Encryptor

Welcome to **Secure Text Encryptor**, a simple yet effective tool for encrypting and decrypting messages using a randomly generated key. Keep your communications private and secure! 🔒

## 🚀 Features

- 🔑 **Custom Encryption Key Generation**
- 📝 **Encrypt & Decrypt Messages**
- 💾 **Save & Load Key for Future Use**
- ⚡ **Fast & Easy to Use**

## 🎮 How to Use

### 1️⃣ Running the Program
1. **Copy & run the script**:
   ```sh
   python encryptor.py
   ```

### 2️⃣ Features in Detail

#### 🔏 Encrypt a Message
- Enter your text and the script will generate an encrypted version using a stored or newly generated key.

#### 🔓 Decrypt a Message
- Enter an encrypted message, and if the key matches, the original text will be revealed.

#### 🔑 Generate a New Key
- Generates a fresh encryption key and saves it to `cipher_key.json` for future use.

### 🖥 Example Usage
```
🔏 ENCRYPTION MODE 🔏
Enter the text to encrypt: Hello, World!
🔒 Encrypted Message:
📜 @zXo!w&k3P$
```

```
🔓 DECRYPTION MODE 🔓
Enter the text to decrypt: @zXo!w&k3P$
✅ Decrypted Message:
📜 Hello, World!
```

## ⚠ Important Notes
- **The encryption key is required to decrypt messages!**
- If you lose `cipher_key.json`, decryption will not be possible.
- Keep the key file secure and do not share it publicly.

---

🔐 **Stay Secure, Encrypt Your Messages!** 🔒

