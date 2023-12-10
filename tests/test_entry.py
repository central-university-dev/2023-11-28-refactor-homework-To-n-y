from pathlib import Path
from renamer.var_renamer import rename_variable
from renamer.func_renamer import rename_function
from renamer.class_renamer import rename_class


def test_var():
    got = rename_variable(
        Path('tests/fixtures/source/var.py').read_text(),
        'var',
        'rav',
    )

    assert got == Path('tests/fixtures/expected/var.py').read_text()


def test_func():
    got = rename_function(
        Path('tests/fixtures/source/func.py').read_text(),
        'func',
        'foo',
    )

    assert got == Path('tests/fixtures/expected/func.py').read_text()


def test_cls():
    got = rename_class(
        Path('tests/fixtures/source/cls.py').read_text(),
        'func',
        'foo',
    )

    assert got == Path('tests/fixtures/expected/cls.py').read_text()
