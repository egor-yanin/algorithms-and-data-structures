fin = open('input.txt')
a, b = map(int, fin.read().split())
fin.close()
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    fout = open('output.txt', '+w')
    fout.write(str(a + b))
    fout.close()
else:
    print('Неверные входные данные')