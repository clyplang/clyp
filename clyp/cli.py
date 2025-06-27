import argparse
from clyp import __version__
import sys
from clyp.transpiler import parse_clyp
import os
import traceback

def main():
    parser = argparse.ArgumentParser(description="Clyp CLI tool.")
    parser.add_argument('file', nargs='?', type=str, help="Path to the Clyp file to execute.")
    parser.add_argument('--version', action='store_true', help="Display the version of Clyp.")
    
    args = parser.parse_args()

    def get_clyp_line_for_py(py_line, line_map, clyp_lines):
        if not line_map or not clyp_lines:
            return '?', ''
        # Find the closest previous mapped line
        mapped_lines = sorted(line_map.keys())
        prev = None
        for ml in mapped_lines:
            if ml > py_line:
                break
            prev = ml
        if prev is not None:
            clyp_line = line_map[prev]
            if 0 <= clyp_line-1 < len(clyp_lines):
                return clyp_line, clyp_lines[clyp_line-1]
            elif clyp_lines:
                return len(clyp_lines), clyp_lines[-1]
        return '?', ''

    if args.version:
        print(f"{__version__}")
    elif args.file:
        try:
            file_path = os.path.abspath(args.file)
            with open(file_path, 'r', encoding='utf-8') as f:
                clyp_code = f.read()
        except (IOError, UnicodeDecodeError) as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print(f"File {args.file} not found.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
        try:
            result = parse_clyp(clyp_code, file_path, return_line_map=True)
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)
            sys.exit(1)
        if isinstance(result, tuple):
            python_code, line_map, clyp_lines = result
        else:
            python_code = result
            line_map = None
            clyp_lines = None
        try:
            exec(python_code, {'__name__': '__main__', '__file__': file_path})
        except SyntaxError as e:
            py_line = e.lineno
            print("\nTraceback (most recent call last):", file=sys.stderr)
            clyp_line, code = get_clyp_line_for_py(py_line, line_map, clyp_lines)
            print(f"  File '{args.file}', line {clyp_line}", file=sys.stderr)
            print(f"    {code}", file=sys.stderr)
            print(f"(Python error at transpiled line {py_line})", file=sys.stderr)
            print(f"{type(e).__name__}: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            print("\nTraceback (most recent call last):", file=sys.stderr)
            for frame in tb:
                if frame.filename == '<string>':
                    py_line = frame.lineno
                    clyp_line, code = get_clyp_line_for_py(py_line, line_map, clyp_lines)
                    print(f"  File '{args.file}', line {clyp_line}", file=sys.stderr)
                    print(f"    {code}", file=sys.stderr)
                else:
                    print(f"  File '{frame.filename}', line {frame.lineno}", file=sys.stderr)
                    print(f"    {frame.line}", file=sys.stderr)
            print(f"{type(e).__name__}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"clyp version {__version__}, Python version {sys.version}")

if __name__ == "__main__":
    main()
