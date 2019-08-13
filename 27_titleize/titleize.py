def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words_lst = phrase.split(' ')
    lst = []
    result = ''
    for words in words_lst:
        tmp_str = ''
        for idx in range(len(words)):
            
            if idx == 0:
                tmp_str += words[idx].upper()

            else:
                tmp_str += words[idx].lower()

        lst.append(tmp_str)
    
    for idx in range(len(lst)):
        if idx == (len(lst) - 1):
            result += lst[idx]
        else:
            result += lst[idx] + ' '
        
    return result

titleize('this is awesome')
