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
                        | "pop"
                        | "incr"
                        | "decr"
                        | "hlt"
                        | "print"
                        | "read"
                        | "sub"
                        | "div"
                        | "mul"
                        | "push_by_adr"
                        | "load_by_adr"

num_or_var_operand  ::= "push"
                        | "mod"

label_name_operand  ::= "jmp"
                        | "jeq"
                        | "jne"
                        | "jle"
                        | "jla"


var_or_number       ::= value | name_of_variable
```

### Примечание

- Код выполняется последовательно
- Первой инструкцией считается инструкция, с которой начинется лейбл "start"
- Все переменные должны быть обхявлены в специальной секии "_data"
- Метки должны быть объявлены в отдельной строке
- Переход по метки означает переход на иструкцию последующую после ее объвления
- Исполняемый код и метки объявляются в секции "_programme"

## (ISA) Система команд

#### Набор исполняймых инструкций:

- ```push name_of_variable``` - положить значение перменной на вершину стека ```[...] => [..., value]```
- ```push value``` - положить значение на вершину стека ```[...] => [..., value]```
- ```pop``` - удалить верхний элемент стека ```[value_1, value_2] => [value_1]```
- ```incr``` - увеличть верхнее значения стека на 1 ```[..., value] => [..., value+1]```
- ```decr``` - уменшить верхнее значения стека на 1 ```[..., value] => [..., value-1]```
- ```hlt``` - завершить выполнение программы
- ```print``` - помещает верхнее значение стека в буфер вывода ```[..., value] => [...]```
- ```read``` - помещает один символ из буфера ввода на верх стека ```[...] => [value]```
- ```add``` - складывает два верхних значения со стека и помещает результат на верх стека ```[value_1, value_2] => [value_1, value_2, value_1+value_2]``` 
- ```sub``` - вычитает два верхних значения со стека и помещает результат на верх стека ```[value_1, value_2] => [value_1, value_2, value_1+value_2]```
- ```div``` - целочисленно делит два верхних значения со стека и помещает результат на верх стека ```[value_1, value_2] => [value_1, value_2, value_1/value_2]```
- ```mul``` - умножает два верхних значения со стека и помещает результат на верх стека ```[value_1, value_2] => [value_1, value_2, value_1*value_2]```
- ```mod operand``` - находит остаток от деления верхнего знаения стека и операнда и помещает на вершину стека ```[value] => [value, value%operand]```
- ```push_by_adr``` - помещает в память значение с вершины стека по адресу равному второму с вершины значению стека ```[adr, value_by_adr] => [adr]```
- ```load_by_adr``` - помещает на верх стека значение из ячейки чей адрес равен значению на вершине стека ```[adr] => [adr, value_by_adr]```
- ```jmp``` - безусловный переход на метку
- ```jeq``` - переход на метку, если ```a==b```, где ```[a, b]```
- ```jne``` - переход на метку, если ```a!=b```, где ```[a, b]```
- ```jla``` - переход на метку, если ```a>b```, где ```[a, b]```
- ```jle``` - переход на метку, если ```a<b```, где ```[a, b]```