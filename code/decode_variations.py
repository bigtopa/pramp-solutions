"""
Decode Variations

A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.


input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.

"""


# Recursive
# O(n), O(n)
def decodeVariations(S):
  def dfs(i):
    if i == len(S):
      return 1
    if i in memo:
      return memo[i]
    
    count = 0
    if 1 <= int(S[i]) <= 9:
      count += dfs(i+1)
    if 10 <= int(S[i:i+2]) <= 26:
      count += dfs(i+2)
    memo[i] = count
    return count
    
  memo = {}
  return dfs(0)


# Iterative (DP)
# O(n), O(1)
def decodeVariations(S):
  if not S or S[0] == "0":
    return 0
  
  prev = 1
  curr = 1
  
  for i in range(1, len(S)):
    temp = curr
    if S[i] == "0":
      if S[i-1] == "1" or S[i-1] == "2":
        curr = prev
      else:
        return 0
    elif 10 <= int(S[i-1:i+1]) <= 26:
      curr += prev
    prev = temp
    
  return curr

        