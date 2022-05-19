print("Please enter an IP Address")
address = input()

address += "."
# 192.168.43.267
segments = 0
num_length = 0


if address != ".":
    for char in address:
        num_length += 1
        if char == '.':
            num_length -= 1
            print("Segment {} has {} numbers".format(segments + 1, num_length))
            segments += 1
            num_length = 0

    print("There are {} segments".format(segments))
else:
    print("There are no segments")
