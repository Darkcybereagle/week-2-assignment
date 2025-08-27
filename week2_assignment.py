# Week Two Assignment Solution

# 1. Create an empty list called my_list.
my_list = []

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After step 2:", my_list)

# 3. Insert the value 15 at the second position in the list.
# Note: Python uses 0-based indexing, so second position is index 1
my_list.insert(1, 15)
print("After step 3:", my_list)

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("After step 4:", my_list)

# 5. Remove the last element from my_list.
my_list.pop()  # pop() without index removes the last element
print("After step 5:", my_list)

# 6. Sort my_list in ascending order.
my_list.sort()
print("After step 6:", my_list)

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)

# Final result
print("\nFinal my_list:", my_list)