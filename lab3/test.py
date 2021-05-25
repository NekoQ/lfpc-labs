def new_split(string):
    splitted = []
    old_s = ''
    for s in string:
        if s.isdigit():
           old_s += s
        else:
            splitted.append(old_s)
            old_s = s
    splitted.remove('')
    splitted.append(old_s)
    return splitted

print(new_split("ba"))
print('test')

def test():
    return None

if test():
    pass
else:
    print("null")
