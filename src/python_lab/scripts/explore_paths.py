import datetime
from pathlib import Path
from python_lab.aggregates import group_by
from python_lab.models import FileReport

def project_root(marker: str = "pyproject.toml") -> Path:
    """Walk up from this file until the directory containing `marker` is found and return a Path."""
    for directory in Path(__file__).resolve().parents:
        if (directory / marker).exists():
            return directory
    raise FileNotFoundError(f"No {marker} in any parent of {__file__}")

def report_file(file: Path) -> FileReport:
    """return file information"""
    stat = file.stat()
    return {'name': file.name,
            'stem': file.stem,
            'suffix': file.suffix,
            'size_kb': round(stat.st_size / 1024, 1),
            'modified': datetime.datetime.fromtimestamp(stat.st_mtime).date().isoformat()
            }

def find_by_extension(folder: Path, ext: str) -> list[Path]:
    """return a list of file paths that match the extension"""
    suffix = ext if ext.startswith('.') else f'.{ext}'
    return sorted(p for p in folder.rglob(f'*{suffix}') if p.is_file())

def total_size(folder: Path) -> float:
    """return the total size of the files in the folder"""
    return round(sum(x.stat().st_size for x in folder.rglob('*') if x.is_file()) / 1024**2, 2)

def group_files_by_extension(folder: Path) -> dict[str, list[Path]]:
    """return a dictionary of file paths grouped by extension"""
    return group_by([x for x in folder.rglob('*') if x.is_file()], key = lambda x: x.suffix.lower())

def largest_files(folder: Path, n: int = 5 ) -> list[Path]:
    """return a list of largest file paths"""
    files = [x for x in folder.rglob('*') if x.is_file()]
    return sorted(files, key = lambda x: x.stat().st_size, reverse = True)[:n]

def safe_target(path: Path) -> Path:
    """return a file path that does not exist"""
    safe_path = path
    counter = 1
    while safe_path.exists():
        safe_path = path.with_stem(f'{path.stem}_{counter}')
        counter += 1
    return safe_path

if __name__ == '__main__':
    print(project_root())
    print(report_file(Path(__file__)))
    print(find_by_extension(project_root() / 'src' / 'python_lab', ext='.py'))
    print(total_size(project_root() / 'src' / 'python_lab'))
    print(group_files_by_extension(project_root() / 'src' / 'python_lab'))
    print(largest_files(project_root() / 'src' / 'python_lab', 5))
    print(safe_target(Path('C:/dev/python-lab/src/python_lab/aggregates.py')))