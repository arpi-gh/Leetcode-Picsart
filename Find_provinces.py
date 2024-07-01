class Solution(object):
    def findCircleNum(self, isConnected):
        provinces = 0
        visited = [False] * len(isConnected)

        def dfs(v, path):
            visited[v] = True
            for j in range(len(isConnected[v])):
                if isConnected[v][j] and not visited[j]:
                    path.append(j)
                    dfs(j, path)

        for i in range(len(isConnected)):
            if not visited[i]:
                province = []
                province.append(i)
                dfs(i, province)
                provinces += 1

        return provinces


if __name__ == '__main__':
    print(Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
