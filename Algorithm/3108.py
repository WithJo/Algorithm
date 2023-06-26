from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
MAX = 2001

n = int(input())

points = [list(map(lambda x:int(x)*2+1000, input().split())) for _ in range(n)]

board = [[0]*MAX for _ in range(MAX)]

def solv():
    set_border()
    visited = [[False]*MAX for _ in range(MAX)]

    answer = 0
    #시작점에서 BFS갈 수 있는 모든 도형을 가본다. BFS가 몇번 호출되는지 구하는 문제
    for x1,y1,x2,y2 in points:
        if not visited[x1][y1]:
            bfs(x1,y1,visited)
            answer += 1
    answer += -1 if board[1000][1000] != 0 else 0 #원점에 걸쳐 있다면 -1을 해줘야함
    print(answer)


def bfs(sx,sy,visited):
    global board

    q = deque([(sx,sy)])
    visited[sx][sy] = True
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, visited):
                visited[nx][ny] = True
                q.appendleft((nx,ny))

#갈 수 있는 곳이면 True 반환 이미 갔던 곳은 False반환
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= MAX or y >= MAX:
        return False
    elif board[x][y] == 0:
        return False
    elif visited[x][y]:
        return False
    return True

#보드에 입력된 사각형들을 1로 그리는 함수
def set_border():
    global board

    idx = 1
    for x1,y1,x2,y2 in points:
        for y in range(y1,y2+1):
            board[x1][y] = board[x2][y] = idx
        for x in range(x1,x2+1):
            board[x][y1] = board[x][y2] = idx

solv()