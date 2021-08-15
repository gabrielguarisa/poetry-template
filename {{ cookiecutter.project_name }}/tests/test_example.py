from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.example import add, mult


def test_add():
    assert add(1, 2) == 3


def test_mult():
    assert mult(2, 3) == 6
