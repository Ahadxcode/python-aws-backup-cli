
from pathlib import Path
from backup import create_backup

def test_backup_creates_zip(tmp_path: Path):
    # Arrange: create dummy data
    src = tmp_path / "data"
    src.mkdir()
    (src / "a.txt").write_text("hello")
    out = tmp_path / "out"

    # Act
    archive = create_backup(src, out, "zip")

    # Assert
    assert archive.exists()
    assert archive.suffix == ".zip"

def test_backup_creates_tar(tmp_path: Path):
    src = tmp_path / "data"
    src.mkdir()
    (src / "a.txt").write_text("hello")
    out = tmp_path / "out"

    archive = create_backup(src, out, "tar")
    assert archive.exists()
    assert archive.name.endswith(".tar.gz")
