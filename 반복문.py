# while 문 : 조건이 참인 동안 반복 수행하며 주로 횟수가 정해지지 않은 경우에 사용, 횟수가 정해지지 않는 경우 반드시 탈출 조건이 필요 

# n = int(input("정수 입력 : "))
# sum = 0
# while n :
#     sum += n 
#     n -= 1 
# print(sum)

# # 유효값 체크 
# while True :
#     age = int(input("나이를 입력 : "))
#     if 0 < age < 200 :
#         break           # 정상적인 입력으로 간주 
#     print("나이를 다시 입력하세요.")


# for 요소 in 시퀀스(리스트, 튜플, 문자열) : 요소를 순회 
# fruits = ["apple", "banana", "kiwi"]
# for e in fruits :
#     print(e)

# # for 변수 in range(시작값, 종료값, 증감값) : 자바의 기본적인 for문과 동일
# n = int(input('정수를 입력 : '))
# sum = 0
# for i in range(1, n+1) :
#     sum += i  
# print(sum)


# 2중 for 문 : 구구단 출력
# for i in range(2, 10) :
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}")
#     print("-" * 20)


# 2중 for문과 조건문 활용하기 
# n = int(input("정수 입력 : "))
# for i in range(0, n) : # 입력받은 갯수 만큼 순회 
#     for j in range(0, n) :
#         if j % 2 == 0 : print(f"{j}는 짝수")
#         else : print(f"{j} 는 홀수")
#     print()

# 별찍기 : 입력 받은 수 만큼 별 찍기
# n = int(input())
# for i in range(n) : 
#     for j in range(i+1) :
#         print("*", end="")
#     print()

# n = int(input())
# for i in range(n) :
#     for j in range(n-i) :
#         print("*", end="")
#     print()


# # for문에서 continue 사용하기 : continue를 만나면 아래의 문장을 수행하지 않고 반복문의 조건문으로 이동 
# n = int(input())
# for i in range(n) :
#     if i % 2 == 0 : continue
#     print(i)

# for문을 역순으로 순회 하기 
# n = int(input())
# for i in range(n, 0 -1, -1) :
#     print(f"값 : {i}")


# for문으로 알파벳 출력 하기
# chr : 유니코드 값을 입력받아 코드의 해당하는 문자를 출력
# ord : 문자의 유니코드 값을 돌려주는 함수 
# for i in range(ord("A"), ord("Z")+1) :
#     print(chr(i), end=" ")

# for i in range(65, 90+1) :
#     print(chr(i), end=" ")


# 학점 구하기 : 성적을 입력 받아서 학점 출력 하기 (반복문 사용, 음수가 입력되면 종료, 100보다 크면 재입력 요구)

while True : 
    score = int(input("점수 입력 : "))
    # 종료 조건
    if score < 0 : break
    # 재입력 요구 조건
    if score > 100 : 
        print("점수를 잘 못 입력하셨습니다.")  
        continue
    if score >= 90 :
        grade = ("A 입니다.")
    elif score >= 80 :
        grade = ("B 입니다.")
    elif score >= 70 :
        grade = ("C 입니다.")
    elif score >= 60 :
        grade = ("D 입니다.")
    else :
        grade = "F"

    print(f"{score}에 대한 학점은 \"{grade}\"")