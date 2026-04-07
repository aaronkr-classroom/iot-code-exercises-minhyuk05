# 4_operators.py

a = 132
b = 45

fmt0 = '{:<10}' # 변수 + 공백 10개까지
fmt1 = '0b{:08b}, 0x{:02x} {:3}' # 0b________ 8개의 2진법, 0x__2개의 16진법, 3개의 10진법

#bit and &
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n = 30
print('-' * n)

print(fmt0.format('a&b'), fmt1.format(a&b,a&b,a&b))

#bit or |
print("\nbit OR |")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n = 30
print('-' * n)

print(fmt0.format('a|b'), fmt1.format(a|b,a|b,a|b))



#bit NOT ~
print("\nbit NOT ~")
print(fmt0.format('a'), fmt1.format(a,a,a))

n = 30
print('-' * n)

print(fmt0.format('~a'), fmt1.format(~a&0xff,~a&0xff,~a&0xff))

#bit 왼쪽 쉬프트 <<
print("\nbit 왼쪽 쉬프트 <<")
print(fmt0.format('a'), fmt1.format(a,a,a))

n = 30
print('-' * n)

print(fmt0.format('a << 2'), fmt1.format(a<<2&0xff,a<<2&0xff,a<<2&0xff))

#bit 오른쪽 쉬프트 >>
print("\nbit 오른쪽 쉬프트 >>")
print(fmt0.format('a'), fmt1.format(a,a,a))

n = 30
print('-' * n)

print(fmt0.format('a >> 2'), fmt1.format(a>>2&0xff,a>>2&0xff,a>>2&0xff))