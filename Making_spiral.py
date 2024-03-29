# Enter some number(N), it will create spiral (N * N) with 1 in center  (N % 2 != 0)


def full_spiral(n):
    matrix = [[0 for x in range(n)] for y in range(n)]

    y = round((n-1) / 2)
    x = round((n-1) / 2)
    dif = 1; count = 2
    matrix[y][x] = 1
    while dif < n:
        for i in range(1, dif+1):
            x += 1
            matrix[y][x] = count
            count += 1
        for i in range(1, dif+1):
            y += 1
            matrix[y][x] = count
            count += 1
        dif += 1
        for i in range(1, dif+1):
            x -= 1
            matrix[y][x] = count
            count += 1
        for i in range(1, dif+1):
            y -= 1
            matrix[y][x] = count
            count += 1
        dif += 1
    for i in range(1, dif):
            x += 1
            matrix[y][x] = count
            count += 1
    return matrix

n = int(input('Enter your number: '))
if n % 2 == 0:
    print('Only not paired numbers!')
else:
    spir = full_spiral(n)

    for y in range(len(spir)):
        for x in range(len(spir[0])):
            print('%3d' % spir[y][x], end = ' ')
        print()
        
        
        # I`ve spend so much time doing this)
