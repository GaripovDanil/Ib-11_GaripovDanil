print(' '.join(str(int(n) ** 2) for n in range(int(input())) if (int(n) % 2 != 0 and int(n) ** 2) % 10 != 9))
