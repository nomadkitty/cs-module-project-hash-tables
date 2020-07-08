import re


def word_count(s):
    # Your code here
    words = {}
    new_s = re.sub(r'[^A-Za-z0-9\' ]+', ' ', s).lower()
    list_s = new_s.split(" ")
    # print(new_s)
    # print(list_s)
    for word in list_s:
        if word == '':
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
