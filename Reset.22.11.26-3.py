#c=input("안녕하세요: ")

# a=int(input("첫 번째 숫자를 입력하세요: "))
# b=int(input("두 번째 숫자를 입력하세요: "))

# print(a+b)

aaa,bbb=input("문자열 두개를 입력하세요: ").split()
# .split()  기본으로 할 때는 띄어쓰기가 기본
print(aaa,bbb)
# 23.01.10에 몰랐던거 문장을 여러 개 입력할 때는 그만큼 변수가 필요함

# c,d,f=map(float,input("숫자 두 개를 입력하세요:").split('+'))
# print(c+d+f)

a,b,c=1,2,3
print(a,b,c,sep="+") # sep은 파이썬만 가능함

print("hello","파이썬",sep="+")

print(1,2,3,sep="\n")

# print(1 \n 2) 숫자끼리는 불가능함
print("안녕\n하세요") #  이렇게는 가능함

# \n 줄바꿈 \t 여러 칸을 띄움

print(1,end="+") # 뒤에 붙여 주는 기능
print(2,end="=") # 이것도 파이썬만 가능함
print(3)