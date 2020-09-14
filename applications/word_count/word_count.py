def word_count(s):
    cache = {}
    for w in s.split():
        w = w.lower()
        p = '":;,.+-=\//|{}[]()^*&'
        for c in w:
            if c in p:
                w = w.replace(c, "")
        if w in cache:
            cache[w] += 1
        elif w != '':
            cache.update({w: 1})
    print(f'Cache: {cache}')
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))