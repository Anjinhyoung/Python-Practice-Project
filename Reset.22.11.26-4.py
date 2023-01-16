print(3>1) # T rue라고 뜸

print("A"=="a") # False라고 뜸

# print(1 is 1.0) # False 라고 나옴 1= 정수 객체 1.0=실수 객체
# print(1 is not 1.0) # True라고 나오겠죠
# is, is not 객체 비교할 때 나옴
# id는 객채 확인
# 값 비교에는 is를 쓰지 않기
print(id(1.0))

# True랑 or not은 설명 안해도 되겠지?? 진형아

print(not True and False or not False) # 이렇게 되면 앞에서부터 하게 됨, 순서가 헷갈릴때는 ()붙여주면 됨
print(False or True) # 둘 중에 하나만 맞으면 됨

# 비교 연산자(is, is , ==, !=, <, >, <=, >=) 먼저 그 다음 논리 연산자(not, and, or)

# bool() ---> 정수 0, 실수 0.0 제외하고 True 빈 문자열("")을 제외하고 True임

# 단락 평가는 첫 번째 값만으로 결과가 확실할 때 두 번째값은 확인하지 않는 방법 잘 모르겠으면 8번 ppt를 보면 됨

# 파이썬에서는 단락 평가를 마지막까지 실시한 값으로 함

print("1번입니다", True and "python") # python이 나옴 두 번째 것도 판단해야 되기 때문에
# but or은 앞이 거짓이 나오면 뒤에 보지도 않고 바로 False 나옴

# 참고로 and or 이렇게 대놓고 쓸 수 있는 건 파이썬 밖에 안됨

print("1번입니다", True or "python")

print( 0 or "True")

