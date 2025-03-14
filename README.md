# 🚀 Status Buster

```
███████╗████████╗ █████╗ ███████╗██╗   ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗
███████╗   ██║   ███████║███████╗██║   ██║█████╗  ██████╔╝
╚════██║   ██║   ██╔══██║╚════██║██║   ██║██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████║╚██████╔╝███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

## 🌍 Overview

Status Buster is a Python-based tool designed to check the HTTP response status of multiple URLs. It helps identify accessible and restricted web pages, making it useful for **web monitoring, penetration testing, and security research**.

Unlike [**Payload Checkers**](https://github.com/Alecto-Fsociety/Payload_Checkers) 🔥, which focuses on **testing vulnerabilities such as XSS and SQL injection**, Status Buster is primarily used for **scanning URLs for accessibility and status code responses**.

## ✨ Features

- ⚡ **Multi-threading support** for faster scanning.
- 🌐 **HTTP/HTTPS compatibility**.
- 📝 **Saves results** to a log file.
- 🎭 **Customizable user-agent** for stealth scanning.
- 📂 **Supports URL lists** for bulk testing.
- 🚀 **No external dependencies required** (pure Python implementation).

## 📌 Installation

No installation is required. Status Buster runs as a standalone script.

## 🛠️ Usage

### ▶️ Basic Usage:

Run the script with a single URL:

```bash
python status_buster.py -u https://example.com
```

### 📑 Scan multiple URLs from a file:

```bash
python status_buster.py -f urls.txt
```

### 🎭 Customize the User-Agent:

```bash
python status_buster.py -u https://example.com -a "Mozilla/5.0 (compatible; StatusBuster)"
```

### 💾 Save results to a file:

```bash
python status_buster.py -u https://example.com -o results.log
```

## 📊 Example Output:

```
[200] https://example.com
[403] https://example.com/admin
[404] https://example.com/nonexistent
```

## 🔍 Difference from Payload Checkers

| Feature       | Status Buster 🚀                               | [Payload Checkers](https://github.com/Alecto-Fsociety/Payload_Checkers) 🔥 |
| ------------- | ---------------------------------------------- | ----------------------------------------------------------------------- |
| Purpose       | URL status scanning 🖥️                         | Security vulnerability testing 🛡️                                      |
| Functionality | Checks HTTP status codes (200, 403, 404, etc.) | Injects payloads to test XSS, SQLi, etc.                               |
| Input         | URLs (single or list)                          | URLs + payloads                                                         |
| Output        | Status logs 📜                                  | Vulnerability detection results 🛠️                                      |

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**. Unauthorized use on systems without explicit permission is strictly prohibited and may be illegal. **Use at your own risk.** ❗

## 🤝 Contributing

Feel free to **submit issues, feature requests, or pull requests** to improve Status Buster. Contributions are always welcome! ✨

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/Alecto-Fsociety/Alecto-Fsociety/blob/main/LICENSE) file for details.

## 👨‍💻 Author

Developed by [Alecto-Fsociety](https://github.com/Alecto-Fsociety). 🚀

