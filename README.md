# Status Buster

## 🔥 Overview
**Status Buster** is a high-speed, multi-threaded **HTTP status code checker** designed for penetration testers, OSINT researchers, and web security analysts. This tool allows you to quickly analyze the status of multiple URLs, helping identify live, redirected, or inaccessible web resources.

## 🚀 Features
- **Multi-threaded scanning** – Uses multiprocessing to speed up URL checking.
- **Supports HTTP & HTTPS** – Detects status codes for both `80` and `443` ports.
- **Custom User-Agent Rotation** – Uses randomized user-agents from a file (`ua.txt`) to avoid detection.
- **Automatic Logging** – Saves successful and error responses into structured logs.
- **Timeout Handling** – Fast response detection with a configurable timeout.

## 📌 Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Alecto-Fsociety/status_buster.git
cd status_buster
pip install -r requirements.txt  # Install dependencies if required
```

## 🔧 Usage
### **Basic Usage**
Run the script with a list of URLs:

```bash
python3 status_buster.py -ul urls.txt
```

### **Options**
| Option  | Description |
|---------|------------|
| `-ul` `<file>` | Path to the URL list (required) |
| `-t` `<int>` | Number of threads to use (default: 4) |

### **Example**
```bash
python3 status_buster.py -ul urls.txt -t 10
```
This will check the URLs in `urls.txt` using 10 concurrent threads.

## 👤 Output Logs
- **Checked URLs:** Stored in `checked_url/`
- **Errors & Exceptions:** Stored in `err_logs/`
- **Successful URLs:** Logged with timestamps for easy tracking.

## 💡 How It Works
1. Reads the URL list from the given file.
2. Establishes a socket connection (HTTPS/SSL or HTTP).
3. Sends a `GET` request with a randomized User-Agent.
4. Parses the response headers to extract HTTP status codes.
5. Saves results in structured logs.

## 🔥 Why Use Status Buster?
- **Fast & Efficient:** Multi-threaded execution for rapid URL status checking.
- **Customizable:** Modify the User-Agent file (`ua.txt`) to mimic different clients.
- **Security-Oriented:** Useful for reconnaissance, OSINT, and pentesting tasks.
- **Error Handling:** Automatically logs unreachable URLs for further analysis.

## 🐝 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests and feature suggestions are welcome! Feel free to open an issue if you find any bugs.

## 🛠️ Author
Developed by **Alecto-Fsociety**  
🔗 **GitHub:** [Alecto-Fsociety](https://github.com/Alecto-Fsociety)
