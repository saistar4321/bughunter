# 🐞 BugHunter - Advanced Bug Bounty Recon Automation Tool

BugHunter is a modular automation framework for security researchers and bug bounty hunters. It combines powerful Bash + Python scripts to uncover deep application vulnerabilities with minimal effort.

## ✨ Features

- 🌐 **Subdomain Enumeration**
- 🛰 **Subdomain Takeover Detection**
- 🧠 **JavaScript Endpoint & Function Discovery**
- 🧪 **SSRF Scanner**
- 🔓 **IDOR (Insecure Direct Object Reference) Brute-forcer**
- ⚠️ **CORS Misconfiguration Checker**
- 🦠 **CVE Scanner for JavaScript Libraries**
- 💉 **HTTP Parameter Pollution Detector**
- 🧾 **CRLF Injection & Log Poisoning**
- 🔍 **Sensitive Headers & Token Leaks Scanner**
- 📸 **Screenshot Capture + HTML/PDF Reports**
- 🔐 **2FA & Authorization Bypass Scanner**

---

## 🚀 Usage

### 🔧 Quick Start

```bash
git clone https://github.com/saistar4321/bughunter.git
cd bughunter
chmod +x run.sh
pip install -r requirements.txt

📚 Requirements :
pip install -r requirements.txt

You’ll also need common tools:

nuclei, httpx, subfinder, amass, chromium (for screenshots)

wkhtmltopdf or weasyprint for PDF reports


Full Recon on a Target
./run.sh example.com

 Run Individual Module
python3 cli.py --target example.com --module subdomain_takeover


Project Structure
bughunter/
├── run.sh                      # Main launcher
├── cli.py                     # CLI tool controller
├── core/                      # Individual scanner modules
│   ├── subdomain_takeover.py
│   ├── ssrf_scanner.py
│   ├── cors_check.py
│   ├── idor_fuzzer.py
│   ├── cve_scanner.py
│   ├── hpp_scanner.py
│   ├── js_endpoint_scanner.py
│   ├── sensitive_header_scanner.py
│   ├── xss_open_redirect.py
│   └── auth_bypass_scanner.py
├── screenshots/               # Captured screenshots
├── reports/                   # Auto-generated PDF/HTML reports
└── requirements.txt
