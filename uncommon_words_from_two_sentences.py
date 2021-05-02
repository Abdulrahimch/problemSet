def uncommon_words_two_sentences(a, b):
    c = (a + ' ' + b).split()
    result = []
    for i in c:
        if c.count(i) == 1:
            result.append(i)

    return result

A, B = "this apple is sweet", "this apple is sour"
D, F = 'lets try another easy example', 'the other example is easy'
print(uncommon_words_two_sentences(A, B))
print(uncommon_words_two_sentences(D, F))

