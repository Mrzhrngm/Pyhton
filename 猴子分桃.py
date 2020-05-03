def fen(count, num):
    if count == 0:
        return True
    if num%5 == 1:
        num = (num-1)//5*4
        return fen(count-1, num)

def main():
    for num in range(1, 10000):
        re = fen(5, num)
        if re:
            print('number is %d' % num)

if __name__ == '__main__':
    main()