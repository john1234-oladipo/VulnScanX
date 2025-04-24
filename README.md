# VulnScanX - Automated Vulnerability Scanner

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-brightgreen)](https://www.python.org/dev/peps/pep-0008/)
![GUI](https://img.shields.io/badge/GUI-PyQt5-blueviolet)
[![CI/CD](https://github.com/yourusername/vulnscanx/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/vulnscanx/actions)

A lightweight vulnerability scanner that identifies security issues and generates actionable reports for system administrators and developers.

## What's New (v0.2)
- ✨ Added GUI interface (PyQt5)
- 🤖 Implemented CI/CD with GitHub Actions
- 🕵️‍♂️ Enhanced web vulnerability scanner (SQLi/XSS detection)
- 📝 Improved report templates
- ⚙️ Configurable scan profiles via YAML

## Features

### Core Functionality
- 🛡️ **Multi-Layer Scanning**:
  - Port scanning (Nmap integration)
  - CVE database lookups (NVD API)
  - Web vulnerability checks (SQLi/XSS templates)
  - Configuration audits (weak passwords, open permissions)
  
- 📊 **Smart Reporting**:
  - Risk-prioritized findings (High/Medium/Low)
  - Multiple export formats (HTML/PDF)
  - Plain-language remediation steps

### Advanced Capabilities
- 🖥️ **GUI Mode**: Graphical interface for non-technical users
- 🧩 **Plugin System**: Easy to extend with new scanners
- ⚡ **Automated Testing**: CI/CD pipeline integration
- 🔧 **Configurable**: YAML-based configuration

## Installation

```bash
git clone https://github.com/yourusername/vulnscanx.git
cd vulnscanx
# Core only (no GUI):
  pip install -r requirements.txt --ignore-installed

# With GUI support:
  pip install -r requirements.txt
```

## Usage

### Command Line Interface
```bash
# Basic scan
python vulnscanx.py --target 192.168.1.1 --scan-type quick

# Full scan with PDF report
python vulnscanx.py --target example.com --scan-type full --report pdf --output my_report.pdf
```

### Graphical Interface
```bash
python gui/app.py
```
![GUI Preview](samples/gui_preview.png) <!-- Add actual screenshot later -->

## Configuration

Edit `config.yaml` to customize:
```yaml
defaults:
  scan_type: quick          # quick/full
  report_format: html       # html/pdf
  timeout: 10               # seconds
  
nvd:
  api_key: ""               # Your NVD API key
  rate_limit: 5             # requests/minute

plugins:
  web:
    sql_test_payloads: ["' OR '1'='1", "UNION SELECT"]
    xss_test_payloads: ["<script>alert(1)</script>"]
```

## Supported Checks

| Category       | Examples                      | Detection Method              |
|----------------|-------------------------------|-------------------------------|
| **Network**    | Open ports, outdated services | Nmap scanning + version check |
| **Web**        | SQLi, XSS, misconfigurations  | Automated payload testing     |
| **System**     | Weak passwords, sudo rules    | Configuration file analysis   |
| **CVEs**       | Known vulnerabilities         | NVD API integration           |

## Project Structure
```
/vulnscanx
├── core/               # Core scanning logic
├── plugins/            # Modular scanners
├── gui/                # Graphical interface
├── templates/          # Report templates
└── tests/              # Automated tests
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Add tests for new functionality
4. Submit a Pull Request

See our [Contribution Guidelines](CONTRIBUTING.md) for details.

## License
This project is licensed under the [MIT License](LICENSE).

---

### Key Changes Made:
1. **Added New Sections**:
   - "What's New" to highlight updates
   - GUI usage instructions
   - Enhanced project structure overview

2. **Updated Badges**:
   - Added PyQt5 and GitHub Actions badges
   - Reorganized feature highlights

3. **Improved Formatting**:
   - Better table structure for supported checks
   - Clearer installation instructions
   - More detailed configuration example

4. **Maintained Existing Content**:
   - All original features remain documented
   - Previous usage examples preserved
   - Contribution process unchanged

5. **Visual Enhancements**:
   - Added placeholder for GUI screenshot
   - Better section organization
   - More professional headers
