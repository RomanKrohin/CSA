# CSA

Доклад: https://docs.google.com/document/d/1pqh6lWx7quKqExYecAtPWpER1Pg1ET_thW8gMhzH160/edit?usp=sharing

Презентации: https://docs.google.com/presentation/d/1ucovfqSpkRbDhBtjRxTBdhUN7Sblf31OOiO9-Uxf1cA/edit?usp=sharing

- Крохин Роман Олегович
- P3224
- ```asm | stack | harv | hw | instr | struct | stream | port | pstr | prob1 | spi```
- Облегченный вариант

## Язык программирования

```ebnf
program             ::= { statement }

statement           ::= section [ comment ] "\n"
                        | declaration [ comment ] "\n"
                        | label [ comment ] "\n"
                        | instruction [ comment ] "\n"

section             ::= "_data" | "_programme"
comment             ::= "$$" { any_character } "$$"
any_character       ::= ? any valid character ?

declaration         ::= name_of_variable "=" value
name_of_variable    ::= [ a-zA-Z_ ] { [ a-zA-Z0-9_ ] }
value               ::= number | string
number              ::= [ "-" ] digit {digit}
digit               ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
string              ::= {string_character}
string_character    ::= ? any valid character ?

label               ::= "@ " label_name ":"
label_name          ::= [ a-zA-Z_ ] { [ a-zA-Z0-9_ ] }

instruction         ::= command {argument}
command             ::= [ a-zA-Z_ ] { [ a-zA-Z0-9_ ] }
argument            ::= number | name_of_variable

instruction         ::= zero_operand
                        num_or_var_operand  var_or_number
                        label_name_operand  label_name

zero_operand        ::= "add"
                        "pop"
                        "incr"
                        "decr"
                        "hlt"
                        "print"
                        "read"
                        "sub"
                        "div"
                        "mul"
                        "push_by_adr"
                        "load_by_adr"

num_or_var_operand  ::= "push"
                        "mod"

label_name_operand  ::= "jmp"
                        "jeq"
                        "jne"
                        "jle"
                        "jla"

var_or_number       ::=     value | name_of_variable
```

### Примечание

- Код выполняется последовательно
- Первой инструкцией считается инструкция, с которой начинется лейбл "start"
- Все переменные должны быть обхявлены в специальной секии "_data"
- Метки должны быть объявлены в отдельной строке
- Переход по метки означает переход на иструкцию последующую после ее объвления