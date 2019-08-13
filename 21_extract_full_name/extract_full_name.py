def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    result = []
    
    for lst in names:
        x = ''
        for name in lst.values():
            x += ' ' + name 
        x = x[1:]    
        result.append(x)
    return result

names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
]
        
extract_full_names(names)
