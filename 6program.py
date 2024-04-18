from collections import deque

def min_moves_to_destination(board, n):
    directions_knight = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    directions_king = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # Находим начальную и конечную позиции
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start = (i, j, 'K')  # Начинаем с коня
            elif board[i][j] == 'F':
                end = (i, j)
    
    queue = deque([(start[0], start[1], start[2], 0)])  # добавляем количество шагов
    visited = set([(start[0], start[1], start[2])])

    while queue:
        i, j, piece, steps = queue.popleft()
        if (i, j) == (end[0], end[1]):
            return steps
        
        # Проверяем возможные направления в зависимости от типа фигуры
        directions = directions_knight if piece == 'K' else directions_king

        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < n and 0 <= new_j < n and board[new_i][new_j] != '#':
                new_piece = piece
                if board[new_i][new_j] == 'K' and piece != 'K':
                    new_piece = 'K'  # Превращаемся в коня
                elif board[new_i][new_j] == 'G' and piece != 'G':
                    new_piece = 'G'  # Превращаемся в короля
                if (new_i, new_j, new_piece) not in visited:
                    visited.add((new_i, new_j, new_piece))
                    queue.append((new_i, new_j, new_piece, steps + 1))  # увеличиваем количество шагов
    
    return -1  # Путь не найден

# Чтение входных данных
n = int(input())
board = [input() for _ in range(n)]

# Поиск минимального количества ходов
result = min_moves_to_destination(board, n)
print(result)