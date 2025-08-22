
from pathlib import Path
from backup import create_backup
from s3_upload import upload_to_s3
import argparse

def main():
    p = argparse.ArgumentParser(description="Create backup and upload to S3")
    p.add_argument("-s","--source", default="my_data", help="Folder to back up")
    p.add_argument("-o","--outdir", default="backups", help="Where to store backups")
    p.add_argument("-f","--format", choices=["zip","tar"], default="zip", help="Archive format")
    p.add_argument("--bucket", required=True, help="S3 bucket name")
    p.add_argument("--prefix", default="", help="Optional S3 key prefix (folder path in bucket)")
    args = p.parse_args()

    src = Path(args.source).expanduser().resolve()
    out = Path(args.outdir).expanduser().resolve()

    archive = create_backup(src, out, args.format)

    # Construct object key
    prefix = args.prefix.strip("/")
    key = f"{prefix}/{archive.name}" if prefix else archive.name

    upload_to_s3(archive, args.bucket, key)

if __name__ == "__main__":
    main()
