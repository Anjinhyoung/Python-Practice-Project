class Person:
    def __init__(self):
        print('person __init__')
        self.hello="안녕하세요"



class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school="파이썬 코딩 도장"

if __name__ == '__main__':
    james=Student()
    print(james.school)
    #print(james.hello)  # 애때문에 에러가 발생



print("")

class Person:
    def __init__(self):
        print('person __init__')
        self.hello="안녕하세요"



class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school="파이썬 코딩 도장"

if __name__ == '__main__':
    james=Student()
    print(james.school)
    print(james.hello)


# 기반 클래스를 초기화 하지 않아도 되는 경우


print("")

class Person:                       # 기반 클래스
    def __init__(self):
        print('person __init__')
        self.hello="안녕하세요"



class Student(Person):              #      파생 클래스
    pass

james=Student()
print(james.hello)