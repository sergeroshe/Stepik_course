def merge(dict_list):
    result = {}
    for cur_dict in dict_list:
        for key in cur_dict:
            result.setdefault(key, set()).add(cur_dict[key])

    return result


result_dict = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100},
               {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]

merge(result_dict)