a =[10,5,3,9,253,1]
total = 0
for i in a:
    total += i

print('total : ',total)


# [표현식 for 요소 in 시퀀스 (if 조건)]
prices = [132,-5323,423,523,-523,232]
# list 내포
mprices = [i if i>0 else 0 for i in prices]
print('prices : ',prices)
print('mprices : ',mprices)

list1 = [3,4,5]
list2 = [x*2 for x in list1]
print('list1 : ',list1)
print('list2 : ',list2)
n1 = [x for x in range(10) if x%2==0]
n2 = [x*3 for x in range(10) if x%2==0]
print('n1 : ',n1)
print('n2 : ',n2)

fruit = ['apple','banna','tomato','kiwi']
items = [word[0] for word in fruit] #첫글자만 붙이기
print('items : ',items)
result = [len(w) for w in items]
print('result : ',result)


#리스트 내포에 대한 이해
#1) 1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트 내포:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
# 출력: [2, 4, 6, 8, 10]

#2) 문자열 리스트에서 문자열의 길이가 5 이상인 문자열만 선택하는 리스트 내포:
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) >= 5]
print(long_words)
# 출력: ['apple', 'banana', 'cherry', 'elderberry']

# 3) 리스트 내포를 사용하여 각 요소를 제곱하는 예제:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
# 출력: [1, 4, 9, 16, 25]


# 함수
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b

x = add(3,4)
print(x)
y = minus(3,4)
print(y)
z = multiply(x,y)
print(z)

# 함수 인수의 기본값 지정
def say_msg(name, msg='^^'):
    print(name,' : ',msg)

say_msg('hong')
say_msg('jang', 'good job!')


#lambda 함수
is_even = lambda x: x % 2 == 0
print(is_even(3))
print(is_even(2))







