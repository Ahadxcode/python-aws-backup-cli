
import boto3
from pathlib import Path

def upload_to_s3(file_path: Path, bucket: str, key: str | None = None):
    """Upload a file to S3. Requires AWS credentials to be configured in env or AWS CLI."""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    s3 = boto3.client("s3")
    key = key or file_path.name
    s3.upload_file(str(file_path), bucket, key)
    print(f"☁️ Uploaded to s3://{bucket}/{key}")
