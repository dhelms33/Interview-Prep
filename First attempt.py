# Description: This program will decode a message from a file

def decode(message_file):
    messagefile = []
    current_num = 0
    with open(message_file, 'r') as file:
        message = file.read()
        decoder(message)
def decoder(message):
    for line in lines:
        num, word = line.strip.split()
        num = int(num)
        
        if num == current_num:
            message_words.append(word)
            current_num+=1
    return ' '.join(message_words)
    return message