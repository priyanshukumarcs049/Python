import re
N = int(input())
for _ in range(N):
    line = input().strip()
    x = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]\
{3})[\s:;,)]', line, re.I)]
    for y in x:
        print (y)