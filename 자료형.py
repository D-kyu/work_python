# 한번에 변수에 값 할당하기 
a = b = c = 1 
print(a, b, c)

a,b,c = 1, True, "스타벅스"
print(a,b,c)

# 변수의 타입 확인 
age = 100
is_adult = True
gender = "Male"
score = 95.67

print(type(age))
print(type(is_adult))
print(type(gender))
print(type(score))



# 형 변환 : 선언된 변수에 값이 할당되는 순간에 형이 결정되고 이 후 다른 데이터형으로 변경하는 것을 의미
print(10+int("10"))
print("나이 : "+str("33"))
print(f"나이 : {33}")

a, b = 10, "20"
print(a +int(b))

x, y, z = -1, 10, ""
print(bool(x))
print(bool(y))
print(bool(z))
