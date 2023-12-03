def build_matrix(f):
    matrix = []
    for i, line in enumerate(map(str.strip, f.readlines())):
        start_pos = None
        matrix.insert(i, [])
        for j, char in enumerate(line):
            if char.isdigit():
                if start_pos is None:
                    start_pos = (i, j)
                matrix[i].append((int(char), start_pos))
            else:
                start_pos = None
                matrix[i].append(char)
    return matrix


def get_num(matrix, start_pos):
    num = 0
    for i in range(start_pos[0], len(matrix)):
        for j in range(start_pos[1], len(matrix[i])):
            if type(matrix[i][j]) == tuple:
                num = num * 10 + matrix[i][j][0]
            else:
                return num


def get_adjacent_nums(directions, matrix):
    nums = set()
    for ii, jj in directions:
        if type(matrix[ii][jj]) == tuple:
            nums.add(get_num(matrix, matrix[ii][jj][1]))
    return nums


def get_directions(i, j, matrix):
    directions = []
    if i > 0:
        directions.append((i - 1, j))
        if j > 0:
            directions.append((i - 1, j - 1))
        if j < len(matrix[i]) - 1:
            directions.append((i - 1, j + 1))
    if i < len(matrix) - 1:
        directions.append((i + 1, j))
        if j > 0:
            directions.append((i + 1, j - 1))
        if j < len(matrix[i]) - 1:
            directions.append((i + 1, j + 1))
    if j > 0:
        directions.append((i, j - 1))
    if j < len(matrix[i]) - 1:
        directions.append((i, j + 1))
    return directions


def part1(file):
    ret = 0
    with open(file) as f:
        matrix = build_matrix(f)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                char = matrix[i][j]
                if type(char) == str and char != '.':
                    directions = get_directions(i, j, matrix)

                    nums = get_adjacent_nums(directions, matrix)

                    ret += sum(nums)

        return ret


def part2(file):
    ret = 0
    with open(file) as f:
        matrix = build_matrix(f)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                char = matrix[i][j]
                if type(char) == str and char == '*':
                    directions = get_directions(i, j, matrix)

                    nums = get_adjacent_nums(directions, matrix)

                    if len(nums) == 2:
                        ret += nums.pop() * nums.pop()

        return ret


if __name__ == '__main__':
    assert 4361 == part1('example.txt')

    print(part1('input.txt'))

    assert 467835 == part2('example.txt')

    print(part2('input.txt'))
