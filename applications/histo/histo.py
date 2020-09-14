import os.path

robin_text = os.path.join(os.path.dirname(__file__), 'robin.txt')

with open(robin_text) as t:
    words = t.read()

def word_count(s):
    dict = {}
    spec_chars = '" : ; , . - + = / \ | { } [ ] * ^ &'.split()
    s2 = ''.join(c.lower() for c in s if not c in spec_chars)
    for word in s2.split():
        dict[word] = dict[word] + 1 if word in dict else 1
    return dict

def print_histogram(dict):
    sortItems = sorted(dict.items(), key = lambda x: (-x[1], x[0]), reverse=False)
    for i in sortItems:
        print(f"{i[0]:<20} {'#'*i[1]}")

wordCount = word_count(words)
print_histogram(wordCount)


