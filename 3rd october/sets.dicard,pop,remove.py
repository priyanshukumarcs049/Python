n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    x = list(input().split())
    eval('s.{0}({1})'.format(*x+['']))
print (sum(s))