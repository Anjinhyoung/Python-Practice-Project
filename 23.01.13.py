# 냉장고 클래스를 만들어서 객체를 계속 만들었다.
# 현재까지 냉장고 클래스를 이용하여 몇 개의 객체를 만들었는가?

# 기본적으로 객체는 독립적이다.
# count 속성에 대하여 이전 상태를 유지(기억)하도록 하면 해결한다

# 클래스 속성 - 공유 & 공유
# 인스턴스 속성 - 개별적 & 독립적


# 클래스 속성은 클래스 외부에서 직접 언급하여 사용할 수 있다.
# 객체를 만들지 않고서도 클래스 속성은 직접 사용할 수 있다.


class Person:
    bag=[]

    def put_bag(self,stuff):
        self.bag.append(stuff)

if __name__ == '__main__':

    james=Person()
    james.put_bag("책")

    maria=Person()
    maria.put_bag("열쇠")

    print(james.bag)
    print(maria.bag)


print("한 박자 쉬고")

# 다음 코드를 수정하시오 > bag리스트 속성을 객체를 만들지 않고 직접 출력하도록 하시오


class Person:
    bag=[]

    def put_bag(self,stuff):
        self.bag.append(stuff)

if __name__ == '__main__':

    print(Person.bag)

    james=Person()
    james.put_bag("책")

    print(Person.bag)

    maria=Person()
    maria.put_bag("열쇠")

    print(james.bag)
    print(maria.bag)







    # 클래스 속성: 객체들간의 공유 속성이
    #       언제든지 그 내용을 확인할 수 있다.
    #       클래스 이름과 같이 사용할 수 있다.



