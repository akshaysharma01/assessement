def has_pair_with_sum(arr, x):
    # Create an empty set to store seen elements
    seen = set()

    # Traverse through the array
    for num in arr:
        # Calculate the required complement to make the sum x
        complement = x - num

        # If the complement exists in the set, we found a pair
        if complement in seen:
            return True

        # Otherwise, add the current element to the set
        seen.add(num)

    # If no pair is found, return False
    return False

# Example usage:
arr1 = [0, -1, 2, -3, 1]
x1 = -2
print(has_pair_with_sum(arr1, x1))  # Output: True

arr2 = [1, -2, 1, 0, 5]
x2 = 0
print(has_pair_with_sum(arr2, x2))  # Output: False

