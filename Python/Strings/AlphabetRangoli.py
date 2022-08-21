a = '-'

def print_rangoli(size):
    for i in range(1, size):
        b = (3*size-1)//2
        c = size -i
        print(a*b + chr(97+c) + a*b)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

