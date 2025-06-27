import pytest
from clyp.transpiler import parse_clyp, ClypSyntaxError

def test_transpiler():
    clyp_code = """
    # This is a comment
    if (true) {print("Hello, World!");} else {print("Goodbye, World!");}
    """
    expected_python_code = """from typeguard import install_import_hook; install_import_hook()
import clyp
from clyp.stdlib import d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
eval = clyp.eval; exec = clyp.exec
del clyp
true = True; false = False; null = None
# This is a comment
if (true):
    print("Hello, World!")
else:
    print("Goodbye, World!")

"""
    # Note: The exact output depends on the stdlib names, which can vary.
    # This test should be made more robust.
    assert "if (true):" in parse_clyp(clyp_code)

def test_new_syntax_valid_variable_declaration():
    valid_var_code = "int x = 5;"
    parsed_code = parse_clyp(valid_var_code)
    assert "x: int = 5" in parsed_code

def test_new_syntax_valid_function_definition():
    valid_func_code = "def my_func(str a) returns None { print(a); }"
    parsed_code = parse_clyp(valid_func_code)
    assert "def my_func(a: str) -> None:" in parsed_code
    assert "print(a)" in parsed_code

def test_new_syntax_valid_function_with_default_value():
    valid_func_code_default = "def my_func(str a, int b = 0) returns None { print(a, b); }"
    parsed_code = parse_clyp(valid_func_code_default)
    assert "def my_func(a: str, b: int = 0) -> None:" in parsed_code

def test_new_syntax_invalid_function_definition():
    invalid_func_code = "def my_func(a) returns None { print(a); }"
    with pytest.raises(ClypSyntaxError, match="Argument 'a' in function definition must be in 'type name' format."):
        parse_clyp(invalid_func_code)

def test_new_syntax_invalid_function_definition_missing_returns():
    invalid_func_code_no_returns = "def my_func(str a) { print(a); }"
    with pytest.raises(ClypSyntaxError, match="Function definition requires a 'returns' clause."):
        parse_clyp(invalid_func_code_no_returns)

def test_new_syntax_valid_self_in_function():
    valid_self_code = "def my_method(self, bool b) returns None { pass; }"
    parsed_code = parse_clyp(valid_self_code)
    assert "def my_method(self, b: bool) -> None:" in parsed_code

def test_empty_blocks_function():
    empty_func_code = "def my_func() returns None {}"
    parsed_code = parse_clyp(empty_func_code)
    assert "def my_func() -> None:" in parsed_code
    assert "pass" in parsed_code

def test_empty_blocks_if():
    empty_if_code = "if (true) {}"
    parsed_code = parse_clyp(empty_if_code)
    assert "if (true):" in parsed_code
    assert "pass" in parsed_code

def test_empty_blocks_nested():
    nested_empty_code = "if (true) { if(false) {} }"
    parsed_code = parse_clyp(nested_empty_code)
    assert "if (true):" in parsed_code
    assert "if(false):" in parsed_code
    assert "pass" in parsed_code

def test_range_to_syntax():
    clyp_code = "for i in range 1 to 5"
    parsed_code = parse_clyp(clyp_code)
    assert "for i in range(1, 5 + 1)" in parsed_code

def test_is_is_not_syntax():
    clyp_code = """
    if (a is b) {}
    if (x is not y) {}
    """
    parsed_code = parse_clyp(clyp_code)
    assert "if (a == b):" in parsed_code
    assert "if (x != y):" in parsed_code

def test_unless_syntax():
    clyp_code = "unless (a > b) {}"
    parsed_code = parse_clyp(clyp_code)
    assert "if not (a > b):" in parsed_code

def test_pipeline_operator():
    clyp_code = "data |> clean |> transform |> save"
    parsed_code = parse_clyp(clyp_code)
    assert "save(transform(clean(data)))" in parsed_code

def test_pipeline_operator_with_assignment():
    clyp_code = "let result = data |> clean |> transform"
    parsed_code = parse_clyp(clyp_code)
    assert "result = transform(clean(data))" in parsed_code

def test_pipeline_operator_with_args():
    clyp_code = 'data |> clean |> transform("fast") |> save'
    parsed_code = parse_clyp(clyp_code)
    assert 'save(transform(clean(data), "fast"))' in parsed_code

import tempfile
import shutil
import os

