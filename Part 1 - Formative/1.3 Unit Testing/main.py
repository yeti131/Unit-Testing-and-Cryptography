# DO NOT modify this code!

def reverse_string(text):
    return ''.join([text[i] for i in range(len(text) - 1, -1, -1)])


def split_string(text):
    return text[len(text)//2:] + text[:len(text)//2]


def insert_string(text, insert_text):
    return text[:len(text)//2] + insert_text + text[len(text)//2:]
