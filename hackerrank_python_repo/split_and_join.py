def split_and_join(line):
    x = '-'
    line = line.split(' ')
    line = x.join(line)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)