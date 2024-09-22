def main():
    fin = open('input.txt')
    n = int(fin.readline())
    fin.close()
    fib = [0, 1]
    if 0 <= n <= 10**7:
        for i in range(2, n + 1):
            fib.append((fib[-1] + fib[-2]) % 10)
        fout = open('output.txt', '+w')
        fout.write(str(fib[n]))
        fout.close()
    else:
        print('Неверные входные данные')

main()