s = input('please enter a string: ')

if s.isnumeric() == True:
    print(s)
    s = int(s)
    print(type(s))
elif s.startswith('[') and s.endswith(']'):
    print(s)
    s = list(s)
    print(type(s))
else:
    print(s)
    print(type(s))