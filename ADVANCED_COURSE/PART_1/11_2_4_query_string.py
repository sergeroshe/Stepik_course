def build_query_string(input_dict):
    result_list = sorted([f'{k}={v}' for k, v in input_dict.items()])
    result_string = '&'.join(result_list)
    return result_string
