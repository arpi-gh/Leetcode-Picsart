class Solution(object):
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

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            can_finish[crs] = True
            prereqs[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
