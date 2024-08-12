
def romanToInt(str):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D'  : 500,
        'M' : 1000
    }
    sum = 0
    string_length = len(str)
    character = 0

    while character < string_length:
        if character < string_length - 1  and roman[str[character]] < roman[str[character+1]]:
            sum += roman[str[character + 1]] -  roman[str[character]]
            character += 2
        else:
            sum += roman[str[character]]
            character += 1
    
    return sum


# Time complexity : O(n)
#Space complexity : O(1)
romanToInt("MCMXCIV")