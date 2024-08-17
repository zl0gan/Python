import pytest
from television import Television


def test_mute():
    tv = Television()

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


def test_channel_up():
    tv = Television()

    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()