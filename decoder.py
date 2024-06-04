def decode(message_file):
    with open(message_file, 'r') as file:
        message = file.read()
        decoded_message = decoder(message)
    return decoded_message

def decoder(message):
    decoded_words = []
    expected_num = 1
    
    # Split the message into lines
    lines = message.strip().split('\n')
    
    # Iterate over each line in the message
    for line in lines:
        # Split the line into number and word
        num, word = line.split()
        num = int(num)
        
        # Check if the number matches the expected number
        if num == expected_num:
            decoded_words.append(word)
            expected_num += 1
            
    # Join the decoded words into a single string
    decoded_message = ' '.join(decoded_words)
    return decoded_message

# Example usage:
decoded_message = decode("message_file.txt")
print(decoded_message)
