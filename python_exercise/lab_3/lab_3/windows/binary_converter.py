print("2진수로 변환할 10진수를 입력하시오")
user_input = int(input())
result =""
while user_input>0:
    remainder = user_input % 2
    user_input = user_input // 2
    result = str(remainder) + result
print(result)
