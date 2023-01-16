# 아래거랑 위에 거 같다.

# def add(x,y):
#   res=x+y
#    print(res)


#if __name__=='__main__':    # 파이썬 프로그램으ㅣ 시작 지점을 의미한다.
#    add(5,6)


# 함수, 클래스, 모듈
# 함수: 재료를 집어 넣어 결과를 도출한다.


# 지금까지는 하나의 소스 코드(파일)로 구성된 프로그램
# 1. 기본 문법
# 2. 만들어져 있는 함수 가져다 사용하기
# 3. 내가 만든 함수


def add(x,y):   # x,y를 매개 변수라고 함
    res=x+y
    return res

def minus(x,y):
    res3=x-y
    return res3

def div(x,y):
    res5=x*y
    return res5

def mod(x,y):
    res10=x/y
    return res10



if __name__=='__main__':    # 파이썬 프로그램으ㅣ 시작 지점을 의미한다.
    total = add(5,6)
    print(total)

    total1=minus(10,5)
    print(total1)

    total5 = div(1, 5)                          # 1,5가  인수임
    print(total5)

    total10 = mod(10, 5)
    print(total10)

# 선생님 답변
def div(a,b):
    res=a/b
    print(res)

if __name__=='__main__':
    div(6,2)

def div(a,b):
    print(a/b)

if __name__=='__main__':
    div(6,2)

















