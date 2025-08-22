
# Python AWS Backup CLI

A simple, production-ready Python script to compress a directory and upload the archive to **AWS S3**.  
Includes unit tests (pytest) and CI automation with **GitHub Actions**.

## Features
- Compress any folder into a timestamped **.zip** (default) or **.tar.gz**
- Upload the archive to **Amazon S3**
- Simple CLI interface with sensible defaults
- Unit tests with **pytest**
- **GitHub Actions** workflow to run tests on every push/PR

---

## Quickstart

### 1) Clone & set up
```bash
git clone https://github.com/your-username/python-aws-backup-cli.git
cd python-aws-backup-cli
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure AWS credentials (one-time)
Use the AWS CLI or environment variables.

```bash
# Option A: AWS CLI (recommended)
aws configure
# Provide AWS Access Key ID, Secret Access Key, region, output format
```

Alternatively set env vars before running:
```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=ap-south-1
```

### 3) Run a local backup (no upload)
```bash
python backup.py --source ./my_data --outdir ./backups --format zip
```

### 4) Backup and upload to S3
```bash
python backup_and_s3.py --source ./my_data --outdir ./backups --format zip --bucket your-bucket-name --prefix optional/folder/path/
```

- `--bucket` is your S3 bucket name.
- `--prefix` is optional (folder path inside the bucket).
- Result example: `s3://your-bucket-name/optional/folder/path/backup_my_data_20250101_123000.zip`

---

## Project Structure
```
python-aws-backup-cli/
├─ backup.py                # create compressed backups (zip/tar.gz)
├─ s3_upload.py             # upload helper for S3
├─ backup_and_s3.py         # one-shot: create backup + upload
├─ requirements.txt
├─ .gitignore
├─ README.md
├─ tests/
│  └─ test_backup.py
└─ .github/
   └─ workflows/
      └─ python-tests.yml   # CI: run pytest on push/PR
```

---

## Examples

Create a **.zip** archive:
```bash
python backup.py -s ./my_data -o ./backups -f zip
```

Create a **.tar.gz** archive:
```bash
python backup.py -s ./my_data -o ./backups -f tar
```

Backup and **upload to S3** with a prefix:
```bash
python backup_and_s3.py -s ./my_data -o ./backups -f zip --bucket my-bucket --prefix daily/ahad/
```

---

## Notes
- Windows users: prefer absolute paths or use `./my_data` relative to the project root.
- Make sure your AWS IAM user/role has `s3:PutObject` permission for your bucket (and `s3:ListBucket` if needed).
- Large directories: consider excluding patterns (future enhancement).

---

## License
MIT
