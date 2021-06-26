class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = {i: graph[i] for i in range(len(graph))}

        target = len(graph) - 1

        visited = [False] * len(graph)

        path = [0]
        q = [[0, path]]
        ans = []
        while q:
            cur, path = q.pop(0)
            for i in dic[cur]:
                # if not visited[i]:
                if i == target:
                    ans.append(path + [i])
                else:
                    q.append([i, path + [i]])

        return ans


