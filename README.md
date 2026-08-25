# 🪙 Crypto & Fiat Currency Converter CLI

A clean, light-weight Python Command Line Interface (CLI) application that fetches live prices for **Bitcoin**, **Ethereum**, and **Cardano** using the **CoinGecko API** and converts user-specified quantities into **USD** and **PKR**.

---

## 🛠️ Features

- **Real-Time Data:** Fetches live market prices directly via REST API.
- **Dual Fiat Currency:** Supports both USD ($) and PKR (Rs) conversions.
- **Error Protection:** Built-in try-except blocks to gracefully handle network issues.
- **Interactive Menu Loop:** Simple terminal-based choice menu with clean number formatting.

---

## 📦 Requirements & Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/FarazAliID/crypto-currency-converter-cli.git
   cd crypto-currency-converter-cli
   pip install -r requirements.txt
   python main.py

   ==== SAMPLE OUTPUT ====
   === Crypto & Fiat Currency Converter CLI ===
1. Bitcoin USD & PKR Converter
2. Ethereum USD & PKR Converter
3. Cardano USD & PKR Converter
4. Exit

Select The Option Between (1 & 4) : 1
Put Your Coins To Calculate Bitcoin Currency In USD & PKR: 0.5

Coin Price USD is 62500.0 X User 0.5 == $31,250.00
Coin Price PKR is 17400000.0 X User 0.5 == Rs 8,700,000.00

=== Crypto & Fiat Currency Converter CLI ===
1. Bitcoin USD & PKR Converter
2. Ethereum USD & PKR Converter
3. Cardano USD & PKR Converter
4. Exit

Select The Option Between (1 & 4) : 4
Thank you for using Crypto Converter!
