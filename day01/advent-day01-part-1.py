def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists of numbers.

    Args:
      left_list: The first list of numbers.
      right_list: The second list of numbers.

    Returns:
      The total distance between the two lists.
    """
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance

# Example usage with your provided lists (replace with your actual input)
def calculate_total_distance_from_file(filename):
    """
    Reads two lists of numbers from a file and calculates the total distance between them.

    Args:
      filename: The name of the file containing the lists.

    Returns:
      The total distance between the two lists.
    """
    left_list = []
    right_list = []
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return calculate_total_distance(left_list, right_list)

# Example usage (replace 'input.txt' with your actual file name)
filename = 'input.txt'
total_distance = calculate_total_distance_from_file(filename)
print(total_distance)