from reverse import read_and_reverse
from reverse import write_to_file

def main(input_file, output_file):
    read_and_reverse(input_file)
    write_to_file(input_file, output_file)

main("/Users/kairo/repos/encryption_challenge/encryption/secret_message.txt", "/Users/kairo/repos/encryption_challenge/encryption/reverse_message.txt")