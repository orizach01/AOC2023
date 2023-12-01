def main(file, part2: bool):
    nums = [(1, '1', 'one'),
            (2, '2', 'two'),
            (3, '3', 'three'),
            (4, '4', 'four'),
            (5, '5', 'five'),
            (6, '6', 'six'),
            (7, '7', 'seven'),
            (8, '8', 'eight'),
            (9, '9', 'nine')]
    with open(file) as f:
        ret = 0
        for line in [_.strip() for _ in f.readlines()]:
            idx = []
            for num in nums:
                try:
                    i = line.index(num[1])
                    idx.append((num[0], i))

                    i = line.rindex(num[1])
                    idx.append((num[0], i))

                except ValueError:
                    pass

                if not part2:
                    continue

                try:
                    i = line.index(num[2])
                    idx.append((num[0], i))

                    i = line.rindex(num[2])
                    idx.append((num[0], i))
                except ValueError:
                    pass

            idx.sort(key=lambda t: t[1])

            ret += idx[0][0] * 10 + idx[-1][0]

        return ret


if __name__ == '__main__':
    res = main('example.txt', part2=False)

    assert res == 142

    res = main('input.txt', part2=False)

    print(res)

    assert main('example2.txt', part2=True) == 281

    res = main('input.txt', part2=True)

    print(res)
