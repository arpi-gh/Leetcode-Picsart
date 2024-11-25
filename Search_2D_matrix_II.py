# Linear Solution
class Solution(object):
    def searchMatrix(self, matrix, target):
        end_row = len(matrix)
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > target:
                end_row = i
                break

        end_col = len(matrix[0])
        for j in range(len(matrix[0])):
            if matrix[0][j] == target:
                return True
            if matrix[0][j] > target:
                end_col = j
                break
        for i in range(end_row):
            for j in range(end_col):
                if matrix[i][j] == target:
                    return True

        return False
#
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         end_row = len(matrix)
#         end_col = len(matrix[0])
#         found = False
#
#         def find_row_range(matrix, target, start, end):
#             nonlocal end_row
#             nonlocal found
#             mid = (start + end) // 2
#             if matrix[mid][0] == target:
#                 found = True
#                 return
#             if start == mid:
#                 if matrix[end][0] > target:
#                     end_row = end
#                 elif matrix[start][0] > target:
#                     end_row = start
#                 return
#             if start == end:
#                 if matrix[start][0] > target:
#                     end_row = start
#             if matrix[mid][0] > target:
#                 end_row = mid
#                 find_row_range(matrix, target, start, end=mid - 1)
#             else:
#                 find_row_range(matrix, target, start=mid + 1, end=end)
#
#         def find_col_range(first_row, target, start, end):
#             nonlocal end_col
#             nonlocal found
#             mid = (start + end) // 2
#             if first_row[mid] == target:
#                 found = True
#                 return
#             if start == mid:
#                 if first_row[end] > target:
#                     end_col = end
#                 elif first_row[start] > target:
#                     end_col = start
#                 return
#             if start == end:
#                 if first_row[start] > target:
#                     end_col = start
#             if first_row[mid] > target:
#                 end_col = mid
#                 find_col_range(first_row, target, start, end=mid - 1)
#             else:
#                 find_col_range(first_row, target, start=mid + 1, end=end)
#
#         find_row_range(matrix, target, start=0, end=len(matrix))
#         if found:
#             return True
#
#         f_row = matrix[0]
#         find_col_range(f_row, target, start=0, end=len(f_row))
#
#         if found:
#             return True
#
#         for i in range(end_row):
#             for j in range(end_col):
#                 if matrix[i][j] == target:
#                     return True
#
#         return False


if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(sol.searchMatrix(mat, 20))