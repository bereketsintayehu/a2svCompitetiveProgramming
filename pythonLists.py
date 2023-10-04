if __name__ == '__main__':
    pList = []
    N = int(input())
    for _ in range(N):
        inp = input().split()
        match inp[0]:
            case 'insert':
                pList.insert(int(inp[1]), int(inp[2]))
            case 'print':
                print(pList)
            case 'remove':
                if int(inp[1]) in pList:
                    pList.remove(int(inp[1]))
            case 'append':
                pList.append(int(inp[1]))
            case 'sort':
                pList.sort()
            case 'pop':
                if len(pList) > 0:
                    pList.pop()
            case 'reverse':
                pList.reverse()
