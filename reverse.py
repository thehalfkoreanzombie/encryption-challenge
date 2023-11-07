def read_and_reverse(input_file):
    f = open(input_file, "r")
    secret_message = f.read()
    #print(secret_message)
    f.close()
    reverse = secret_message[::-1]
    return reverse

#read_and_reverse("/Users/kairo/repos/encryption_challenge/encryption/secret_message.txt")

def write_to_file(input_file, output_file):
    f = open(output_file, "w")
    write_file = read_and_reverse(input_file)
    f.write(write_file)

#write_to_file("/Users/kairo/repos/encryption_challenge/encryption/secret_message.txt", "/Users/kairo/repos/encryption_challenge/encryption/reverse_message.txt")