# 🧠 Offline Socket-Based Communication Prototype

> ⚡ A raw TCP-based communication system built from scratch — designed to simulate peer-to-peer messaging **without the internet**, using only core `socket` programming and system-level constructs.

---

## 🚀 Why It's Unique

Unlike most chat apps that rely on high-level APIs, cloud infra, or third-party messaging platforms, this project dives deep into **low-level networking** using pure Python sockets. It’s a bare-metal demo of two machines talking directly over a LAN — no servers, no web protocols, no frameworks.

It was also built as part of an **experimental attempt to understand how communication can be achieved using principles similar to ethical hacking**, reverse shells, and real-time command execution — but all in a **controlled, educational context**.

---

## 🛠️ Features

- Full-duplex communication using TCP sockets.
- Minimalistic sender–receiver architecture.
- Basic command-response interface (like primitive shells).
- Demonstrates concept of **manual message fragmentation and reassembly**.
- Handles broken messages and socket errors gracefully.

---

## 🧪 Use Cases (Experimental)

- Learning tool for socket communication.
- Exploring basic principles of remote shells and command execution.
- Foundation for future tools in peer-to-peer networking or secure comms.

---

## ⚠️ Disclaimer

This code is **for educational purposes only**. It was created to explore networking fundamentals, not for malicious use. It is not hardened, encrypted, or intended to run over the open internet.

Do not deploy this outside of a secure, local environment.

---

## 📂 Files

- `listener.py`: The server-side script, awaiting connections and sending/receiving messages.
- `backdoor.py`: The client-side script that connects to the server and handles commands.

---

## 🧠 Future Directions

- Add encryption with SSL/TLS sockets.
- Build GUI over the messaging layer.
- Extend to allow multiple clients using threading or async sockets.

---

## ✅ Built With

- Python 3
- `socket`
- `subprocess` (optional command execution)
- Localhost / LAN network

---

## 🔒 Security Reminder

Again — this is **not a backdoor**. It's a technical proof of concept designed to understand the flow of peer-to-peer communication. Use responsibly.

