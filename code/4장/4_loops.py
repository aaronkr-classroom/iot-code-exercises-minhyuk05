# 4_loops.py
cars = ['Tesla', 'Hyundai', 'Kia', 'Toyota', 'Honda', 'Ford']


    
# 리스트 컴프리헨션을 이용하여 리스트 만들기 (짝수일때)
prices = [i**2 for i in range(1,13) if i % 2 == 0]

for car in cars:
    print(f"My new car is a {car}!")
    
for price in prices:
    print(f"It cost ${price},000!")