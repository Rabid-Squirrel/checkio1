def checkio(data: str) -> bool:
    # replace this for solution
    for elem in data:
        print('{}-{}\n'.format(elem,elem.isalpha()))
    #print('data.isdigit(): {} data.isupper() {} data.islower() {} data.isalpha() {} data.isascii() {}'.format(
        #data.isdigit(), data.isupper(), data.islower(),
        #data.isalpha(), data.isascii()))
    result = dict{'digit': elem.isdigit()}
    if len(data) >= 10:
        for elem in data:
            if elem.isdigit() or elem.isupper() or elem.islower() or elem.isalpha() or elem.isascii():
                continue
            else:
                return False
    return True

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio('1a') == False, "0st example"
    # assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
