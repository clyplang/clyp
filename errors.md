## Error Codes
### Registered Errors:
| Code | Description                                                               |
| A100 | Syntax error                                                              |
| A101 | Python-style function definition detected                                 |
| C100 | Type error                                                                |
| D100 | Runtime error                                                             |
| D101 | Division by zero                                                          |
| E100 |                                                                          |
| F100 | File not found                                                            |
| F101 | OS error                                                                  |
| G100 | IO error                                                                  |
| H100 | Assertion error (semantic)                                                |
| I100 | Deprecation warning                                                       |
| J100 | Not implemented error (internal)                                          |
| L100 | Do not define 'self' argument in class methods; it is added automatically |
| M100 | Attribute error                                                           |
| M101 | Key error                                                                 |
| N100 | Name error                                                                |
| P100 | Permission error                                                          |
| Q100 | Timeout error                                                             |
| R100 | Memory error                                                              |
| U500 | Major version mismatch                                                    |
| U501 | Minor version mismatch                                                    |
| U502 | Patch version mismatch                                                    |
| V100 | Validation error                                                          |
| W501 | Deprecated syntax 'repeat [times] times'                                  |
| Z999 | Unknown/unclassified error                                                |

### Letter Group Codes:
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

### Numbering Scheme
| Range   | Use Case Example                          |
| ------- | ----------------------------------------- |
| 001–099 | **Critical** (usually crash or hard-stop) |
| 100–299 | **Common user mistakes**                  |
| 300–499 | **Advanced/edge-case errors**             |
| 500–699 | **Warnings and notices**                  |
| 700–899 | **Compiler/runtime only**                 |
| 900–999 | **Reserved for future/experimental**      |
