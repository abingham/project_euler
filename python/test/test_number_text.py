from euler.lib.number_text import number_text


def test_zero():
    assert number_text(0) == 'zero'


def test_one():
    assert number_text(1) == 'one'


def test_13():
    assert number_text(13) == 'thirteen'


def test_forty():
    assert number_text(40) == 'forty'


def test_69():
    assert number_text(69) == 'sixty-nine'


def test_310():
    assert number_text(310) == 'three hundred and ten'


def test_487():
    assert number_text(487) == 'four hundred and eighty-seven'


def test_800():
    assert number_text(800) == 'eight hundred'


def test_3000():
    assert number_text(3000) == 'three thousand'


def test_12345():
    assert number_text(12345) == 'twelve thousand three hundred and forty-five'
