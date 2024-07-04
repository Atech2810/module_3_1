calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    return ((len(string), string.upper(), string.lower()))
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
       return True
    else:
       return False
print(string_info('Wheel of Fortune'))
print(string_info('London is the capital of Great Britain'))
print(is_contains('book', ['book', 'Alice', 'mirror']))
print(is_contains('death', ['deadly', 'dead end', 'dreadful']))
print(calls)
