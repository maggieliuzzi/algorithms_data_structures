"""
Find first recurrent character in a list

Could be many recurrent ones, but we want the first from left to right
If none, return None

Brute force: nested loop comparing every item with all subsequent ones (second loop starting at i+1, not 1!) (Time: O(n^2), Space: O(1)) - This method also returns the first instance of the first recurring value
Another bad one: storing all previous values in an array (even if repeated), and looping through all of them every time we move to a new item in the original list
"""

def first_recurrent_item(input_list):  # Time: O(n), but space: O(n) - Returns second instance of first recurring value

    if type(input_list) != list or len(input_list) < 2:
        return None

    seen_items = {}
    for item in input_list:
        if item in seen_items:
            return item
        else:
            seen_items[item] = None
        
    return None


input_list = [1, 3, 3, 1, 4, 2, 5]
# input_list = []
# input_list = 1
# input_list = [3]
# input_list = [2, 1]
print(first_recurrent_item(input_list))


def brute_force(input_list):
    for i in input_list:
        for j in range(i+1, len(input_list)):
            if i == input_list[j]:
                return i
    return None

def brute_force2(input_list):
    for i in range(1, len(input_list)):
        for j in range(0, i):
            if input_list[i] == input_list[j]:
                return input_list[i]
    return None

print(brute_force(input_list))
print(brute_force2(input_list))
