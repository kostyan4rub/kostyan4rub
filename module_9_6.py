def all_variants(text):
    len_ = len(text)
    for y in range(len_):
        for i in range(len_):
            yield text[i:i+y+1]
        len_ = len_ - 1

a = all_variants("abc")
for i in a:
    print(i)
print()

