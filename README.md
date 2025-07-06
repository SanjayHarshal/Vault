Vault

A command-line application to securely encrypt .txt files and passwords. Includes secure password generation with a secure login system.

Actions :

- Encrypt .txt files
- Decrypt the encrypted files
- Encrypt and store passwords
- Get stored password in clipboard
- Generate a secure password
- Exit the application

Highlights :

- Secure login system in place
- Only 1 user allowed in a system
- Can sign-up or sign-in the application based on previous interactions
- Inputs involving passwords is masked
- Password asked twice for secure login and secure confirmation by the user
- Password not visible for security purposes
- Asks name or path or password again if user provides it incorrectly
- Retrieving Passwords in the clipboard (ready to paste) for security purposes
- Creates necessary folders and files (if not already exists) in the first run
- Handles any file or path not found smoothly
- .txt files are only allowed for encryption
- Handles password confirmation and certain name not found situations

Folder Structure :

vault/
├── vault.py
├── Encrypted Files/
│ └── .gitkeep
├── Decrypted Files/
│ └── .gitkeep
├── Password/
│ └── .gitkeep
├── Key/
│ └── .gitkeep
├── Login.txt
├── README.md
└── requirements.txt

Folder And File Purpose :

- vault.py : Python script to run the application
- Encrypted Files/ : Folder which stores the encrypted files
- Decrypted Files/ : Folder which stores the decrypted files
- Password/ : Folder which stores encrypted password and fernet keys
- Key/ : Folder which stores fernet keys for encrypts files
- Login.txt : Text file which contains the hashed password for login system
- README.md : Markdown file which explains details of the projects
- requirements.txt : Text file which contains the required modules which are to be installed

How To Run :

- Install the latest version of python
- Open command prompt in project folder
- Install required packages by typing :
  ```
  pip install -r requirements.txt
  ```
- To start the app type :
  ```
  python vault.py
  ```
- First time users are asked to sign-up. Then you can sign-in and perform any action as mentioned above

Modules Used :

- os
- string
- pyperclip
- bcrypt
- getpass
- random
- secrets
- cryptography.fernet

Author :

Made By Sanjay Harshal
Github : https://github.com/SanjayHarshal
