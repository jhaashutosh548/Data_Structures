
def simple(path):
    oplist = []
    path = path.split('/')
    for i in path:
        if oplist and i == '..':
            oplist.pop()
        elif i not in ['','.','..']:
            oplist.append(i)
    return '/'+'/'.join(oplist)

print(simple('/home//foo/'))