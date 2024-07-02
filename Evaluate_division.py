class Solution(object):
    def calcEquation(self, equations, values, queries):

        def simplify(equation: list[str]):
            for letter in equation[0]:
                if letter in equation[1]:
                    equation[0] = equation[0].replace(letter, '')
                    equation[1] = equation[1].replace(letter, '')
            return equation

        def is_simple(ls: list):
            if len(ls[0]) != 1 or len(ls[1]) != 1:
                return False
            return True

        edges = {}
        for i in range(len(equations)):
            if not is_simple(equations[i]):
                equations[i] = simplify(equations[i])
            nominator = equations[i][0]
            denominator = equations[i][1]
            if nominator not in edges:
                edges[nominator] = []
            if denominator not in edges:
                edges[denominator] = []
            edges[nominator].append((denominator, values[i]))
            edges[denominator].append((nominator, 1 / values[i]))

        result = 1

        def dfs(source: str, dest: str, vis):
            if source not in edges or dest not in edges:
                return -1
            if source == dest:
                return 1
            vis[source] = True
            for neighbor in edges[source]:
                if neighbor[0] == dest:
                    return neighbor[1]
            for neighbor in edges[source]:
                if not vis[neighbor[0]]:
                    if neighbor[0] == dest:
                        return neighbor[1]
                    else:
                        return neighbor[1] * dfs(neighbor[0], dest, vis)

            return 1



        res = []
        for query in queries:
            if not is_simple(query):
                query = simplify(query)
            visited = {key: False for key in edges}
            res.append(dfs(query[0], query[1], visited))

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.calcEquation(equations=[["a","b"],["b","c"],["bc","cd"]], values=[1.5, 2.5, 5.0],
                           queries=[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
