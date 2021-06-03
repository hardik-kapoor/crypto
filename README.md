# Project on Cryptography
* Implementation of SHA-256, RSA algorithm in python, with GUI created using PyQt
* Used RSA algorithm to encrypt images and texts
* Used SHA-256 to generate TOTP (time- based one time passwords), and to generate hashes of strings

# Important Notes!
* For the image encryption, please limit the bits of prime to 20, as above that the code will take a lot of time.
* For text encryption, code works efficiently for even primes of 500 bits, but is a bit slow for 1000 bits.

# How to Run
* Clone the repository locally, and run main.py
* OpenCV, numpy and PyQt must be installed on the pc
* use pip install cv2, pip install numpy and pip install pyqt5 on cmd to install them, if not already installed.
* For Image encryption, the image must be placed in the same directory as main.py (the directory where the repository is cloned)
