# ⚡ EMap — Experimental Multithreaded IP Scanner

<p align="center">
  <b>A lightweight, ZMap-inspired network scanner built for flexibility and constrained environments.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg">
  <img src="https://img.shields.io/badge/status-experimental-orange.svg">
  <img src="https://img.shields.io/badge/license-educational-lightgrey.svg">
</p>

---

## 🧠 Overview

**EMap** is a Python-based scanner inspired by high-speed tools like ZMap, designed for:

- Systems where high-performance scanners crash or fail  
- Learning how network scanning works internally  
- Lightweight, customizable scanning workflows  

---

## 🚀 Features

✨ **Random IP Scanning**  
- Generates random IPv4 addresses on the fly  

🧵 **Multithreading**  
- Adjustable thread count for speed vs stability  

🌐 **Port Detection**  
- Scans for open TCP ports  

🖥️ **Web Server Discovery**
- Attempts HTTPS connections  
- Extracts page titles (if available)  

🔄 **User-Agent Rotation**
- Helps avoid basic detection  

📁 **Multiple Output Files**
- Organized results for later use  

---

## 📦 Requirements

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

---

## 🛠️ Usage

```bash
python emap.py [PORT] [THREADS] [OUTPUT_FILE] [AMOUNT]
```

### 📌 Arguments

| Argument        | Description |
|----------------|------------|
| `PORT`         | Port to scan (e.g. 80, 443) |
| `THREADS`      | Number of threads *(default: 50)* |
| `OUTPUT_FILE`  | File to store discovered IPs |
| `AMOUNT`       | Number of IPs to find |

---

### 💻 Example

```bash
python emap.py 443 100 results.txt 500
```

---

## 📁 Output Files

| File | Description |
|------|------------|
| `list.txt` | Discovered IPs |
| `site.txt` | IPs with active web servers |
| `output_with_title.txt` | Sites with page titles |
| `dns.txt` | Reverse DNS results |
| `dns_title.txt` | DNS hosts with titles |

---

## ⚠️ Known Limitations

- Not a full replacement for ZMap  
- No blacklist filtering (yet)  
- Threading is not fully optimized  
- May produce false positives  
- HTTPS validation may fail on some hosts  

---

## 🔮 Planned Features

- 🚫 Deep blacklist filtering (CIDR, reserved IP ranges)  
- ⚡ Performance improvements  
- 🧩 Modular scanning system  
- 📊 JSON / CSV output support  
- 🛡️ Better error handling  

---

## ⚠️ Legal Disclaimer

> 🚨 **IMPORTANT**

This tool is for:

- Educational purposes  
- Authorized penetration testing ONLY  

**DO NOT scan networks without permission.**

Unauthorized use may:
- Violate laws  
- Result in ISP bans  
- Lead to legal consequences  

---

## 👤 Author

```
Eyezik  
github.com/00xZ
```

---

## 💡 Inspiration

- ZMap — high-speed internet scanner  

---

## ⭐ Contributing

Pull requests, improvements, and ideas are welcome.

---

## 🧪 Status

> ⚠️ Experimental — expect bugs, crashes, and unfinished features  

---

<p align="center">
  <b>Built for learning. Use responsibly.</b>
</p>
