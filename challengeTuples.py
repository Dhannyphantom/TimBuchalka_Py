imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Puling the Rug"), (2, "Psycho"), (3, "Kentish Town Waltz"))

album, artist, year, tracks = imelda

print("Album name: " + album)
print("Artist: " + artist)
print("Year: " + str(year))
print("Tracks: ")

for track in tracks:
    number, title = track
    print("\t{}. {}".format(number, title))

