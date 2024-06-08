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

## Организация памяти

Память интсрукций и данных разделены согласно Гарвадской архитектуре

- В памяти данных длина машинного слова не ограничена
- В памяти инструкций она граничена 9 байт

Программист не имеет доступа к памяти иструкций

Поддержиаваются различные типы данных:
- integer
- char
- string

Порты ввода-вывода не отражены в памяти, для этого есть другое адресное пространство (для работы с этим пристуствуют отдельыне команды)



```
                                    data memory
                                +-----------------+
                                |      0: ...     |
                                |      1: ...     |
                                |       ...       |
                                |    2**11: ...   |
                                +-----------------+

                                inctruction memory
                                +-----------------+
                                |      0: ...     |
                                |      1: ...     |
                                |       ...       |
                                +-----------------+
```

Поддерживается разная адрессаци:

- Прямая: ```push_by_adr => [adr] => [adr, value_by_adr]```
- Косвенная: ```push name_of_var => [value_of_var]```

Строки представляют собой массив символов ```[len, char_1, char_2, ..., char_len]``` где переменная является ссылкой на его начало

## Транслятор

```python parser.py <source_filepath> <targer_filepath>```

[parser.py](spasm/translate/parser.py)

Подход:

- Построчно читает исходный файл
- Очищает исходный код от комментариев
- Разбивает обработку на две секции: ```_data``` и ```_programme```
- Парсит лейбы, перменныые и инсрукции
- Базово проверяет синтаксис
- Траслирует код в набор простых команд и группирует их в список списков ```[[opcode_1, operand_11, operand_12], [opcode_2, operand_21, operand_22], ...]```

## Модель процессора

```
python machine.py <machine_code_file> <input_file>
```

### Control Unit
![CU.drawio.svg](scheme/CU.drawio.svg)

### Data path
![Datapath.drawio.svg](scheme/Datapath.drawio.svg)

### Примечание

- Процесс моделирууется с отслеживанием по инструкции
- Остановка программы происходит по выполнении команды ```hlt``` или при ошибки (переполнение стека или неправильное использование меток)
- Доступ к памяти инструкций осуществляется по специальному регистриу - command pointer
- Предусмотрены разлиные флаги АЛУ:
    1. ```Z``` (zero)- устанавливается когда результат последней арифметической операции равен 0
    2. ```N``` (negative) - устанавливается когда результат последней арфиметической операции отрицателен 

#### Стоимость команд в тактах:

| Инструкция | Количество тактов |
|:----------:|:-----------------:|
|    push    |      1 или 2      |
|push_by_adr |         2         |
|    pop     |         2         |
|    read    |         1         |
|    jump    |         1         |
|    jla     |      5 или 6      |
|    jle     |      5 или 6      |
|    jeq     |      5 или 6      |
|    jne     |      5 или 6      |
|    add     |         6         |
|    sub     |         6         |
|    mul     |         6         |
|    div     |         6         |
|    inc     |         3         |
|    dec     |         3         |
|   print    |         1         |
|    mod     |         2         |
|load_by_adr |         6         |
|    load    |         2         |
|    halt    |         1         |

## Тестирование

- Тестирование происходит при помощи ```pytest```
- [Реализация](spasm/golden_test.py)
- Файлы утилит находятся в [директрии](spasm/golden/)
- Команда для запуска: ```poetry run coverage run -m pytest . -v```

### Linter

```
lint:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install ruff

    - name: Run ruff
      run: |
        ruff check .
```

### Tests

```
test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        cd spasm
        python -m pip install --upgrade pip
        pip install poetry
        poetry install

    - name: Run tests
      run: |
        cd spasm
        poetry run coverage run -m pytest . -v
        poetry run coverage report --omit='/usr/lib/python3/dist-packages/*' -m
```

### Output

```
======================== test session starts =========================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/roman/roman/work/CSA/spasm
configfile: pyproject.toml
plugins: yaml-1.2.1, goldie-0.1.5, golden-0.2.2, anyio-4.3.0
collected 4 items                                                    

golden_test.py::test_machine_cat[golden/cat.yml] PASSED        [ 25%]
golden_test.py::test_machine_cat[golden/hello_username.yml] PASSED [ 50%]
golden_test.py::test_machine_cat[golden/prob1.yml] PASSED      [ 75%]
golden_test.py::test_machine_cat[golden/hello_world.yml] PASSED [100%]

========================= 4 passed in 15.10s =========================
```

## Статистика

|    Тест     | Инструкций |  Исполнено  |    Такт    |
|:-----------:|:----------:|:-----------:|:----------:|
| hello world |     34     |     162     |    629     | 
| hello user  |     115    |     472     |    1908    |
|    prob1    |     36     |    17061    |   76162    |
|     cat     |     9      |     36      |    144     |