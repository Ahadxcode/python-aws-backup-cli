# 🗄️ Python AWS Backup CLI  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![GitHub Actions](https://github.com/Ahadxcode/python-aws-backup-cli/actions/workflows/python-tests.yml/badge.svg)  


A simple yet powerful **Python CLI tool** that compresses local directories and uploads them securely to **AWS S3**.  
Built with **automation + DevOps best practices** (Pytest, GitHub Actions, modular Python).  

---

## 🚀 Features  
- 📦 Compress and back up files/directories into `.tar.gz`.  
- ☁️ Upload backups automatically to **AWS S3**.  
- 🧪 Includes **unit tests** (`pytest`) for reliability.  
- ⚡ **GitHub Actions** workflow to run tests on every push.  
- 🛠️ Modular design (`backup.py`, `s3_upload.py`, etc.).  

---
## 📂 Project Structure  

python-aws-backup-cli/
│── backup.py # Handles local compression
│── s3_upload.py # Handles AWS S3 upload
│── backup_and_s3.py # Combined CLI script
│── requirements.txt # Python dependencies
│── tests/ # Unit tests (pytest)
│── .github/workflows/ # CI/CD (GitHub Actions)
│── README.md # Project documentation
