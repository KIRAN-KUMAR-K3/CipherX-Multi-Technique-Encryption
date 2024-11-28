# CipherX: Multi-Technique Encryption

**CipherX** is a Python-based tool that implements multiple encryption algorithms to encrypt and decrypt text. This project supports several popular cipher techniques, including:

- **Monoalphabetic Cipher**
- **Vigenère Cipher**
- **Playfair Cipher**
- **Hill Cipher**

Each cipher is implemented in a modular way, allowing you to easily add new encryption methods if desired. CipherX is designed to showcase different cryptographic techniques and provide a hands-on way to understand their implementation.

## Features

- Multiple encryption techniques in one tool.
- User-friendly interface with dynamic text input.
- Easy-to-use, supporting both encryption and decryption of messages.
- Customizable keys for each encryption technique.
- Error validation for robust performance.

## Installation

To get started with **CipherX**, you need to have Python installed on your machine. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Steps to install:

1. Clone this repository:

   ```bash
   git clone https://github.com/KIRAN-KUMAR-K3/CipherX-Multi-Technique-Encryption.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CipherX-Multi-Technique-Encryption
   ```

3. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. After cloning the repository, run the script:

   ```bash
   python run.py
   ```

2. The program will prompt you to choose an encryption technique and enter the text you want to encrypt or decrypt.

3. Select the appropriate cipher technique (Monoalphabetic, Vigenère, Playfair, or Hill) and provide the required key if necessary.

4. The tool will display the encrypted or decrypted text based on your input.

## Example

### Monoalphabetic Encryption

**Input:**

```
Text: HELLO WORLD
Key: A-Z (shifted)
Encrypted: ITSSG VGKSR
```

### Vigenère Encryption

**Input:**

```
Text: HELLO WORLD
Key: KEY
Encrypted: RIJVS GSPVH
```

### Playfair Encryption

**Input:**

```
Text: HELLO WORLD
Key: KEYWORD
Encrypted: GYFFKOKCGC
```

### Hill Encryption

**Input:**

```
Text: HELLO
Key: 3x3 matrix
Encrypted: JGDDV
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by various cryptography tutorials and resources.
- Built with Python for a simple and effective implementation of classic ciphers.

