# Задание №13 по варианту: `Реализация стека, очереди и связанных списков`
Студент ИТМО, Янин Егор Вячеславович  468187

## Вариант 24

## Задание 

1. Реализуйте двусвязный список с функциями вывода содердимого списка,
добавления и удаления элемента с начала списка, добавления и удаления
элемента с конца списка, добавления и удаления элемента до заданного
элемента (key); поиска элемента в списке.
2. Реализуйте стек на основе связного списка с функциями isEmpty, push, pop
и вывода данных.



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
    cd ./lab4/task13
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