class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._mute = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """Toggle the power status of the TV."""
        self._status = not self._status

    def mute(self):
        """Toggle the mute status of the TV."""
        if self._status:
            self._mute = not self._mute

    def channel_up(self):
        """Increase the channel by 1. Wrap around to MIN_CHANNEL if at MAX_CHANNEL."""
        if self._status:
            if self._channel < Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self):
        """Decrease the channel by 1. Wrap around to MAX_CHANNEL if at MIN_CHANNEL."""
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Increase the volume by 1. Cap at MAX_VOLUME."""
        if self._status:
            if self._mute:
                self._mute = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the volume by 1. Cap at MIN_VOLUME."""
        if self._status:
            if self._mute:
                self._mute = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Return the TV status as a string in the format: Power = [status], Channel = [channel], Volume = [volume]."""
        return f"Power = {'True' if self._status else 'False'}, Channel = {self._channel}, Volume = {self._volume}"