# import heapq
#
#
# class Solution(object):
#     def findCheapestPrice(self, n, flights, src, dst, k):
#         sources = {node: [] for node in range(n)}
#         price = {node: 10 ** 5 for node in range(n)}
#         for s, d, t in flights:
#             sources[s].append((t, d))
#
#         pq = [(0, src, 0)]
#         found = []
#
#         while pq:
#             cur_price, cur_stop, cur_level = heapq.heappop(pq)
#
#             level = cur_level + 1
#
#             for pr, neighbor in sources[cur_stop]:
#                 new_price = cur_price + pr
#                 if neighbor != dst:
#                     if new_price < price[neighbor]:
#                         price[neighbor] = new_price
#                         heapq.heappush(pq, (new_price, neighbor, level))
#                 else:
#                     if level - 1 < k:
#                         heapq.heappush(found, (new_price, neighbor, level))
#
#         if found:
#             cost, destination, level = heapq.heappop(found)
#             return cost
#         return -1

# import heapq
#
#
# class Solution(object):
#     def findCheapestPrice(self, n, flights, src, dst, k):
#         sources = {node: [] for node in range(n)}
#         for s, d, c in flights:
#             sources[s].append((d, c))
#         visited = [False] * n
#         pq = []
#
#         def dfs(i, dest, cost, stops):
#             if i == dest:
#                 if stops <= k:
#                     heapq.heappush(pq, cost)
#                 return
#             visited[i] = True
#
#             for neighbor, price in sources[i]:
#                 if visited[neighbor]:
#                     continue
#                 cost += price
#                 stops += 1
#                 dfs(neighbor, dest, cost, stops)
#                 cost -= price
#                 stops -= 1
#                 visited[neighbor] = False
#
#         dfs(src, dst, cost=0, stops=-1)
#         if pq:
#             return heapq.heappop(pq)
#         return -1


from collections import deque


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        sources = {node: [] for node in range(n)}
        for s, d, c in flights:
            sources[s].append((d, c))

        prices = {node: float('inf') for node in range(n)}
        prices[src] = 0

        q = deque([(src, 0, 0)])

        while q:
            current, cost, stops = q.popleft()

            if stops <= k:
                for neighbor, flight_cost in sources[current]:
                    new_cost = cost + flight_cost
                    if new_cost < prices[neighbor]:
                        prices[neighbor] = new_cost
                        q.append((neighbor, new_cost, stops + 1))

        return prices[dst] if prices[dst] < float('inf') else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
