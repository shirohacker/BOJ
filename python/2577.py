a = int(input())
b = int(input())
c = int(input())
mul = a * b * c

count = [0 for i in range(10)]
string_list = list(str(mul))

for i in string_list:
    count[int(i)] += 1

for i in count:
    print(i)