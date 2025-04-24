# VulnScanX - Automated Vulnerability Scanner

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-brightgreen)](https://www.python.org/dev/peps/pep-0008/)

A lightweight vulnerability scanner that identifies security issues and generates actionable reports for system administrators and developers.

## Features

- 🛡️ **Multi-Layer Scanning**:
  - Port scanning (Nmap integration)
  - CVE database lookups (NVD API)
  - Web vulnerability checks (SQLi/XSS templates)
  - Configuration audits (weak passwords, open permissions)
  
- 📊 **Smart Reporting**:
  - Risk-prioritized findings
  - HTML/PDF export
  - Plain-language remediation steps

- 🧩 **Modular Design**:
  - Easy to add new scan modules
  - Configurable scan profiles (quick/full)

## Installation

  ```bash
  git clone https://github.com/yourusername/vulnscanx.git
  cd vulnscanx
  pip install -r requirements.txt
  ```

## Usage

# Basic Scan
  ```bash
  python vulnscanx.py --target 192.168.1.1 --scan-type quick
  ```
# Full Scan with PDF Report
  ```bash
  python vulnscanx.py --target example.com --scan-type full --report pdf
  ```

## Configuration
**Edit config.yaml to:**
 - Set default scan options
 - Add NVD API key (for CVE lookups)
 - Customize report templates
```yaml
# config.yaml example
defaults:
  scan_type: quick
  report_format: html
nvd_api_key: "your_api_key_here"
```
## Supported Checks

| Category       | Examples                      |
|----------------|-------------------------------|
| Network        | Open ports, outdated services |
| Web            | SQLi, XSS, misconfigurations  |
| System         | Weak passwords, sudo rules    |
| CVEs           | NVD database lookups          |

## Contributing
1.  Fork the repository
2.  Add new plugins in /plugins
3.  Submit a PR with tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
MIT - See [MIT License](LICENSE)

## **Key Advantages**

1. **Real-World Utility**:
   - Unlike educational-only tools, this provides immediate value to sysadmins
   - Focuses on *actionable* results with remediation steps

2. **Learning Opportunities**:
   - Network scanning (Nmap)
   - API integration (NVD database)
   - Secure coding practices
   - Report generation (Jinja2/PDF)

3. **Professional Presentation**:
   - GitHub badges
   - Clear sample output
   - Modular architecture

4. **Extensible**:
   - Easy to add new scanners (create a new plugin file)
   - Supports custom report templates
