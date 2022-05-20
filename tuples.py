# record = ("Rock solid", "Imagine Dragons", 2020)
#
# album, artist, year = record
#
# print(album)
# print(artist)
# print(year)

record = ("Rock solid", "Imagine Dragons", 2020, (
    (1, "Birds"), (2, "Enemies"), (3, "Believer")
))

album, artist, year, tracks = record

track1, track2, track3 = tracks

print(track2[1])
