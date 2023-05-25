# 입력 받은 n개의 원소에 대한 평균 구하기 

n = int(input("원소 갯수 입력 : "))
total = 0
for i in range(n) :
    num = int(input("숫자 입력 : "))
    total += num
averge = total / n 
print("평균 : ", averge)

# 정수 n을 입력 받아 n * n 출력 하기 
n = int(input("n개 입력 : "))
for i in range(n, n*n)
    




# n개에 대한 숫자를 입력 받아 최소값 및 최대값 구하기
n = list(map(int,(input("숫자입력 : ").split())))

print(min(n))
print(max(n))






# 주민등록번호를 입력받아 생년월일, 성별 나이 출력

jumin = input("주민번호입력 : ") #9909991181465
year = int(jumin[:2])
month = int(jumin[2:4])
day = int(jumin[4:6])
gender = int(jumin[6])



current_year = 2023
if gender == 1 or gender == 2 :
    age = current_year - 1900 - year
else :
    age = current_year - 2000 - year

if gender == 1 or gender == 3 :
    gen = "남성"
else :
    gen = "여성"

print(f"당신의 나이는{age}")
print(f"당신의 생년월일은 {year}년 {month}월 {day}일")
print(f"당신의 성별은 {gen}")

