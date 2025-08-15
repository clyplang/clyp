__all__ = [
    "write_file", "read_file", "file_exists", "remove_file", "make_dir", "remove_dir",
    "list_dir", "list_files", "is_file", "is_dir", "remove", "rename", "copy", "move", "mkdir"
]

import os
import shutil

def write_file(path: str, content: str) -> None:
    """Write content to a file at the given path."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def read_file(path: str) -> str:
    """Read content from a file at the given path."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def file_exists(path: str) -> bool:
    """Check if a file exists at the given path."""
    return os.path.isfile(path)

def remove_file(path: str) -> None:
    """Remove a file at the given path."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No such file: '{path}'")
    os.remove(path)

def make_dir(path: str) -> None:
    """Create a directory at the given path."""
    os.makedirs(path, exist_ok=False)

def remove_dir(path: str) -> None:
    """Remove a directory at the given path."""
    if not os.path.isdir(path):
        raise FileNotFoundError(f"No such directory: '{path}'")
    shutil.rmtree(path)

def list_dir(path: str) -> list[str]:
    """List all entries (files and directories) in the given directory."""
    return os.listdir(path)

def list_files(path: str) -> list[str]:
    """List all files in the given directory."""
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def is_file(path: str) -> bool:
    """Check if the given path is a file."""
    return os.path.isfile(path)

def is_dir(path: str) -> bool:
    """Check if the given path is a directory."""
    return os.path.isdir(path)

def remove(path: str) -> None:
    """Remove a file or directory at the given path."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    if is_file(path):
        os.remove(path)
    elif is_dir(path):
        shutil.rmtree(path)
    else:
        raise ValueError(f"Path is neither a file nor a directory: '{path}'")

def rename(source: str, destination: str) -> None:
    """Rename a file or directory."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"No such file or directory: '{source}'")
    os.rename(source, destination)

def copy(source: str, destination: str) -> None:
    """Copy a file or directory from source to destination."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"No such file or directory: '{source}'")
    if is_file(source):
        shutil.copy2(source, destination)
    elif is_dir(source):
        shutil.copytree(source, destination)
    else:
        raise ValueError(f"Source is neither a file nor a directory: '{source}'")

def move(source: str, destination: str) -> None:
    """Move a file or directory from source to destination."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"No such file or directory: '{source}'")
    shutil.move(source, destination)

def mkdir(path: str) -> None:
    """Create a new directory at the given path."""
    if os.path.exists(path):
        raise FileExistsError(f"Directory already exists: '{path}'")
    os.makedirs(path)

__all__ = [
    "write_file", "read_file", "file_exists", "remove_file", "make_dir", "remove_dir",
    "list_dir", "list_files", "is_file", "is_dir", "remove", "rename", "copy", "move", "mkdir"
]
