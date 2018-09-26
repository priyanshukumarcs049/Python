if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    P = list(map(int, arr))
    Q = set(P)
    R = sorted(list(Q))
    print (R[-2])