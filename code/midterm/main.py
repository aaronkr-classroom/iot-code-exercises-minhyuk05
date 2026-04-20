# lib 폴더 안에 있는 module.py에서 RoomSensor 클래스 가져오기
from lib.module import RoomSensor

# 객체 3개 생성
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 55, 420)
sensor3 = RoomSensor("Balcony", 15, 30, 150)

# 리스트에 때려 박기
sensors = [sensor1, sensor2, sensor3]

# 상태 개수 셀 딕셔너리 준비
comfort_counts = {
    "Comfortable": 0,
    "Normal": 0,
    "Warning": 0
}

# 리스트 반복 돌리기
for sensor in sensors:
    sensor.show_info()
    
    c_level = sensor.comfort_level()
    l_status = sensor.light_status()
    
    print(f"Comfort Level: {c_level}")
    print(f"Light Status: {l_status}")
    print("-" * 20)
    
    # 상태 개수 하나씩 올리기
    comfort_counts[c_level] += 1

# 최종 보너스 문제 출력
print(f"Comfortable: {comfort_counts['Comfortable']}")
print(f"Normal: {comfort_counts['Normal']}")
print(f"Warning: {comfort_counts['Warning']}")
