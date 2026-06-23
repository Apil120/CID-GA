# CID-GA

A simple Python proof-of-concept for SSH login testing using random password attempts.

## Project Overview

This repository contains a lightweight script that uses `paramiko` to connect to an SSH server and repeatedly attempts authentication with randomly generated passwords.

> Note: This project is intended for educational and authorized testing only. Do not use it against systems or networks without explicit permission.

## Files

- `main.py` - Main script that prompts for SSH server IP and number of login attempts, then performs repeated connection attempts with random passwords.
- `utils.py` - Contains `RandomStringGenerator`, which generates random strings of length 5-50 from letters, digits, and punctuation.
- `requirements.txt` - Python dependencies required to run the project.

## Dependencies

The project depends on:

- `paramiko`
- `cryptography`
- `bcrypt`
- `cffi`
- `pycparser`
- `PyNaCl`
- `invoke`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the repository directory:

```bash
python main.py
```

Then enter:

1. The SSH server IP address
2. The number of login attempts

The script will attempt to connect using the username `vboxuser` and a random password for each iteration.

## Behavior

- Uses `paramiko.SSHClient` to initiate SSH connections.
- Handles authentication failures and connection errors.
- Sleeps 1 second between attempts.

## Important

This script is not a full penetration testing tool. It is a basic educational example of SSH client usage and random password generation.

Always use it only in environments where you have authorization to test access control behavior.
