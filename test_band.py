import pytest

from band import Band, Musician, Drummer, Guitarist, Bass

def test_play_solo():
    assert 'all for one, one for all' == Band.get_play_solo()

def test_leader_is_instance_of_correct_class():
    leader = Guitarist('Nick Hipa')
    assert isinstance(leader, Guitarist)


def test_leader_is_instance_of_parent_class(leader):
    assert isinstance(leader, Guitarist)

def test_leader_name():
    leader = Guitarist('Nick Hipa')
    assert leader.name == 'Nick Hipa'

def test_create_Band_from_data():
    data = Band = Band.create_from_data(data)

@pytest.fixture()
def leader():
    return Guitarist('Nick Hipa')

@pytest.fixture(autouse=True)
def clean():
    Band.all = []