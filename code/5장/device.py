#device.py

import random

class Device:
    """
    Base Iot device
    기반 사물인터넷 장치
    """
    def __init__(self, name: str) -> None:
        self.name = name
        
    def connect(self) -> None:
        print(f"{self.name} connecting...")
        
    def status(self) -> str:
        return "Unknown"
    
class SensorDevice(Device):
    """
    A device that reads data.
    데이터를 읽을 수 있는 장치.
    """
    
    def status(self) -> str:
        return "Reading data..."
    
    def read(self) -> float:
        """가짜 온도 값을 반환"""
        return 0.0
    
class ActuatorDevice(Device):
    """
    A device that performs actions.
    작동할 수 있는 장치.
    """
    
    def status(self) -> str:
        return "Performing action..."
    
class TemperaturesSensor(SensorDevice):
    """
    Simulated temperature sensor.
    온도 센서 시뮬레이션.
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def read(self) -> float:
        """가짜 온도 값을 반환"""
        return round(random.uniform(20.0, 30.0), 2)
    
class LightSenosor(SensorDeivce):
    """
    simulated light sensor.
    빛 센서 시뮬레이션.
    """
    def read(self) -> float:
        """가짜 빛 값을 반환"""
        return round(random.uniform(0, 100), 2)

    