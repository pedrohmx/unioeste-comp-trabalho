# The C+- Language Specification

## Data Types

- Integer types:
  - signed integer (two's complement)
    - i8, i16, i32, i64
  - unsigned integer
    - ui8, ui16, ui32, ui64
- Floating point types:
  - f32, f64
- boolean types:
  - bool: single byte, false if zero, true otherwise

## Symbols

- `#`: Comments, reasoning being compatibility with shebang expressions on script files

## Operations

- `=`: Attribution
  - `<type> <id> = <value>`

### Logical Operations

Logical operations, results in a boolean value.

For non-boolean operands, zero means `false`, otherwise `true`.

```Sintax: <operand> <op> <operand>```

- `&&`: and
- `||`: or
- `!` : not
  - `! <operand>`

### Relational Operations

Comparation expressions, results in a boolean value.

```Sintax: <operand> <op> <operand>```

- `==`: equality
- `!=`: not equal
- `>=`: more than or equal
- `<=`: less than or equal
- `>`:  more than
- `<`:  less than

### Arithmetic Operations

```Sintax: <operand> <op> <operand>```

- `+`: sum
- `-`: subtraction
- `*`: multiplication
- `/`: division
- `%`: module

### Flow Control Statements
### Identifiers and KeyWords

## EBNF Specification


