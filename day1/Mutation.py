s = input()
t = tuple(input().split(' '))
s = s[:int(t[0])] + t[1] + s[int(t[0]) + 1:]
print (s)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)