def get_results(line):
    winning = set(map(int, line.split(':')[1].split('|')[0].strip().split()))
    have = set(map(int, line.split(':')[1].split('|')[1].strip().split()))
    return have, winning


def part1(file):
    ret = 0
    with open(file) as f:
        for line in map(str.strip, f.readlines()):
            have, winning = get_results(line)
            ret += 2 ** (len(have & winning) - 1) if len(have & winning) else 0
    return ret


def part2(file):
    with open(file) as f:
        res = []
        for i, line in enumerate(map(str.strip, f.readlines())):
            have, winning = get_results(line)
            res.append(len(winning & have))

        cards = [1] * len(res)
        for i, card in enumerate(cards):
            for j in range(1, res[i]+1):
                cards[i+j] += card

        return sum(cards)


if __name__ == '__main__':
    assert 13 == part1('example.txt')

    print(part1('input.txt'))

    assert 30 == part2('example.txt')

    print(part2('input.txt'))
