class car:
    def __init__(self,color):
        self.name="자동차"
        self.color = color

    def qa(self):
        print("최종 생산 결과:" +self.color+"색 "+self.name)

if __name__ == '__main__':
    cus1=car("흰색")
    cus1.qa()
    cus2 = car("핑크")
    cus2.qa()


# init 메서드: 내부의 코드는 객체를 만드는 시점에서 무조건 실행된다.
            #  1. 다수의 객체에 공통 사항이 필요하면 여기에 서술한다.
            #  2. 객체를 만드는 시점에서 추가적인 옵션이 매게 변수를 만든다.


class account:
    def __init__(self,name,age,address):
        self.name2="Sbs은행"  # 기본 환경 설정
        self.name=name
        self.age=age
        self.address=address


    def info(self):
        print("{0}에서 {1}으로 된 통장을 만들고 내 나이는 {2}이고 주소는 {3}이다".format(self.name2,self.name,self.age,self.address))

if __name__ == '__main__':
    anjinhyoung=account("안진형",27,"서울")
    anjinhyoung.info()

    print("이름:",anjinhyoung.name)
    print("나이:", anjinhyoung.age)
    print("주소:", anjinhyoung.address)





    # 비공개 : 만들어진 객체에서 임의대로 수정이 불가능
    #           클래스 내부의 메서드에서만 접근이 가능하다

    # 1.언더스코어를 연속으로 두 번 사용하고 속성 이름을 서술한다.
    # 2. 최초에 값을 대입하는 것이 일반적인 방법으로는 안된다.
    # 3. 속성 중에서 일반적으로 외부에서 들어오는 값을 그대로 적용하는 경우에는 사용하지 않는다.



class account:
    def __init__(self,name,age,address,balance):
        self.__name2="Sbs은행"  # 기본 환경 설정
        self.name=name
        self.age=age
        self.address=address

        self.__balance=balance


    def info(self,plus,minus):
        self.__balance+=plus
        self.__balance-=minus
        print("{0}에서 {1}으로 된 통장을 만들고 내 나이는 {2}이고 주소는 {3}이다 잔액은 {4}이다." .format(self.__name2,self.name,self.age,self.address,self.__balance))

if __name__ == '__main__':
    anjinhyoung=account("안진형",27,"서울",20000)
    anjinhyoung.info(plus=10000,minus=5000)

################################################
print("한 박자 쉬고 아래 위는 별개임")


class account:
    def __init__(self,name,age,address):
        self.__name2="Sbs은행"  # 기본 환경 설정
        self.name=name
        self.age=age
        self.address=address
        self.__balance=0


    def add(self,amount):
        self.__balance+=amount

    def subt(self,amount):
        if amount >self.__balance:
            print("잔액부족")
            return      # 더 이상 뒤에 있는 건 실행 하지 않음

        self.__balance-=amount

    def info(self):
        print("{0}에서 {1}으로 된 통장을 만들고 내 나이는 {2}이고 주소는 {3}이다 잔액은 {4}이다." .format(self.__name2,self.name,self.age,self.address,self.__balance))

if __name__ == '__main__':
    anjinhyoung=account("안진형",27,"서울")
    anjinhyoung.add(10000)

    anjinhyoung.subt(5000)

    anjinhyoung.info()  # 이렇게 해야 순서가 맞음

