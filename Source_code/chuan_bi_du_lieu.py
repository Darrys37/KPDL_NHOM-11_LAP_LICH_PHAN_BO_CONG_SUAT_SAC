"""Giải nén dữ liệu đi kèm, không cần khóa API."""
from pathlib import Path
import shutil
import zipfile

def main():
    source_dir = Path(__file__).resolve().parent
    archive = source_dir.parent / "data" / "caltech_merged_15min.csv.zip"
    target = source_dir / "caltech_merged_15min.csv"
    with zipfile.ZipFile(archive) as z:
        entry = z.getinfo("caltech_merged_15min.csv")
        if target.exists():
            raise SystemExit("CSV đã tồn tại. Giữ nguyên file; có thể chạy notebook.")
        temporary = target.with_suffix(".csv.part")
        try:
            with z.open(entry) as src, temporary.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            if temporary.stat().st_size != entry.file_size:
                raise RuntimeError("Dung lượng CSV giải nén không khớp.")
            temporary.rename(target)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    print("Đã giải nén:", target)

if __name__ == "__main__":
    main()
