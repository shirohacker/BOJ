'''
아래 코드를 다음과 같이 간단히 할 수 있다.
a, b = map(int, input().split())
'''
a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')