def test_import_clyp_package(tmp_path):
    # Create a package structure: pkg/__init__.clyp, pkg/mod.clyp
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.clyp").write_text("# package init\n")
    (pkg / "mod.clyp").write_text("let x = 42;")
    # Simulate importing 'pkg' (should succeed)
    code = "clyp import pkg"
    try:
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))
    except Exception as e:
        pytest.fail(f"Importing valid package failed: {e}")

def test_import_clyp_package_missing_init(tmp_path):
    # Create a folder without __init__.clyp
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "mod.clyp").write_text("let x = 42;")
    code = "clyp import pkg"
    with pytest.raises(ClypSyntaxError, match="not a Clyp package"):
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))

def test_import_clyp_single_file(tmp_path):
    # Create a single file script
    (tmp_path / "foo.clyp").write_text("let y = 99;")
    code = "clyp import foo"
    try:
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))
    except Exception as e:
        pytest.fail(f"Importing single file failed: {e}")

def test_import_clyp_subpackage(tmp_path):
    # pkg/__init__.clyp, pkg/sub/__init__.clyp, pkg/sub/mod.clyp
    pkg = tmp_path / "pkg"
    sub = pkg / "sub"
    sub.mkdir(parents=True)
    (pkg / "__init__.clyp").write_text("")
    (sub / "__init__.clyp").write_text("")
    (sub / "mod.clyp").write_text("let z = 1;")
    code = "clyp import pkg.sub"
    try:
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))
    except Exception as e:
        pytest.fail(f"Importing subpackage failed: {e}")

def test_import_clyp_subpackage_missing_parent_init(tmp_path):
    # pkg/sub/__init__.clyp, pkg/sub/mod.clyp (pkg missing __init__.clyp)
    pkg = tmp_path / "pkg"
    sub = pkg / "sub"
    sub.mkdir(parents=True)
    (sub / "__init__.clyp").write_text("")
    (sub / "mod.clyp").write_text("let z = 1;")
    code = "clyp import pkg.sub"
    with pytest.raises(ClypSyntaxError, match="not a Clyp package"):
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))

def test_comment_inside_string():
    clyp_code = 'print("Hello # not a comment") # real comment'
    parsed_code = parse_clyp(clyp_code)
    assert 'print("Hello # not a comment")' in parsed_code
    assert '# real comment' in parsed_code

def test_nested_blocks():
    clyp_code = 'if (true) { if (false) { let x = 1; } }'
    parsed_code = parse_clyp(clyp_code)
    assert 'if (true):' in parsed_code
    assert 'if (false):' in parsed_code
    assert 'x = 1' in parsed_code

def test_var_declaration_without_assignment():
    clyp_code = 'int y'
    parsed_code = parse_clyp(clyp_code)
    assert 'y: int' in parsed_code

def test_function_with_args_kwargs():
    clyp_code = 'def foo(str a, *args, **kwargs) returns int { return 1; }'
    parsed_code = parse_clyp(clyp_code)
    assert 'def foo(a: str, *args, **kwargs) -> int:' in parsed_code

def test_class_definition():
    clyp_code = 'class MyClass { def method(self, int x) returns None { pass; } }'
    parsed_code = parse_clyp(clyp_code)
    assert 'class MyClass:' in parsed_code
    assert 'def method(self, x: int) -> None:' in parsed_code

def test_repeat_loop():
    clyp_code = 'repeat [5] times { print("hi"); }'
    parsed_code = parse_clyp(clyp_code)
    assert 'for _ in range(5):' in parsed_code
    assert 'print("hi")' in parsed_code

def test_clyp_from_import(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.clyp").write_text("")
    (pkg / "mod.clyp").write_text("let x = 1;")
    code = "clyp from pkg import mod"
    try:
        parse_clyp(code, file_path=str(tmp_path / "main.clyp"))
    except Exception as e:
        pytest.fail(f"clyp from import failed: {e}")

def test_true_false_null():
    clyp_code = 'let a = true; let b = false; let c = null;'
    parsed_code = parse_clyp(clyp_code)
    assert 'a = true' in parsed_code
    assert 'b = false' in parsed_code
    assert 'c = null' in parsed_code
    assert 'true = True' in parsed_code
    assert 'false = False' in parsed_code
    assert 'null = None' in parsed_code

def test_else_if_to_elif():
    clyp_code = 'if (a) {} else if (b) {}'
    parsed_code = parse_clyp(clyp_code)
    assert 'elif (b):' in parsed_code

def test_invalid_var_declaration():
    clyp_code = 'int = 5'
    with pytest.raises(Exception):
        parse_clyp(clyp_code)
