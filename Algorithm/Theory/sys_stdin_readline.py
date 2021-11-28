📌한 개의 정수를 입력받을 때
    import sys
    a = int(sys.stdin.readline())
    😨 그냥 a = sys.stdin.readline() 하면 안되나요?
    👉 sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
    만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
    또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.

📌정해진 개수의 정수를 한줄에 입력받을 때
    import sys
    a,b,c = map(int,sys.stdin.readline().split())
    map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.
    위와 같이 사용한다면 a,b,c에 대해 각각 int형으로 형변환을 할 수 있습니다.

📌 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
    import sys
    data = list(map(int,sys.stdin.readline().split()))
    split()은 문자열을 나눠주는 함수입니다.
    괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눕니다.

    list()는 자료형을 리스트형으로 변환해주는 함수입니다.
    map()은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 list()로 감싸주었습니다.

📌 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
    import sys
    data = []
    n = int(sys.stdin.readline())
    for i in range(n):
        data.append(list(map(int,sys.stdin.readline().split())))
    이렇게 한다면 각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고,
    각각 길이가 다른 2차원 리스트도 입력 받을 수 있습니다.

📌 문자열 n줄을 입력받아 리스트에 저장할 때
    import sys
    n = int(sys.stdin.readline())
    data = [sys.stdin.readline().strip() for i in range(n)]
    strip()은 문자열 맨 앞과 맨 끝의 공백문자를 제거합니다.
    
    👉 입력

    3
    안녕안녕
    나는 지수야
    헬륨가스 마셨더니 이렇게됐지
    👉 출력
    ['안녕안녕', '나는 지수야', '헬륨가스 마셨더니 이렇게됐지']
    
    
    출처 : https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline