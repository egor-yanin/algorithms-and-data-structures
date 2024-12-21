# Задание №5 по варианту: `Выборы в США`
Студент ИТМО, Янин Егор Вячеславович  468187

## Задание 

Как известно, в США президент выбирается не прямым голосованием, а путем
двухуровневого голосования. Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные
выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата. На практике, все выборщики от штата голосуют
в соответствии с результатами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число
голосов. Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом. Подведите итоги выборов: для каждого из участника
голосования определите число отданных за него голосов.
* Формат ввода / входного файла (input.txt). Каждая строка входного файла
содержит фамилию кандидата, за которого отдают голоса выборщики этого
штата, затем через пробел идет количество выборщиков, отдавших голоса
за этого кандидата.
* Формат вывода / выходного файла (output.txt). Выведите фамилии всех
кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них голосов.

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
    $env:PYTHONPATH = (Get-Location).Path
    cd ./lab6/task5
   ```
3. Запустите программу:
   ```bash
   python src/main.py
   ```
4. Запуск тестов:
   ```bash
   pytest tests/test.py -v
   ```