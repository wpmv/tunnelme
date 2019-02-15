"""Tests to ensure that the pytest setup is correct."""


def test_universe():
    """Ensure that math is not broken."""
    assert 2 + 2 == 4


def test_fixtures(sample_fixture):
    """Ensure that equality is not broken."""
    assert sample_fixture == sample_fixture
