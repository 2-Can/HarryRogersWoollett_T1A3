from main import count


def test_count():
    assert count == sum(1 for line in open('tally.txt'))