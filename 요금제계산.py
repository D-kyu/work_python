# 요금제 계산 
# 영식 요금제 : 30초에 10원 
# 민식 요금제 : 60초에 15원
# 입력은 첫 줄에 통화 횟수를 입력 : 3 
# 각 통화에 대한 통화 시간을 입력 : 34 56 78

cnt = int(input("통화 횟수 : "))
call_time = list(map(int,input("통화시간 : ").split())) 
y_pay = m_pay = 0

for i in range(cnt) :     # cnt 횟수만큼 반복 
    y_pay += (call_time[i] // 30) * 10 + 10  
    m_pay += (call_time[i] // 60) * 15 + 15 

if y_pay > m_pay :
    print("M", m_pay)
elif y_pay < m_pay : 
    print("Y", y_pay)
else :
    print("Y N", y_pay)