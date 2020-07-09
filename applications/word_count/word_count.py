import re
# caleb's way of doing:
# ignore = re.compile(r'[]":;,.+=/\\|[{}()*^&-]')
# def word_count(s):
#     s = ignore.sub('', s.lower()).split()


def word_count(s):
    # Your code here
    words = {}
    # raw string matching from the start of string, escape \' and repeatedly matching, replancing with space ' '
    new_s = re.sub(r'[^A-Za-z0-9\']+', ' ', s).lower()
    list_s = new_s.split(" ")
    print(new_s)
    print(list_s)
    for word in list_s:
        if word == '':
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count(
    #     'This is a test of the emergency broadcast network. This is only a test.'))
    # print(word_count('a a\ra\na\ta \t\r\n'))
    # print(word_count("Hello    hello"))
