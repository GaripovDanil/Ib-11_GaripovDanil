str1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
str2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']


def number_in_english(number):
    if not number:
        return 'zero'
    if number // 100 and number % 100:
        result = '{} hundred and '.format(str1[number // 100 - 1])
    elif number // 100:
        result = '{} hundred'.format(str1[number // 100 - 1])
    else:
        result = ''
    if number % 100 <= 19:
        result += str1[number % 100 - 1]
    else:
        result = result.strip()
    return result


print(number_in_english(0).lower())
print(number_in_english(1).lower())
