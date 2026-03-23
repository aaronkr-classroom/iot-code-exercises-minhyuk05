# 3_list.py
# 리스트 생성
my_list = [10, 20, 30, 40]

#리스트 요소에 접근
print(my_list[0])
print(my_list[3])

# 리스트에 요소 추가
my_list.append(50)
print(my_list)

# 특정 위치에 요소 삽입
my_list.insert(1, 15)
print(my_list)

# 리스트에서 요소 삭제
my_list.remove(30)
print(my_list)

# 인덱스로 요소 삭제
del my_list[2]
print(my_list)

# 리스트 길이 구하기
print(len(my_list))

# 리스트의 모든 요소 반복
for item in my_list:
    print(item)
    
# 리스트 슬라이싱
sub_list_1 = my_list[1:3]
print(sub_list_1)

for i in range(6, 15, 2):
    my_list.append(i*10)
    
print(my_list)

sub_list_2 = my_list[4:]
sub_list_3 = my_list[:4]
sub_list_4 = my_list[2:7:2]
sub_list_5 = my_list[::]

print(f"s2: {sub_list_2}")
print(f"s3: {sub_list_3}")
print(f"s4: {sub_list_4}")
print(f"s5: {sub_list_5}")