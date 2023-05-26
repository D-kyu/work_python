# 회원정보를 입력 받아서 출력 하는 예제 진행

# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

# 풀이 
name = input("이름입력 : ")

while True :
    age = input("나이를 입력해주세요 : ")
    if age.isdigit() :
        age = int(age)
        if 0 < age < 200  : break
    print("나이를 잘 못 입력하셨습니다.") 
    
while True :
    gender = input("성별을 입력해주세요  : (M,m) (F,f) ")
    if gender == "M" or gender == "m" :
        gender_name = "남성"
        break
    elif gender == "F" or gender == "f" :
        gender_name = "여성"
        break
    else :
        print("다시 입력해주세요")
        continue

while True :
    job = int(input("직업을 선택해주세요 : 1(학생), 2(회사원), 3(주부), 4(무직)"))
    if job == 1 :
        jobs = "학생"
        break
    elif job == 2 :
        jobs = "회사원"
        break
    elif job == 3 :
        jobs = "주부"
        break
    elif job == 4 :
        jobs = "무직"
        break
    else :
        print("다시 선택해주세요")
        continue
print("=" *5, "회원정보", "=" *5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender_name}")
print(f"직업 : {jobs}")







# 선생님 풀이

# name = input("이름을 입력 하세요 : ")
# while True:
#     age = input("나이를 입력하세요 : ")
#     if age.isdigit() : # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
#         age = int(age)
#         if 0 < age < 200 : break
#     print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")
        
# while True:
#     gender = input("성별을 입력 하세요 : ")
#     if gender == 'M' or gender == 'm': break
#     elif gender == 'F' or gender == 'f': break
#     else: print("성별이 틀렸습니다. 다시 입력 해 주세요.") 

# while True:
#     jobs = input("직업을 입력 하세요 : ")
#     if jobs.isdigit() :
#         jobs = int(jobs)
#         if 0 < jobs < 5 : break
#     print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

# if gender == 'M' or gender == 'm': 
# 	gen_name = "남성"
# else: 
# 	gen_name = "여성"

# jobs_name = ("", "학생", "회사원", "주부", "무직") # 튜플 사용

# print("="*3, "회원정보", "="*3)     
# print(f"이름 : {name}")
# print(f"나이 : {age}")
# print(f"성별 : {gen_name}")
# print(f"직업 : {jobs_name[jobs]}")