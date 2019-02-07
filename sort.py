with open('references/negative.txt', 'r') as r:
    for line in sorted(r):
        with open('references/negative_n.txt', 'a') as w:
            w.write(line)
            print(line, end='')
