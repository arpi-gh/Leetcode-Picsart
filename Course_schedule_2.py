class Solution(object):
    def __init__(self):
        self.index = 0
        self.res = []

    def canFinish(self, numCourses, prerequisites):
        prereqs = {key: [] for key in range(numCourses)}
        can_finish = [False] * numCourses
        visited = [False] * numCourses
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        def dfs(crs):
            if visited[crs] and not can_finish[crs]:
                return False
            if len(prereqs[crs]) == 0:
                return True
            visited[crs] = True

            for preq in prereqs[crs]:
                if not dfs(preq):
                    return False
            can_finish[crs] = True
            prereqs[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

    def findOrder(self, numCourses, prerequisites):
        self.index = numCourses - 1
        ordered = [False] * numCourses
        courses = {key: [] for key in range(numCourses)}
        for c, p in prerequisites:
            courses[p].append(c)

        def put_in_order(crs):
            for next_in_order in courses[crs]:
                if not ordered[next_in_order]:
                    put_in_order(next_in_order)
            self.res[self.index] = crs
            self.index -= 1
            ordered[crs] = True

        if self.canFinish(numCourses, prerequisites):
            self.res = [0 for _ in range(numCourses)]
            for course in courses:
                if not ordered[course]:
                    put_in_order(course)

        return self.res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(2, [[0, 1], [1, 0]]))