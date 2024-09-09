fin = open('input.txt')
s = fin.readline()
fin.close()
a, b = map(int, s.split())
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    fout = open('output.txt', '+w')
    fout.write(str(a + b**2))
    fout.close()