from lab2.task4.src.main import main
import psutil
import time


start = time.perf_counter()
main('input.txt')
print(f'Затрачено времени: {round(time.perf_counter() - start, 6)} c.')
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")