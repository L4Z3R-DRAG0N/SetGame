# def set_solver(cards):
#     set = [[] for j in range(4)]
#     for i in range(12):
#         attributeCount = 0
#         for j in range(-11):
#             if cards[i][0]==cards[j][0]
                
                
                
                
#                 attributeCount += 1
        
#         if attributeCount == 4:
#             set[].append()

def solve(cards):
    ans = []
    for i in range(len(cards)):
        for j in  range(len(cards)):
            if i == j:
                break
            for k in range(len(cards)):
                if i == k or j == k:
                    break
                if (
                    (cards[i][0] == cards[j][0] and cards[j][0] == cards[k][0])
                    or (cards[i][1] == cards[j][1] and cards[j][1] == cards[k][1])
                    or (cards[i][2] == cards[j][2] and cards[j][2] == cards[k][2])
                    or (cards[i][3] == cards[j][3] and cards[j][3] == cards[k][3])):
                    if not [i, j, k] in ans:
                        ans.append([i, j, k])
    return ans