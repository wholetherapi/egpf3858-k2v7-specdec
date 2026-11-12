from specdec import draft


def test_import():
    assert draft.Config().seed == 0
