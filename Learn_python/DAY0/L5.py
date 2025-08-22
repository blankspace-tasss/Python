def count_even(arr, left, right):
    if left == right:  # Base case: single element
        return 1 if arr[left] % 2 == 0 else 0

    mid = (left + right) // 2  # Correct integer division

    left_count = count_even(arr, left, mid)
    right_count = count_even(arr, mid + 1, right)

    return left_count + right_count


arr = [2, 4, 6, 7, 8, 10]
result = count_even(arr, 0, len(arr) - 1)
print("Number of even numbers:", result)
