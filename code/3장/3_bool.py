# 3_bool.py
a = True # 참
b = False # 거짓
#c = true # 오류

#숫자에서 bool로 변환
d = bool(0) # False
e = bool(1) # True
f = bool(-1) # True
g = bool(10) # True
h = bool("1") # True
i = bool('hello') # True
j = bool("") # False

#0과 데이터 없을때만 False
print(a, b, d, e, f, g, h, i, j)
