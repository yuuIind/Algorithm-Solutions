def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for list in lists:
        result = append(result, list)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    len = 0
    for item in list:
        len += 1
    return len
    

def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
