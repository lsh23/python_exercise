user_input = input("구구단 몇 단을 계산 할까요?",end)
print("구구단"+user_input+"단을 계산합니다.")
int_user_input = int(user_input)
for i in range(1,10):
    result = int_user_input * i
    print(int_user_input,"X",i,"=",result)
