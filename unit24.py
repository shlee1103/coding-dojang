# 문자열 응용하기

# replace('바꿀문자열', '새문자열') : 문자열 안의 문자열을 다른 문자열로 바꿈
print('Hello, world!'.replace('world', 'Python'))


# translate : 문자열 안의 문자를 다른 문자로 바꿈
# str.maketrans('바꿀문자', '새문자') --> 변환 테이블 생성
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

# 구분자 문자열과 문자열 리스트 연결하기
# join(리스트) : 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듦
# ' '에 join을 사용하여 각 문자열 사이에 공백이 들어가도록 함
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# 소문자 -> 대문자 : upper
# 대문자 -> 소문자 : lower
# 왼쪽 공백 삭제 : lstrip()
# 오른쪽 공백 삭제 : rstrip()
# 양쪽 공백 삭제 : strip()
# 문자열을 왼쪽으로 정렬 : ljust(길이) 
# 문자열을 왼쪽으로 정렬 : rjust(길이) 