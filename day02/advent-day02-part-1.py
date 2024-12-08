def is_safe_report(report):
    """Checks if a report is safe.

    Args:
        report: A list of integers representing the levels in a report.

    Returns:
        True if the report is safe, False otherwise.
    """

    direction = None  # None for initial state, 1 for increasing, -1 for decreasing
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff == 0:
            return False  # No increase or decrease
        if direction is None:
            direction = 1 if diff > 0 else -1
        elif direction * diff <= 0:
            return False  # Change in direction or no change
        if abs(diff) > 3:
            return False  # Difference too large
    return True

def count_safe_reports(filename):
    """Counts the number of safe reports in a file.

    Args:
        filename: The name of the file containing the reports.

    Returns:
        The number of safe reports.
    """

    count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = [int(num) for num in line.strip().split()]
            if is_safe_report(report):
                count += 1
    return count

filename = 'input.txt'
safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports}")