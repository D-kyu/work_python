# 입력 받은 수가 소수인지 아닌지 판별하기(함수이용)
# 소수 : 1과 자기 자신 이외에 나누어지지 않는 수 
def num(n) :
    for i in range(2, n) : # 1과 자기 자신
        if n % i == 0 : return False 
    return True

n = int(input("정수 입력 : "))

if(num(n)) :
    print(f"{n}은 소수입니다.")
else :
    print("소수가 아닙니다.")
    