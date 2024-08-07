calls = 0
str = input('Введите строку:')
lst = list(input('Введите список:').split())


def count_calls():
    global calls
    calls += 1


def string_info(string):
    a = (len(string), string.lower(), string.upper())
    print(a)
    count_calls()


def is_contains(string, list_to_search):
    b = string in list_to_search
    print(b)
    count_calls()


string_info(str)
is_contains(str,lst)
string_info(str)
is_contains(str,lst)

print(f'функции вызывали {calls} раз')
