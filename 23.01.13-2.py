# 정적 메서드 <-> 동적 메서드
# @staticmethod
# @ - 데코레이터

# 정적 메서드는 객체를 만들어서 사용하는 일반적인 방법이 아니고
# 클래스에서 직접 사용이 가느하다
# 즉, 객체를 만들지 않고 직접 사용 가능하ㅏ
# 클래스 매서드: 클래스 속성을 이용하는 매서드는 클래스 매세드에서 만들어야 한다

# 공통점: 굳이 객체를 만들 필요가 없이 결과만을 확인(출력)하는 경우에 사용한다


# 자동차 공장에서 퇴근 전에 오늘 생산 수량을 확인(출력)하자

class Car:
    count=0

    def __init__(self):
        Car.count+=1

    def print_count(self):
        print("{0}명이 생성 되었습니다.".format(Car.count))

if __name__ == '__main__':
    c1=Car()
    print(Car.count)
    c2=Car()
    print(Car.count)
    c3=Car()
    print(Car.count)