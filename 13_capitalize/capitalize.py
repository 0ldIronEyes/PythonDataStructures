def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    finalphrase = ""
    finalphrase += phrase[0].upper()
    finalphrase += phrase[1:]
    return finalphrase