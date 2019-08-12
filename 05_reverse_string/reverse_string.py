def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    letters = list(phrase)
    letters.reverse()
    result = ''.join(letters)
    return result

