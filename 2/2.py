from functools import reduce
from operator import mul


def part1(file):
    rules = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    bad_ids = set()
    all_ids = set()
    with open(file) as f:
        for line in map(str.strip, f.readlines()):
            game_id, line = line.split(":")[0].split(' ')[1], line.split(":")[1]
            all_ids.add(int(game_id))
            for game_set in line.split(';'):
                game_set = [tuple(_.strip().split(' ')) for _ in game_set.split(',')]
                for balls in game_set:
                    if int(balls[0]) > rules[balls[1]]:
                        bad_ids.add(int(game_id))

    return sum(all_ids - bad_ids)


def part2(file):
    colors = ['red', 'green', 'blue']

    powers = []
    with open(file) as f:
        for line in map(str.strip, f.readlines()):
            totals = {c: [] for c in colors}
            game_id, line = line.split(":")[0].split(' ')[1], line.split(":")[1]
            for game_set in line.split(';'):
                game_set = [tuple(_.strip().split(' ')) for _ in game_set.split(',')]
                for balls in game_set:
                    totals[balls[1]].append(int(balls[0]))

            powers.append(reduce(mul, [max(totals[c]) for c in colors]))

    return sum(powers)


if __name__ == '__main__':
    assert 8 == part1('example.txt')

    print(part1('input.txt'))

    assert 2286 == part2('example.txt')

    print(part2('input.txt'))
