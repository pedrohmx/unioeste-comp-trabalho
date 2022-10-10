# The C+- Language Specification

## Data Types

- Integer types:
  - signed integer (two's complement)
    - i8, i16, i32, i64.
  - unsigned integer
    - ui8, ui16, ui32, ui64.
- Floating point types:
  - f32, f64.
- boolean types:
  - bool: single byte, false if zero, true otherwise.

## Symbols

- `#`: Comments, reasoning being compatibility with shebang expressions on script files.

### Literals

- String Literal: Any text enclosed in `""` is a string literal.
  - Exemple: `"Hello there!"`.
  - Cannot be attributed to a variable, but can be usend with the write statement.
- Integer Literal: Any sequence of numbers.
  - Exemple: `42`, `-13` ...
- Float Literal: Any sequence of numbers starting with a dot or with a dot in the sequence.
  - Exemple: `4.2`, `.5`
- Boolean Literal: `true`, `false`

## Operations

- `=`: Attribution
  - `<type> <id> = <value>;`
  - `<type> <id>;`

- Exemples
  - `<type> <id> = <value>, <id> = <value>;`
  - `<type> <id> = <value>, <id>;`
  - `<type> <id>, <id> = <value>;`
  - `<type> <id>, <id>;`

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

Sintax
``` <operand> <op> <operand>```

- `==`: equality
- `!=`: not equal
- `>=`: more than or equal
- `<=`: less than or equal
- `>`:  more than
- `<`:  less than

### Arithmetic Operations

Syntax:
```<operand> <op> <operand>```

- `+`: sum
- `-`: subtraction
- `*`: multiplication
- `/`: division
- `%`: module

#### Arithmetic Attributions

You may also update the value of a variable using the following expression:

`<variable> <op> = <value>`

and is equivalent to `<variable> = <variable> <op> <value>`.

- `+=`: sum
- `-=`: subtraction
- `*=`: multiplication
- `/=`: division
- `%=`: modul

#### Increment and Decrement

- increment:
  - `<variable>++`
- decrement:
  - `<variable>--`

### Flow Control Statements

#### Conditionals

- `if`: checks a statement (enclosed by parenthesis) and if its true, runs the following code block (enclosed by curly brackets)
- `else`: must be after an if statement and its statements/code block, runs a following code block if the condition in the if statement is false
- `elif`: aka poor man's switch, equivalent to an if just after else, must be after an if or an elif statement, has its own conditional expression and code block, may be folloed be else or another elif 


Syntax
```
if (<cond_expr>) {
  <stmts> 
} elif (<cond_expr>) {
  <stmts>
} else {
  <stmts>
}
```
Exemple
```
if (age < 18) {
  write "can't drink or drive"
} elif (age < 99) {
  write "can drink and drive"
} else {
  write "can't play with legos"
}
```

#### Loops

- `while`: repeats statements in followed block while condition is true.
  - `while(<cond_expr>){<stmts>}`
- `for`:
  - `for (<setup>;<cond_expr>;<post>) {<stmts>}`

Syntax

```
i32 i = 0;
while (i < 2) {
  write "Reese's puffs\n";
}


for (i = 0; i < 3; i += 1) {
  write "Eat them up\n"
}

# Output:
# Reese's puffs
# Reese's puffs
# Eat them up
# Eat them up
# Eat them up
```

### Identifiers and KeyWords

#### Identifiers

Variables must be identified with unique names, these unique names are called identifiers.

An identifier must start with a letter or underscore, and might follow with any sequence of alphanumeric characters (plus underscore).

Exemples:

```
i32 minutes = 60;
i32 _something = -1;
i32 MyVariableIs = 0;
i32 _123 = 123;
```

#### IO Statements

- `read`: reads from stdin and sets value on variable
  - Syntax: `read <variable>;`
- `write`: writes to stdout, can write variables and literals;
  - is possible to write multiple expressions separated by commas.
  - Syntax
    - `write <writables>;`
  - Examples:
    - `write <variable>;` 
    - `write <variable>, <variable>;` 
    - `write <literal>, <variable>;` 

## EBNF Specification


