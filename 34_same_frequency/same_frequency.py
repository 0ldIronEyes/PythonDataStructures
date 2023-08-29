def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    str1 = []
    str2 = []
    for letr in str(num1):
        str1.append(int(letr))
    str1.sort()
    for letrrs in str(num2):
        str2.append(int(letrrs))
    str2.sort()
    return str1 == str2