print("구구단 몇 단을 계산할까요(1~9)?")
user_input = 1;
while(user_input):
    user_input = int(input())
    if not( 1<=user_input & user_input <=9):
        print("잘못입력하셨습니다. 다시 입력하세요")
    else:
        print("구구단",user_input,"단을 계산합니다.")
        for i in range(1,10):
            result = i * user_input
            print(user_input,"X",i,"=",result)
    print("구구단 몇 단을 계산할까요(1~9)?")
print("구구단 게임을 종료합니다.")
