# Name: dubstep.py
# Author: Robin Goyal
# Last-Modified: July 06, 2018
# Purpose: Decode a dubstep remix into lyrics of the original song


def song_decoder(song):
    """song_decode

    (str) -> str

    Decode a dubstep remix of a song into the original lyrics.
    Before the first word of the song, any number of WUB can exist,
    in between words, at least one WUB exists, and after the last
    word, any number of WUB is possible.

    Examples:
    >>> song_decoder("WUBWUBAWUBBC")
    A B C
    >>> song_decoder("WEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
    WE ARE THE CHAMPIONS MY FRIEND
    """

    return " ".join(filter(lambda x: x != "", song.split("WUB")))
