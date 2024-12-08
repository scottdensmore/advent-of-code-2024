def calculate_multiplications(filename):
  """Calculates the sum of products from valid mul instructions.

  Args:
    filename: The name of the file containing the corrupted memory.

  Returns:
    The sum of products from valid mul instructions.
  """

  total_product = 0

  with open(filename, 'r') as f:
    input_string = f.read()
    i = 0
    while i < len(input_string):
        if input_string[i:i+3] == "mul":

            # Check for valid parentheses and numbers
            start_index = i + 3
            end_index = start_index
            while end_index < len(input_string) and input_string[end_index] != ')':
                end_index += 1

            if end_index < len(input_string) and input_string[start_index] == '(' and input_string[end_index] == ')':
                numbers = input_string[start_index+1:end_index].split(',')
                if len(numbers) == 2 and all(num.isdigit() for num in numbers):
                    num1, num2 = int(numbers[0]), int(numbers[1])
                    total_product += num1 * num2
        i += 1

    return total_product

filename = 'input.txt'
result = calculate_multiplications(filename)
print(result)