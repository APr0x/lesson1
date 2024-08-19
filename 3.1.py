calls = 0


def count_calls():
    global calls
    calls += 1
    print(calls)
def string_ifno():
        string1 = input('Call Your City: ')
        string2 = input('Call Your Name: ')
        print ((len(string1), string1.upper(), string1.lower()))
        print((len(string2), string2.upper(), string2.lower()))
        count_calls()
string_ifno()
def is_contains():
    list_to_search = 0
    string1 = ('Batman')
    string1_low = string1.lower()
    string2 = ('Wolverine')
    string2_low = string2.lower()
    list1 = ['Man', 'BATmAN', 'Woman']
    list1st = str(list1)
    list1_low = list1st.lower()
    list2 = ['Cyclops', 'Rouge', 'Jubelee']
    list2st = str(list2)
    list2_low = list2st.lower()

    for i in string1_low:
        for j in list1_low:
            if i == j:
                list_to_search = 1
                break
    if list_to_search == 1:
        print(True)
    else:
        print(False)
    for i in string2_low:
        for j in list2_low:
            if i == j:
                list_to_search = 1
                break
    if list_to_search == 1:
        print(True)
    else:
        print(False)

count_calls()
is_contains()
