a, b = map(int, input().split())
while not (-10**9 <= a <= 10**9 and -10**9 <= b <= 10**9):
    print('Неверные данные. Введите ещё раз')
    a, b = map(int, input().split())
print(a + b**2)