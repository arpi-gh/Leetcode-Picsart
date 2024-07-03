import heapq


class Solution(object):

    def networkDelayTime(self, times, n, k):
        sources = {node: [] for node in range(1, n + 1)}
        reached = set()
        delay = {node: 1000 for node in range(1, n + 1)}

        for s, d, c in times:
            sources[s].append((c, d))
        pq = [(0, k)]
        delay[k] = 0

        while pq:
            cur_w, cur_node = heapq.heappop(pq)
            if cur_w > delay[cur_node]:
                continue

            reached.add(cur_node)

            for weight, neighbor in sources[cur_node]:
                if neighbor not in reached:
                    new_delay = cur_w + weight
                    if new_delay < delay[neighbor]:
                        delay[neighbor] = new_delay
                        heapq.heappush(pq, (new_delay, neighbor))

        if len(reached) != n:
            return -1
        return max(delay.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.networkDelayTime(
        times=[[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
               [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
               [3, 1, 36], [2, 3, 59]], n=5, k=5))
