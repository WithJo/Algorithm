'''
    시각
    
    정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.
    예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다
    00시 00분 03초
    00시 13분 30초

     반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다
    00시 02분 55초
    01시 27분 45초

'''

s_m = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
h = [3,13,23]

n = int(input())

hour = 0
minute = 0
sec = 0
count=0


while hour!=n or minute!=59 or sec!=59:
    sec+=1
    if sec==60:
        minute+=1
        sec=0
    if minute==60:
        hour+=1
        minute=0
    if (sec in s_m) or (minute in s_m) or (hour in h):
        count+=1        

print(count)
'''
    # H를 입력받기
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    
    print(count)
'''  
