calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    new_list_to_search = [x.upper() for x in list_to_search]
    if string.upper() in new_list_to_search:
        return True
    else:
        return False

print(string_info('Madrid'))
print(string_info('Barcelona'))
print(is_contains('Anna', ['Ant', 'aNNa', 'BanAna']))
print(is_contains('Sara', ['saHaRa', 'Sar', 'ART']))
print(calls)
