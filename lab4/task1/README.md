# Задание №1 по варианту: `Стек`
Студент ИТМО, Янин Егор Вячеславович  468187

## Вариант 24

## Задание 
Реализуйте работу стека. Для каждой операции изъятия элемента выведите ее
результат.
На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда — это либо “+ N”, либо “–”. Команда “+
N”означает добавление в стек числа N, по модулю не превышающего 10^9. Команда “–” означает изъятие элемента из стека. Гарантируется, что не происходит
извлечения из пустого стека. Гарантируется, что размер стека в процессе выполнения команд не превысит 10^6 элементов.

* Формат входного файла (input.txt). В первой строке содержится M (1 ? M ? 10^6) – число команд. В последующих строках содержатся команды, по одной в каждой строке.


* Формат выходного файла (output.txt). Выведите числа, которые удаляются из очереди с помощью команды «–», по одному в каждой строке. Числа
нужно выводить в том порядке, в котором они были извлечены из очереди.
Гарантируется, что извлечения из пустой очереди не производится.

## Input / Output 

| Input                                              | Output      |
|----------------------------------------------------|-------------|
| 6<br/>+ 1<br/>+ 10 <br/>-<br/>+ 2<br/>+ 1234<br/>- | 10<br/>1234 |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/egor-yanin/algorithms-and-data-structures.git
   ```
2. Перейдите в папку с проектом:
   ```bash
    cd ./lab4/task1
    $env:PYTHONPATH = (Get-Location).Path
   ```
3. Запустите программу:
   ```bash
   python src/main.py
   ```
4. Запуск тестов:
   ```bash
   pytest tests/test.py -v
   ```