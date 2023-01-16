# 상속
# 이미 만들어져 있는 클래스를 그대로 가져다가 수정하여 사용하는 방버
# 1. 클래스 가져오기
# 2. (클래스 수정하기)
# 3. 사용하기

# 위에서 언급한 상속은 마치 인가세상에서 부모자식 관계와 유사하다
# 상속이라는 개념이 항상 매번 무조건 한 번만 가능할까? no 여러 번 가능하다

# 내가 개발하는 프로그램에 타인의 클래스를 가져다가 사용하려고 하는 시점에서
# 타인의 클래스가 또 다른 클래스를 상속한 것인지의 여부도 반드시 확인해야 한다.
# : 모든 클래스는 누가 만들었던지 반드시 그 클래스에 관한 자세한 설명서도 필요하다

# class 보통예금:
# string rate

# class 정기에금(보통예금):
    # string year




# class 정기적금(정기예금):
#  string tax



class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def study(self):
        print("공부하기")


if __name__=='__main__':
    james=Student()
    james.greeting()
    james.study()





class Person:
    def greeting(self):
        print("안녕하세요")

class PersonList():
    def __init__(self):
        self.person_list=[]

    def append_person(self,person):
        self.person_list.append(person)