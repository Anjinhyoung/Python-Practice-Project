# 함수에 인수를 순서대로 넣는 방식을 위치 인수
# 위치 인수와 리스트 언패킹은 인수의 개수가 정해지지 않은 가변 인수에 사용함

# 위의 내용은 함수의 매개변수의 갯수를 개발자가 처음부터 지정하지 않고
# 상황에 따라 매개변수의 갯수가 유동적으로 변화한다는 의미


# 객체 지향 프로그래밍-oop

# 1. 설계도를 만들어서 그 설계도에 의한 제품을 만든다.
# 2. 제품은 완제품/부품 일수도 있다.-->하나의 제품을 하나의 부품으로 완성 또는 하나의 제품을 두 개 이상의 부품으로 완성
# 3. 설계도: 클래스
    # 완제품(부품):객체,인스턴스


# oop는 조립 방식이다

# 클래스 만들기>>>기능 + 상태(형태, 디자인)
            #   함수   변수
# 클래스는 최대 2 가지의 구성 요소를 갖는다: 변수& 함수


# 클래스
# 객체, 인스턴스(동일한 의미)



def hello(a,b):
    return a+b,a-b

if __name__=='__main__':
    # print(hello(1,1))
    x,y=hello(5,5)
    print(x)
    print(y)


def add(a, b):
    s = a + b
    return s


def mul(a, b):
    c = a * b
    print(c)

    q = add(a, b)
    return q


if __name__ == '__main__':
    x = 10
    y = 10000
    c=mul(x, y)
    print(c)
