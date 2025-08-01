class leetcode118:
  #state the rows in number, in integer type
  def generate(self, numRows: int) -> list[list[int]]:
    ans = []
     # i shows the rows(list)
    for i in range(numRows):
      ans.append([1] * (i + 1))
    # append all the rows in existing list
    for i in range(2, numRows):
      for j in range(1, len(ans[i]) - 1):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
# ans show the index of list and sublist
    return ans


