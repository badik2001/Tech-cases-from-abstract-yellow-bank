def max_mushrooms(n, forest):
    # Создаем двумерный массив для хранения количества грибов
    dp = [[0] * 3 for _ in range(n)]

    # Заполняем последнюю строку массива dp
    for j in range(3):
        if forest[n-1][j] == 'C':
            dp[n-1][j] = 1

    # Заполняем массив dp снизу вверх
    for i in range(n-2, -1, -1):
        for j in range(3):
            # Проверяем, является ли текущая клетка 'W' (водой)
            if forest[i][j] == 'W':
                continue
            # Если текущая клетка содержит гриб, увеличиваем количество грибов в этой клетке на 1
            mushrooms_here = 1 if forest[i][j] == 'C' else 0
            # Инициализируем переменную для хранения максимального количества грибов в следующей строке
            max_mushrooms_next_row = 0
            # Проверяем соседние клетки в следующей строке на наличие грибов и выбираем максимальное количество
            for k in range(-1, 2):
                if 0 <= j+k < 3:
                    max_mushrooms_next_row = max(max_mushrooms_next_row, dp[i+1][j+k])
            # Суммируем количество грибов в текущей клетке с максимальным количеством грибов в следующей строке
            dp[i][j] = mushrooms_here + max_mushrooms_next_row

    # Проверяем случай, когда в первой строке леса нет грибов
    if max(dp[0]) == 0:
        return 0

    # Возвращаем максимальное количество грибов в первой строке леса
    return max(dp[0])

# Чтение количества строк леса
n = int(input())

# Чтение строк леса
forest = []

for _ in range(n):
    row = input().strip()
    forest.append(row)

# Вызов функции и вывод результата
print(max_mushrooms(n, forest))