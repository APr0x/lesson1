calls = 0


def count_calls():
    global calls
    calls += 1
count_calls()
def string_ifno(s1):
        a = (len(s1), s1.upper(), s1.lower())
        return a
    count_calls()
def is_contains(s, l):
    list_to_search = True
    lower_l = []
    for i in l:
        lower_l.append(i.lower())
    if s.lower() in lower_l:
        return list_to_search
    else:
        return False
    count_calls()
    count_calls()
print(string_ifno(s1= 'Ave Dominus Nox'))
print(string_ifno(s1='Big floppa Cat'))
print(is_contains(s="Batman", l=['Wonan', 'Man', 'BATman']))
print(is_contains(s='Wolverine', l=['Jubelee', 'Beast', 'Professor X']))
print(calls)
