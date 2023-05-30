# 튜플 : 변경할 수 없는 시퀀스 자료형 입니다. () 괄호를 사용하여 생성 합니다. 
# 패킹과 언패킹 개념이 있음 
# 튜플 정의 하기 

person = ("스타벅스", 28, "서울")  # () 생략 가능, 쓰기 불가 특성 
# person[0] = "다른이름으로변경"
# print(person)

# 튜플 언패킹 하기 (구조 분해랑 유사함)
# name, age, city = person
# print(name)
# print(age)
# print(city)

# 튜플을 이용한 함수 반환값 다루기 
def get_person() : 
    name = "김김김"
    age = 22
    city = "수원"
    return name, age, city

result = get_person()   # 튜플의 패킹 동작
print(result)


a, b, c = get_person()  
print(a,b,c)


# 기본적인 동작 
tp = 1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,
print(tp.count(4)) # 원하는 데이터의 개수를 세어주는 함수 (리스트와 동일)
print(tp.index(1)) # 원하는 데이터의 시작 인덱스를 알려 줌 
print(len(tp))     # 튜플에 포함된 데이터의 개수 
print(tp.__len__())


# 튜플에서 사용 불가 (삭제는 안됨)
# t1 = 1,2,3,4,5,6
# del t1[0]