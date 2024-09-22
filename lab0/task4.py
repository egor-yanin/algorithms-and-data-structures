import time
from task3 import main


start = time.perf_counter()
main()
print(time.perf_counter() - start)
