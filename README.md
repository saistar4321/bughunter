# 🐞 bughunter

**An Advanced Bug Bounty Recon Automation Tool (Bash + Python)**  
Built for automation-loving hackers. Perform deep reconnaissance and vulnerability scanning with one command.

---

## 📌 Features

`bughunter` automates the entire bug bounty reconnaissance process and includes:

### 🔍 Core Modules

| Module                         | Description |
|-------------------------------|-------------|
| Subdomain Enumeration         | Uses `subfinder`, `amass`, and `assetfinder` |
| Subdomain Takeover Detection  | Detects dangling CNAMEs and unclaimed services |
| XSS Scanner                   | Checks for reflected/stored XSS in URLs |
| SSRF Detector                 | Tests parameters for SSRF vectors |
| IDOR Scanner                  | Brute-forces object IDs to find insecure access |
| CORS Misconfiguration Tester  | Detects overly permissive or wildcard CORS |
| CVE Scanner (JS Libraries)    | Finds vulnerable frontend libraries |
| CRLF Injection Detector       | Injects log poisoning / newline vectors |
| JS Function Scanner           | Extracts endpoints and secrets from JavaScript files |
| Sensitive Headers Detector    | Finds session/token leaks in headers or responses |
| HTTP Parameter Pollution      | Detects logic flaws via duplicate parameter injection |
| 2FA Bypass + JWT Abuse Tester | Identifies endpoints that allow 2FA bypass via JWT reuse |
| Screenshot + Reporting        | Captures vulnerable endpoints and generates PDF reports |

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/saistar4321/bughunter.git
cd bughunter
````

### 2. Install Dependencies

#### 🔹 Install Python Modules

```bash
pip install -r requirements.txt
```

#### 🔹 Install External Tools (Optional)

```bash
sudo apt install -y subfinder amass assetfinder nuclei gau httpx curl jq
```

For screenshots (optional):

```bash
sudo apt install chromium-driver
```

---

## 🚀 Usage

### 🔁 Run Full Recon

```bash
./run.sh example.com
```

This will execute all enabled modules sequentially and generate:

* Live endpoints
* Vulnerability results
* Screenshots
* PDF/HTML reports in `output/`

---

### ⚡ Run Individual Module

```bash
python3 modules/xss_scanner.py -u "https://target.com/search?q=test"
```

Or:

```bash
python3 modules/subdomain_takeover.py -d target.com
```

---

## 📁 Folder Structure

```
bughunter/
├── run.sh                      # Main automation script
├── requirements.txt            # Python dependencies
├── output/                     # Scan results + reports
├── modules/
│   ├── subdomain_enum.py
│   ├── subdomain_takeover.py
│   ├── xss_scanner.py
│   ├── ssrf_scanner.py
│   ├── idor_scanner.py
│   ├── cve_scanner.py
│   ├── crlf_injection.py
│   ├── js_function_scanner.py
│   ├── sensitive_header.py
│   ├── hpp_detector.py
│   ├── jwt_bypass_scanner.py
│   ├── screenshot_reporter.py
├── templates/                  # Nuclei or custom payloads
└── README.md
```

---

## ⚠️ Limitations

* No rate-limiting evasion is currently implemented.
* XSS scanner uses basic payloads.
* PDF report generation may not work on headless servers without Chromium.
* No Slack/webhook alerting (planned).

---

## 👨‍💻 Contributors

* [saistar4321](https://github.com/saistar4321) - Core development
* \[Monika Sharma, Mohsin Khan] - Vulnerability references and case studies

---

## 📄 License

[MIT](./LICENSE)

---

## 🧠 Bonus

✅ Inspired by real-world bugs:

* \$20K HackerOne cookie leak
* 2FA Bypass via premature JWT
* Parameter Pollution logic bypass
* GraphQL enumeration data leaks
* XSS via open redirect

---

Happy Hacking! ⚔️

