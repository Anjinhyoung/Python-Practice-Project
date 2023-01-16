class Test:
    def greeting(self):
        print("welocme")

if __name__=='__main__':
    james=Test()
    james.greeting()


# 1-7행까지가 객체 지향 파이썬 기본 코드
# 1-3행까지가 설계도
# 6행이 설계도를 가지고 제품을 만듦


def print_numbers(*x):
   print(*x)     # * ()의 유무 없으면 튜플이 됨



if __name__=='__main__':
    a=[1,2,3,4,5]
    print_numbers(*a)
    # *a로 출력할 경우 1,2,3   a로 출력할 경우 [1,2,3]

def print_numbers(a,b,c):
   print(a,b,c)
   print(a)
   print(b)
   print(c)



if __name__=='__main__':
    print_numbers(1,2,3)


def a(*x):
    for abc in x:
        print(abc)

if __name__=='__main__':
    a=range(1,11)
    print(*a)   # a없으면 range(0,10)이 나옴




class Test10:
    def __init__(self):
        self.hello="welcome"

    def greeting10(self):
        print(self.hello)
if __name__=='__main__':

    james=Test10()
    james.greeting10()

    kor=Test10()
    kor.greeting10()


print("")











