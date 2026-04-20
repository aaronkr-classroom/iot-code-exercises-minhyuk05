class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"

    def light_status(self):
        if self.light < 200:
            return "Dark"
        else:
            return "Bright"
