[조건 1] 클래스 만들기
클래스 이름 : SayDays
오브젝트 만들 때 전달할 매개변수 : year, month, day
입력된 year를 기준으로 윤년(2월이 29일까지 있는 해)을 찾아야 함
메소드 days( ) : 당해년도 1월 1일 기준으로 몇째 날인지 알려줌
메소드 days_left( ) : 당해년도 12월 31일 기준으로 남은 일수를 알려줌
메소드 weekday( ) : 숫자로 요일을 알려줌( 0 : 토요일)
메소드 weekday_name( ) : 요일을 한글로 알려줌( 0 : 토요일)
요일 계산은 Zeller 계산법에 따름
import 문은 사용하지 말 것



[조건 2] 앞에서 만든 클래스를 사용해 다음과 같이 프로그램 만들기
SayDays 오브젝트 생성
while True :
input 문으로 임의의 날짜 입력받음
days( ), days_left( ), week( ), week_name( )을 출력

class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def _is_leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def _days_in_month(self, year, month):
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self._is_leap(year):
            return 29
        return days[month]

    def days(self):
        """당해년도 1월 1일 기준으로 몇째 날인지 반환"""
        total = self.day
        for m in range(1, self.month):
            total += self._days_in_month(self.year, m)
        return total

    def days_left(self):
        """당해년도 12월 31일 기준으로 남은 일수 반환"""
        total_days = 366 if self._is_leap(self.year) else 365
        return total_days - self.days()

    def weekday(self):
        """Zeller 계산법으로 요일 반환 (0: 토요일)"""
        y = self.year
        m = self.month
        d = self.day

        # Zeller: 1월, 2월은 전년도 13월, 14월로 처리
        if m < 3:
            m += 12
            y -= 1

        k = y % 100        # 연도의 뒤 두 자리
        j = y // 100       # 세기

        h = (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
        # h: 0=토, 1=일, 2=월, 3=화, 4=수, 5=목, 6=금
        return h

    def weekday_name(self):
        """요일을 한글로 반환 (0: 토요일)"""
        names = {0: "토요일", 1: "일요일", 2: "월요일",
                 3: "화요일", 4: "수요일", 5: "목요일", 6: "금요일"}
        return names[self.weekday()]


sd = SayDays(2024, 1, 1)  # 초기 객체 생성 (이후 입력으로 덮어씀)

while True:
    try:
        date_input = input("날짜를 입력하세요 (예: 2024 5 15) / 종료: q  >> ")
        if date_input.strip().lower() == 'q':
            break

        parts = date_input.strip().split()
        if len(parts) != 3:
            print("  년 월 일을 공백으로 구분해 입력하세요.")
            continue

        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        sd = SayDays(year, month, day)

        print(f"  {year}년 {month}월 {day}일")
        print(f"  - 올해 {sd.days()}번째 날")
        print(f"  - 올해 {sd.days_left()}일 남음")
        print(f"  - 요일 코드: {sd.weekday()} ({sd.weekday_name()})")
        print()

    except ValueError:
        print("  숫자를 올바르게 입력하세요.")

