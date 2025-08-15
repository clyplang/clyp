
## Code Style
- Follow Black code formatting
- Use isort for import sorting
- Follow PEP 8 naming conventions:
  - snake_case for functions and variables
  - PascalCase for classes
  - UPPER_CASE for constants
- Maximum line length of 88 characters (Black default)
- Use absolute imports over relative imports

## Type Hints
- Use type hints for all function parameters and returns
- Import types from `typing` module
- Use `Optional[Type]` instead of `Type | None`
- Use `TypeVar` for generic types
- Define custom types in `types.py`
- Use `Protocol` for duck typing

## Testing
- Use pytest for testing
- Write tests for all routes
- Use pytest-cov for coverage
- Implement proper fixtures
- Use proper mocking with pytest-mock
- Test all error scenarios
- Use uv run -m pytest to run tests

## Error Codes
Letter Group Codes:
| Code | Category                       | Notes                                               |
| ---- | ------------------------------ | --------------------------------------------------- |
| A    | **Syntax Errors**              | Parsing, unexpected tokens, etc.                    |
| B    | **Lexical Errors**             | Illegal characters, tokenizing problems             |
| C    | **Type Errors**                | Mismatched types, invalid operations                |
| D    | **Runtime Errors**             | Null derefs, div by zero, etc.                      |
| E    | **Import/Module Errors**       | Missing or circular imports                         |
| F    | **File System Errors**         | Missing files, permission errors                    |
| G    | **IO Errors**                  | Stream read/write fails                             |
| H    | **Semantic Errors**            | Valid syntax, invalid logic                         |
| I    | **Deprecation Warnings**       | Use of deprecated features                          |
| J    | **Compiler Internal Errors**   | You screwed up your compiler                        |
| K    | **Standard Library Errors**    | Issues in bundled libs                              |
| L    | **Argument Errors**            | Too many/too few args                               |
| M    | **Scope Errors**               | Variable not found, etc.                            |
| N    | **Name Errors**                | Undefined functions or symbols                      |
| O    | **Optimization Warnings**      | Inefficient or redundant code                       |
| P    | **Permission Errors**          | User lacks access                                   |
| Q    | **Concurrency Errors**         | Thread deadlock, race conditions                    |
| R    | **Memory Errors**              | Leaks, allocation fails                             |
| S    | **Security Errors**            | Dangerous patterns, injections                      |
| T    | **Transform Errors**           | Clyp-to-Python transpilation errors                 |
| U    | **Versioning Errors**          | Mismatched versions or protocols                    |
| V    | **Validation Errors**          | Invalid user input or data                          |
| W    | **Warning-Level Notices**      | Non-fatal, but still odd                            |
| X    | **Experimental Feature Fails** | Stuff that's not stable yet                         |
| Y    | **Language Feature Errors**    | Misuse of core features (e.g., `async` in sync ctx) |
| Z    | **Unknown/Unclassified**       | Catch-all, fallback category                        |

Numbering Scheme
| Range   | Use Case Example                          |
| ------- | ----------------------------------------- |
| 001–099 | **Critical** (usually crash or hard-stop) |
| 100–299 | **Common user mistakes**                  |
| 300–499 | **Advanced/edge-case errors**             |
| 500–699 | **Warnings and notices**                  |
| 700–899 | **Compiler/runtime only**                 |
| 900–999 | **Reserved for future/experimental**      |
