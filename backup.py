
from pathlib import Path
from datetime import datetime
import argparse, zipfile, tarfile, sys

def create_backup(source: Path, outdir: Path, fmt: str = "zip") -> Path:
    """Create a compressed archive of `source` inside `outdir`.
    fmt: 'zip' or 'tar' (tar -> .tar.gz)
    Returns the path to the created archive.
    """
    source = Path(source)
    outdir = Path(outdir)
    if not source.exists() or not source.is_dir():
        print(f"ERROR: Source folder not found: {source}")
        sys.exit(1)

    outdir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    if fmt == "zip":
        archive = outdir / f"backup_{source.name}_{ts}.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in source.rglob("*"):
                zf.write(path, arcname=path.relative_to(source))
    elif fmt == "tar":
        archive = outdir / f"backup_{source.name}_{ts}.tar.gz"
        with tarfile.open(archive, "w:gz") as tf:
            tf.add(source, arcname=source.name)
    else:
        print("ERROR: Unknown format. Use 'zip' or 'tar'.")
        sys.exit(2)

    print(f"✅ Backup created: {archive}")
    return archive

def main():
    p = argparse.ArgumentParser(description="Compress a directory into zip/tar.gz")
    p.add_argument("-s","--source", default="my_data", help="Folder to back up")
    p.add_argument("-o","--outdir", default="backups", help="Where to store backups")
    p.add_argument("-f","--format", choices=["zip","tar"], default="zip", help="Archive format")
    args = p.parse_args()

    src = Path(args.source).expanduser().resolve()
    out = Path(args.outdir).expanduser().resolve()
    create_backup(src, out, args.format)

if __name__ == "__main__":
    main()
