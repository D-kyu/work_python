# 웹페이지로 부터 데이터를 추출하는 행위를 크롤링 
# Beautiful Soup은 HTML 및 XML 문서를 파싱하고 데이터를 추출하는 파이썬 라이브러리 
from bs4 import BeautifulSoup
# html = '''
#     <html>
#         <table border=1> 
#             <tr>
#                 <td> 항목 </td> 
#                 <td> 2013 </td> 
#                 <td> 2014 </td> 
#                 <td> 2015 </td>
#             </tr> 
#             <tr>
#                 <td> 매출액 </td> 
#                 <td> 100 </td> 
#                 <td> 200 </td>
#                 <td> 300 </td>
#             </tr> 
#         </table>
#     </html>
# '''

# soup = BeautifulSoup(html, "html.parser")

# result = soup.select("td")

# # print(result)

# for val in result :
#     print(val.text)


# html = '''
# <ul>
#     <li> 100 </li> 
#     <li> 200 </li>
# </ul> 
# <ol>
#     <li> 300 </li> 
#     <li> 400 </li>
# </ol>
# '''

# soup = BeautifulSoup(html, "html5lib")
# result = soup.select("ul li")
# print(result)

# for val in result :
#     print(val.text)


# requests : 파이썬에서 HTTP 요청과 응답을 요청
import requests 

# res = requests.get("http://naver.com")
# print("응답 코드 : ", res.status_code)

# if res.status_code == requests.codes.ok :
#     print("정상 수신 되었습니다.")
# else :
#     print(f"네트워크 오류 : [error 코드 : {res.status_code}]")




# 길이 반환
res = requests.get("http://naver.com")
# print(len(res.text))

# with open("naver.html", "w", encoding="utf8") as fd:
#     fd.write(res.text)

soup = BeautifulSoup(res.text, "lxml")
# 객체에서 원하는 조건에 맞는 첫 번째 요소를 찾을 수 있습니다.(클래스가 "notify_area")인 요소를 찾습니다.
# print(soup.find(attrs={"class" : "notify_area"}))

# CSS 선택자로 요소 검색
# print(soup.select('div.atcmp_footer'))

# 속성으로 요소 검색 
a_tag = soup.find_all('a', href=True)
for val in a_tag :
    print(val.text)


# id로 검색하기 
print(soup.select_one("#topAsideArea"))