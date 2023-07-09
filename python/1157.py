string = input().lower()
alphabet_list = [0 for i in range(26)]

for i in string:
    alphabet_list[ord(i)-97] += 1

max_list_idx = 0
max_list_idx_val = 0
flag = 0

# alpha_list에서 가장 큰 값을 가진 원소의 인덱스를 찾음
'''
    아래 코드는 다음과 같이 간단히 작성할 수 있음
    max_count = max(alphabet_list)
    max_idx = alphabet_list.index(max_count)
'''
for i in range(len(alphabet_list)):
    if (alphabet_list[i] > max_list_idx_val):
        max_list_idx = i    # 최대 값 구하기
        max_list_idx_val = alphabet_list[i] # 최대 값의 인덱스 구하기

'''
    아래 코드는 다음과 같이 간단히 작성할 수 있음
    if alphabet_list.count(max_count) > 1:
        print('?')
    else:
        print(chr(max_idx + ord('a')).upper())
'''
for j in range(len(alphabet_list)):
    if (alphabet_list[max_list_idx] == alphabet_list[j] and max_list_idx != j):
        print('?')
        flag = 1
        break

if (flag == 0):
    print(chr(max_list_idx+97).upper())