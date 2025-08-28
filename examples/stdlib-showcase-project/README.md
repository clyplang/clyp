# Standard Library Showcase Project

Comprehensive demonstration of Clyp's enhanced standard library with 45+ utility functions.

## Function Categories

### 1. Debug and Development
- `debug()` - Enhanced debugging with stack traces
- `profile()` - Performance profiling with memory tracking

### 2. JSON Operations
- `json_parse()` - Enhanced JSON parsing with error handling
- `json_stringify()` - Pretty printing and serialization

### 3. Math Utilities
- `clamp()` - Constrain values to ranges
- `lerp()` - Linear interpolation
- `distance_2d()` - 2D distance calculation

### 4. Collection Utilities
- `unique()` - Remove duplicates
- `partition()` - Split collections by predicate
- `group_by()` - Group items by function result
- `take()`, `drop()` - List slicing operations
- `take_while()`, `drop_while()` - Conditional operations
- `chain()` - Combine multiple collections

### 5. Functional Programming
- `pipe()` - Function composition pipeline
- `compose()` - Function composition
- `curry()` - Function currying
- `tap()` - Debugging utility for pipelines
- `when()`, `unless()` - Conditional execution

### 6. Formatting Utilities
- `format_bytes()` - Human-readable file sizes
- `format_duration()` - Human-readable time durations
- `format_timestamp()` - Date/time formatting

### 7. Dictionary Utilities
- `deep_merge()` - Recursive object merging
- `get_nested()`, `set_nested()` - Nested property access
- `pick()`, `omit()` - Object property selection
- `zip_dict()` - Create dictionary from key/value arrays

### 8. Safe Operations
- `safe_get()` - Exception-safe property access
- `safe_call()` - Exception-safe function calls

### 9. Advanced Caching
- `memoize_with_ttl()` - Time-based function caching

## Running

```bash
clyp run .
```

## Expected Output

Demonstrates all standard library functions with practical examples and clear output showing their capabilities.