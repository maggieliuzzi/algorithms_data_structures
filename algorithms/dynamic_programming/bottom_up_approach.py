"""
Bottom Up Approach
"""

def fibonacci_bottom_up(n):  # Time Complexity: O(n), Space Complexity: O(n) (new variable)
    answer = [0, 1]
    if len(answer) > n:
        return answer[n]
    for i in range(2, n + 1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[n]  # return answer.pop()


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
print(fibonacci_bottom_up(0))  # 0
print(fibonacci_bottom_up(1))  # 1
print(fibonacci_bottom_up(2))  # 1
print(fibonacci_bottom_up(3))  # 2
print(fibonacci_bottom_up(4))  # 3
print(fibonacci_bottom_up(5))  # 5
print(fibonacci_bottom_up(6))  # 8
