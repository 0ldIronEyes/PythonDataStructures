def reverse_vowels(s):
    """Reverse vowels in a string.
	
    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.
	
    >>> reverse_vowels("Hello!")
    'Holle!'
	
    >>> reverse_vowels("Tomatoes")
    'Temotaos'
	
    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'
	
    reverse_vowels("aeiou")
    'uoiea'
	
    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    ls = list(s)
	
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    startingendindex= len(ls) -1
    switchletterA = ""
    switchletterB = ""
    for index in range(len(ls) // 2):
        if vowels.count(s[index]) > 0:
            switchletterA = ls[index]
            for i in range(startingendindex)[::-1]:
                if vowels.count(ls[i]) > 0:
                    switchletterB = ls[i]
                    startingendindex = i
                    ls[i] = switchletterA
                    ls[index] = switchletterB
                    break

    return ("".join(ls))