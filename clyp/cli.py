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

    if args.version:
        print(f"{__version__}")
    elif args.file:
        try:
            file_path = os.path.abspath(args.file)
            with open(file_path, 'r', encoding='utf-8') as f:
                clyp_code = f.read()
            result = parse_clyp(clyp_code, file_path, return_line_map=True)
            if isinstance(result, tuple):
                python_code, line_map, clyp_lines = result
            else:
                python_code = result
                line_map = None
                clyp_lines = None
            try:
                exec(python_code, {'__name__': '__main__', '__file__': file_path})
            except Exception as e:
                tb = traceback.extract_tb(sys.exc_info()[2])
                print("\nTraceback (most recent call last):", file=sys.stderr)
                for frame in tb:
                    if frame.filename == '<string>':
                        py_line = frame.lineno
                        if line_map and py_line in line_map:
                            clyp_line = line_map[py_line]
                            code = clyp_lines[clyp_line-1] if clyp_lines and clyp_line-1 < len(clyp_lines) else ''
                            print(f"  File '{args.file}', line {clyp_line}", file=sys.stderr)
                            print(f"    {code}", file=sys.stderr)
                        else:
                            print(f"  File '{args.file}', line ?", file=sys.stderr)
                    else:
                        print(f"  File '{frame.filename}', line {frame.lineno}", file=sys.stderr)
                        print(f"    {frame.line}", file=sys.stderr)
                print(f"{type(e).__name__}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing file {args.file}: {e}\n\n Warning: These errors come from the transpiled Python code and will likely not provide helpful information.", file=sys.stderr)
    else:
        print(f"clyp version {__version__}, Python version {sys.version}")

if __name__ == "__main__":
    main()
