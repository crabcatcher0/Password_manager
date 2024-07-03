![Home](/my_api/app_api/staic/img/home.png)

# Password Manager
CLI based application. Integrated web-based(Django) feature for data integrity, User can directly control from command line as well use the web interface. 

## Features

### Online:
- **Register**: User can create a account and signin.
- **Browse Account**: Can view account and data.
- **Web Based**: User can now directly browse through web interface. 

### Offline:
- **Password Generation**: Generate strong passwords with customizable length requirements.
- **Account Management**: Store and manage passwords for specific accounts securely.
- **Password Strength Check**: Evaluate password strength based length, character types, and randomness.

## Installation

### To install:
Create a MySQL database with and change the name in settings.py.
For CLI use XAMPP.
1. **Clone the repository**:
   ```bash
   git clone https://github.com/crabcatcher0/Password_manager
   cd Password_manager
   
2. **Install dependency**:
   ```bash
   pip install -r requirements.txt
   
3. **Run**:
   Run the django server and
   ```bash
   cd src
   python3 main.py

## Usage
## Commands
### Online:
- **Open in browser (O)**: Opens a web interface in browser
- **Register (A)**: Signup
- **Login (L)**: Login
- **View Account Info (V)**: Display profile's information
- **Add Data to Vault (S)**: Add data to database
- **Open Vault (W)**: Displays the vault's data
- **Logout (X)**: Logout

### Offline 
- **Generate Password (G)**: Generates a random password.
- **Manage Account (M)**: Allows you to manage your specific accounts and passwords.
- **View Account (S)**: Displays information about your account.
- **Check Password Strength (C)**: Evaluates the strength of a password.
- **Quit (Q)**: Exits the application.
