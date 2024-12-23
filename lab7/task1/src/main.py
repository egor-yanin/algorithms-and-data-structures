from lab7.utils import read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def change_money(money: int, coins: list[int]):
    min_coins = [0] * (money + 1)
    for i in range(1, money + 1):
        min_coins[i] = 10**9
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_coins[i - coins[j]] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[money]


def task1():
    money, k = read_array(FILE_INPUT)
    coins = read_array(FILE_INPUT, line=1)
    result = change_money(money, coins)
    write_vars(FILE_OUTPUT, result)


if __name__ == '__main__':
    task1()
