# 내장 함수 : 파이썬 기본적으로 제공하며, import 없이 사용 

# ls = [1,2,3,4,5,6,7,8,9]
# print(sum(ls) / len(ls))    # 평균 구하기 

# ls2 = [10,2,6,99,75,2,5,7]
# print(sorted(ls2))  # 정렬

# print(divmod(sum(ls), 5))   # 몫과 나머지 



# 외장 함수(import 사용) : 랜덤 
import random 

# 지정한 범위 내의 임의의 수를 구하는 함수 

rand = random.randint(0, 4) # 0 ~ 4 사이의 임의의 값이 생성
rand = random.randrange(0, 4) # 0 ~ 4 미만의 임의의 값이 생성 

# 현재 시간 가져오기 
from datetime import datetime

# 현재 날짜 가져오기
datetime.today()    
# .year(연도) .month(월) .day(일) .hour(시간) 
# print(datetime.today())


# 중복 값 없는 로또번호  

print("로또 번호 : ", end="")
ls = []
while True :
    rend = random.randrange(1, 46)
    if rend not in ls : 
        ls.append(rend)
    if len(ls) == 6 : break

print(ls)