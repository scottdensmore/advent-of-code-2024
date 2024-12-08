def find_mas_x_pattern_count(word_search):
    grid = [list(row) for row in word_search]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    count = 0

    for r in range(rows - 2):
        for c in range(cols - 2):
            center = grid[r+1][c+1]
            if center != 'A':
                continue

            # Extract corners
            top_left = grid[r][c]
            top_right = grid[r][c+2]
            bottom_left = grid[r+2][c]
            bottom_right = grid[r+2][c+2]

            # Check all four patterns:
            # Pattern 1
            # M . S
            # . A .
            # M . S
            if (top_left == 'M' and top_right == 'S' and
                bottom_left == 'M' and bottom_right == 'S'):
                count += 1
            # Pattern 2 (180° rotation)
            # S . M
            # . A .
            # S . M
            elif (top_left == 'S' and top_right == 'M' and
                  bottom_left == 'S' and bottom_right == 'M'):
                count += 1
            # Pattern 3 (90° rotation)
            # M . M
            # . A .
            # S . S
            elif (top_left == 'M' and top_right == 'M' and
                  bottom_left == 'S' and bottom_right == 'S'):
                count += 1
            # Pattern 4 (270° rotation)
            # S . S
            # . A .
            # M . M
            elif (top_left == 'S' and top_right == 'S' and
                  bottom_left == 'M' and bottom_right == 'M'):
                count += 1

    return count

def count_diagonal_mas_from_file(filename):
  """
  Counts the number of occurrences of "XMAS" in a word search from a file.

  Args:
      filename: The name of the file containing the word search.

  Returns:
      An integer representing the number of times "XMAS" appears.
  """

  with open(filename, 'r') as f:
    word_search = [line.strip() for line in f.readlines()]

  return find_mas_x_pattern_count(word_search)

# Example usage
filename = "input.txt"  # Replace with your file name
count = count_diagonal_mas_from_file(filename)
print("Number of X-MAS patterns:", count)

# # Example usage with your puzzle
# word_search = [
#     ".M.S......",
#     "..A..MSMS.",
#     ".M.S.MAA..",
#     "..A.ASMSM.",
#     ".M.S.M....",
#     "..........",
#     "S.S.S.S.S.",
#     ".A.A.A.A..",
#     "M.M.M.M.M.",
#     ".........."
# ]

# print(find_mas_x_pattern_count(word_search))
