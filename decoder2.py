def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    message = ''
    line_number = 1
    max_number = 0

    for line in lines:
        number, word = line.split()
        number = int(number)

        if number > max_number:
            max_number = number
            message += word + ' '

        if number == line_number * (line_number + 1) // 2:
            line_number += 1

    return message.strip()  # Remove the trailing space

# Example usage:
decoded_message = decode("message_file.txt")
print(decoded_message)
