# CID-GA

A small Python toolkit for generating SSH login attempts and NGINX request traffic simulation.

## Clone the repository

```bash
git clone https://github.com/Apil120/CID-GA.git
cd CID-GA
```

## Project Overview

This repository now supports two modes:

1. SSH login attempt simulation using `paramiko` and randomized passwords.
2. NGINX request simulation using `requests` and a range of traffic patterns.

> Note: This project is intended for educational and authorized testing only. Do not use it against systems or networks without explicit permission.

## Files

- `main.py` - CLI entrypoint that accepts user input, validates values, and launches SSH or NGINX log generation.
- `log_generator.py` - Contains `LogGenerator` with SSH and NGINX simulation logic.
- `utils.py` - Contains `RandomStringGenerator` and validation helpers.
- `requirements.txt` - Python dependencies required to run the project.

## Dependencies

The project depends on:

- `paramiko`
- `requests`

## Setup

### Windows

1. Install Python from https://www.python.org/downloads/ and enable the `python` command.
2. Open PowerShell and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

### macOS

1. Install Python using Homebrew or from python.org:

```bash
brew install python
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Linux

1. Install Python and pip using your package manager, for example on Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the repository directory:

```bash
python main.py
```

Then choose:

1. SSH log generation
2. NGINX request simulation

The script validates all input before attempting connections.

## Behavior

- SSH mode validates the host, username, attempt count, and mode.
- NGINX mode validates the target URL, request count, and request mode.
- The generator prints each attempt and includes burst traffic for DOS-style simulation.

## Important

Use this toolkit only in authorized environments. It is not intended for unauthorized penetration testing.
