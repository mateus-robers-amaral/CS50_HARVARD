from twttr import shorten
import sys


def main():
    test_shorten()
    sys.exit(0)


def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('Twitter10') == 'Twttr10'
    assert shorten('!?.,') == '!?.,'


if __name__ == "__main__":
    main()
