# Encrypted Chat App

## Description
A secure real-time client-server chat application built using Python. It uses AES encryption to secure messages before sending them over TCP socket communication.

## Features
- AES encrypted messaging
- Client-server architecture using TCP sockets
- Multi-client support using threading
- Real-time chat system
- Pre-shared secret key encryption
- Safe IV (Initialization Vector) usage
- Message logging with timestamps

## Technologies Used
- Python
- Socket Programming (TCP)
- Threading
- Cryptography (AES Encryption)
- Datetime
- OS Module

## How to Run

1. Install dependencies:
pip install cryptography

2. Start server:
python server.py

3. Start client (open multiple terminals):
python client.py