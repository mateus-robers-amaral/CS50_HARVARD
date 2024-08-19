from bank import value
def main():
    test_value()

def test_value():
    assert value('hello') == 0
    assert value('HELLO') == 0

    assert value('hi') == 20
    assert value('HI') == 20

    assert value('good morning') == 100
    assert value('GOOD MORNING') == 100

if __name__ == "__main__":
    main()
