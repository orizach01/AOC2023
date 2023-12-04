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
        cards = [None]
        for i, line in enumerate(map(str.strip, f.readlines())):
            have, winning = get_results(line)
            cards.append([len(winning & have)])

        for i in range(1, len(cards)):
            for res in cards[i]:
                for j in range(1, res + 1):
                    cards[i + j].append(cards[i + j][0])

        return len([item for sublist in cards[1:] for item in sublist])


if __name__ == '__main__':
    assert 13 == part1('example.txt')

    print(part1('input.txt'))

    assert 30 == part2('example.txt')

    print(part2('input.txt'))
