# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
# result = ""

# for e in input() :
#     if e.islower() :
#         result += e.upper()
#     else :
#         result += e.lower()
# print(result)



# 세 개 자연수 입력받아서 모두 곱함
# 결과 값에서 나오는 숫자의 횟수를 출력하기 
# 150 * 266 * 427 = 17037300
# 17037300 => 0이 3번, 1이 1번, 3이 2번, 7이 2번


a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = list(str(a * b * c))
print(ls) 
for i in range(10) :
    print(ls.count(str(i))) # 해당 문자의 개수 반환