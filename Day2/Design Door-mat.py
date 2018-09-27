a, b = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(b, '-') for i in range(a//2)]
print('\n'.join(pattern + ['WELCOME'.center(b, '-')] + pattern[::-1]))