from collections import deque
#
#
#
# # 스택
# arr = []
#
# arr.append('a')
# arr.append('b')
# arr.append('c')
#
# print(arr)
# print(arr.pop())
#
#
# # 힙
# arr2 = []
#
# arr2 = deque(arr2)
#
# arr2.append('a')
# arr2.append('b')
# arr2.append('c')
#
# print(arr2)
# print(arr2.popleft())



# def DFS(graph, root, visited):
#     visited[root] = True
#     print(root, end=' ')
#     for i in graph[root]:
#         if not visited[i]:
#             DFS(graph, i, visited)
#

# DFS(graph_list, 3, visited)
visited = [False] * 9
graph_list = [[],
              [2, 3, 8],
              [1, 7],
              [1, 4, 5],
              [3, 5],
              [3, 4],
              [7],
              [2, 6, 8],
              [1, 7]
              ]
def BFS(graph, root, visited):
    hip = deque([root])
    visited[root] = True

    while hip:
        print(hip)
        pick = hip.popleft()
        print(pick,end=' ')
        for i in graph[pick]:
            if not visited[i]:
                hip.append(i)
                visited[i] = True

BFS(graph_list, 1, visited)








