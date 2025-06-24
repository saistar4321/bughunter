# 🐞 BugHunter: Advanced Bug Bounty Recon Automation Tool

**BugHunter** is a powerful and modular automation toolkit built with Python and Bash for ethical hackers and bug bounty hunters. It helps automate time-consuming reconnaissance tasks and vulnerability checks — saving you time and letting you focus on exploitation.

---

## 🚀 What It Does

BugHunter performs deep automated recon and vulnerability scanning on any target domain or application. It can:

- Enumerate subdomains
- Detect subdomain takeover vulnerabilities
- Extract secrets and endpoints from JavaScript files
- Detect SSRF, IDOR, HPP, and XSS vectors
- Scan for exposed APIs and CVEs
- Capture screenshots of all active endpoints
- Generate PDF/HTML reports summarizing all findings
- Run modules individually or as a full recon pipeline

---

## 🧱 Folder Structure

```

bughunter/
├── run.sh                      # Full recon launcher
├── cli.py                     # CLI interface to run individual modules
├── requirements.txt           # Python dependencies
├── LICENSE
├── README.md
├── core/                      # Python modules (scanners)
│   ├── subdomain\_enum.py
│   ├── subdomain\_takeover.py
│   ├── js\_endpoint\_scanner.py
│   ├── ssrf\_scanner.py
│   ├── idor\_fuzzer.py
│   ├── cors\_checker.py
│   ├── cve\_scanner.py
│   ├── hpp\_detector.py
│   ├── sensitive\_header\_scanner.py
│   ├── xss\_redirect\_detector.py
│   ├── auth\_bypass\_2fa.py
│   └── screenshot\_capture.py
├── screenshots/               # PNG captures of each endpoint
└── reports/                   # Auto-generated HTML and PDF reports

````

---

## 🛠️ Installation

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/bughunter.git
cd bughunter
````

### 📦 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 🔨 3. Install External Tools

Make sure these are installed on your system:

| Tool          | Purpose                     | Install Command                                                            |
| ------------- | --------------------------- | -------------------------------------------------------------------------- |
| `subfinder`   | Subdomain enumeration       | `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| `httpx`       | Live subdomain detection    | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest`            |
| `nuclei`      | Vulnerability scanning      | `go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest`       |
| `amass`       | Deep subdomain enumeration  | `sudo apt install amass`                                                   |
| `jq`          | JSON parsing                | `sudo apt install jq`                                                      |
| `chromium`    | Screenshot automation       | `sudo apt install chromium-browser`                                        |
| `wkhtmltopdf` | Convert HTML reports to PDF | `sudo apt install wkhtmltopdf`                                             |

✅ Ensure `$GOPATH/bin` is in your `PATH` if using `go install`.

---

## ⚙️ Usage

### ✅ Run Full Recon Automation

```bash
./run.sh example.com
```

### 🧪 Run Individual Module

```bash
python3 cli.py --target example.com --module subdomain_takeover
```

Available modules:

```
subdomain_enum
subdomain_takeover
js_endpoint_scanner
ssrf_scanner
idor_fuzzer
cors_checker
cve_scanner
hpp_detector
sensitive_header_scanner
xss_redirect_detector
auth_bypass_2fa
screenshot_capture
```

---

## 📂 Output

* 🧾 `reports/` folder contains structured HTML/PDF reports of findings
* 📸 `screenshots/` includes images of live hosts
* 💡 Each finding includes severity levels (P1–P4)

---

## ⚠️ Known Limitations

* False positives may occur (especially in SSRF, IDOR fuzzing)
* Does not yet support multi-threaded async scanning
* Javascript parsing relies on regex (limited support for obfuscated JS)
* Tool does not exploit vulnerabilities — it only detects and reports
* Subdomain takeover module uses passive DNS; no DNS poisoning
* Reports may miss context if web app is heavily JS-based

---

## ✨ Planned Features

* GitHub Actions CI integration
* Burp Suite plugin for report import
* Multi-scope scanning (from wordlists)
* Cloud service scanner (e.g., S3 buckets, Firebase DBs)

---

## 📖 License

This project is under the [MIT License](LICENSE).

---

## 🙌 Contribute

Pull requests and issues are welcome!

---

## 💬 Contact

Feel free to reach out via GitHub Issues or Discussions tab.

Happy hacking! ⚔️
