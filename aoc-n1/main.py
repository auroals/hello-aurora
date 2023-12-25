def read_and_print_file(file_path):
    with open(file_path, 'r') as file:
        # Read each line and print it
        sum = 0
        for line in file:
            sum = sum+find_number(line.strip())
            print(sum)

def find_number(line):
    print(line)
    first = find_first_number(line)
    last = find_last_number(line)
    together = first + last
    return int(together)

def find_first_number(line):
    number_list = ["0","1","2","3","4","5","6","7","8","9"]
    for char in line:
        print(char)
        if char in number_list:
            return char


def find_last_number(line):
    reversed_string = line[::-1]
    last_number = find_first_number(reversed_string)
    return last_number

# Example usage:
file_path = 'input.txt'  # Replace with the actual file path
read_and_print_file(file_path)
