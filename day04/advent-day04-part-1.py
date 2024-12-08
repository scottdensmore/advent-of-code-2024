def count_xmas(word_search):
  """
  Counts the number of occurrences of "XMAS" in a word search, considering all orientations (forward and backward).

  Args:
      word_search: A list of strings representing the word search grid.

  Returns:
      An integer representing the number of times "XMAS" appears.
  """

  count = 0
  rows, cols = len(word_search), len(word_search[0])

  def check_word(word):
    return word == "XMAS" or word[::-1] == "XMAS"

  # Check horizontally (forward and backward)
  for row in range(rows):
    for col in range(cols - 3):
      if check_word(word_search[row][col:col+4]):
        count += 1

  # Check vertically (forward and backward)
  for col in range(cols):
    for row in range(rows - 3):
      current_word = ""
      for i in range(4):
        current_word += word_search[row+i][col]
      if check_word(current_word):
        count += 1

  # Check diagonally (top-left to bottom-right, forward and backward)
  for row in range(rows - 3):
    for col in range(cols - 3):
      current_word = ""
      for i in range(4):
        current_word += word_search[row+i][col+i]
      if check_word(current_word):
        count += 1

  # Check diagonally (bottom-left to top-right, forward and backward)
  for row in range(3, rows):
    for col in range(cols - 3):
      current_word = ""
      for i in range(4):
        current_word += word_search[row-i][col+i]
      if check_word(current_word):
        count += 1

  return count

def count_xmas_from_file(filename):
  """
  Counts the number of occurrences of "XMAS" in a word search from a file.

  Args:
      filename: The name of the file containing the word search.

  Returns:
      An integer representing the number of times "XMAS" appears.
  """

  with open(filename, 'r') as f:
    word_search = [line.strip() for line in f.readlines()]

  return count_xmas(word_search)

# Example usage
filename = "input.txt"  # Replace with your file name
number_of_xmas = count_xmas_from_file(filename)
print(f"The word 'XMAS' appears {number_of_xmas} times in the word search.")

# # Example usage
# word_search = [
#   "MMMSXXMASM",
#   "MSAMXMSMSA",
#   "AMXSXMAAMM",
#   "MSAMASMSMX",
#   "XMASAMXAMM",
#   "XXAMMXXAMA",
#   "SMSMSASXSS",
#   "SAXAMASAAA",
#   "MAMMMXMMMM",
#   "MXMXAXMASX"
# ]

# number_of_xmas = count_xmas(word_search)
# print(f"The word 'XMAS' appears {number_of_xmas} times in the word search.")