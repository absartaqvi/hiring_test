"""The goal of this test is to merge dict1 into dict2 recursively. The solution should work for any
dict with values that are comprised of strings, dicts and lists."""


dict1 = {
    'top_level_key1': {
        'level_1_key_1': 'level_1_value_2',
        'level_1_key_2': {
            'level_2_key_1': {
                'level_3_key_1': ['value1', 'value2', 'value3'],
                'level_3_key_2': {'key1': 'value1', 'key2': 'value2'}
            }
        }
    },
    'top_level_key2': ['value1', 'value2', 'value3']
}

dict2 = {
    'top_level_key1': {
        'level_1_key_4': 'level_1_value_4',
        'level_1_key_2': {
            'level_2_key_1': {
                'level_3_key_1': ['value1', 'value4', 'value5'],
                'level_3_key_2': {'key3': 'value3', 'key4': 'value4'},
                'level_3_key_3': 'value4'
            }
        }
    },
    'top_level_key2': ['value1', 'value2', 'value3', 'value4'],
    'top_level_key3': 'value3'
}

expected_result = {
    'top_level_key1': {
        'level_1_key_1': 'level_1_value_2',
        'level_1_key_2': {
            'level_2_key_1': {
                'level_3_key_1': ['value1', 'value2', 'value3', 'value4', 'value5'],
                'level_3_key_2': {'key1': 'value1', 'key2': 'value2',
                                  'key3': 'value3', 'key4': 'value4'},
                'level_3_key_3': 'value4'
            }
        },
        'level_1_key_4': 'level_1_value_4', # This was missing from the initial expected_result dict.
    },
    'top_level_key2': ['value1', 'value2', 'value3', 'value4'],
    'top_level_key3': 'value3'

}

import copy

def merge_dicts(input_dict1, input_dict2):
    """This function recursively merges the two input dicts and returns the result"""
    # We don't want to mutate any of the existing dicts, so make a copy.
    new = copy.deepcopy(input_dict1)
    def _merge(new, input_dict2):
        for k in input_dict2:
            if k in new:
                if isinstance(new[k], dict) and isinstance(input_dict2[k], dict):
                    _merge(new[k], input_dict2[k])
                elif isinstance(new[k], list) and isinstance(input_dict2[k], list):
                    new[k].extend(input_dict2[k])
                    new[k] = sorted(set(new[k]))
            else:
                new.update({k: input_dict2[k]})
        return new
    return _merge(new, input_dict2)


def main():
    result = merge_dicts(dict1, dict2)
    assert result == expected_result


if __name__ == '__main__':
    main()
