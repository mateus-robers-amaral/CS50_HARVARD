from plates import is_valid

def main():
    test_is_valid_number_of_letters()
    test_is_valid_startnumbers()
    test_is_valid_zero()
    test_is_valid_pontuation()

def test_is_valid_number_of_letters():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGHI') == False

def test_is_valid_startnumbers():
    assert is_valid('AB') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

def test_is_valid_zero():
    assert is_valid('AAA111') == True
    assert is_valid('AAA11A') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50') == True

def test_is_valid_pontuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

if __name__ == '__main__':
    main()
