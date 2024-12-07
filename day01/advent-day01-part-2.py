def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score between two lists of numbers.

    Args:
      left_list: The first list of numbers.
      right_list: The second list of numbers.

    Returns:
      The similarity score between the two lists.
    """
    similarity_score = 0
    for left_num in left_list:
        count = right_list.count(left_num)  # Count occurrences in the right list
        similarity_score += left_num * count
    return similarity_score

# Example usage with your provided lists (replace with your actual input)
def calculate_similarity_score_from_file(filename):
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
    return calculate_similarity_score(left_list, right_list)

# Example usage (replace 'input.txt' with your actual file name)
filename = 'input.txt'
similarity_score = calculate_similarity_score_from_file(filename)
print(similarity_score)