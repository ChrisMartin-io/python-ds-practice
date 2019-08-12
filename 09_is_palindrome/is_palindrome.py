def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """


    list1 = list(phrase.lower())
    if ' ' in list1:
        list1.remove(' ')
    list2 = list1[0:len(list1)]
    list2.reverse()
    if list1 == list2:
        return True
    else:
        return False

