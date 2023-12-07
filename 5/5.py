def part1(file):
    with open(file) as f:
        seeds = list(map(int, f.readline().split(":")[1].strip().split(' ')))
        f.readline()
        # sections = f.read().split('\n\n')
        sections = [list(map(lambda x: tuple(map(int, x.split())), s.split('\n')[1:])) for s in f.read().split('\n\n')]
        new_seeds = []
        for seed in seeds:
            for section in sections:
                for mapping in section:
                    dest, source, length = mapping
                    if source <= seed < source + length:
                        seed = dest + (seed - source)
                        break

            new_seeds.append(seed)

        return min(new_seeds)


def part2(file):
    with open(file) as f:
        ranges = list(map(int, f.readline().split(":")[1].strip().split(' ')))
        seeds = []
        while ranges:
            seeds.append((ranges.pop(0), ranges.pop(0)))

        f.readline()
        # sections = f.read().split('\n\n')
        sections = [list(map(lambda x: tuple(map(int, x.split())), s.split('\n')[1:])) for s in f.read().split('\n\n')]
        new_seeds = []
        for i, r in enumerate(seeds):
            for seed in range(r[0], r[0] + r[1]):
                for section in sections:
                    for mapping in section:
                        dest, source, length = mapping
                        if source <= seed < source + length:
                            seed = dest + (seed - source)
                            break

                new_seeds.append(seed)

        return min(new_seeds)


if __name__ == '__main__':
    assert 35 == part1('example.txt')

    print(f'part1 {part1("input.txt")}')

    assert 46 == part2('example.txt')

    print(f'part2 {part2("input.txt")}')
