def print_formatted(number):
    a = len(bin(number).removeprefix('0b'))
    for i in range(1, number + 1):
        print (str(i).rjust(a), oct(i).removeprefix('0o').rjust(a), hex(i).removeprefix('0x').upper().rjust(a), bin(i).removeprefix('0b').rjust(a))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)