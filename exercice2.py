

def draw_hollow_square(char_to_draw, size):    
    size2 = size * 2 - 4
    count = 0

    for i in range(size):
        print(char_to_draw * size)

        count += 1

        if count >= size:
            exit()

        while count != size:
            print(char_to_draw, end=" " * size2)
            print(char_to_draw)
            # print(end="\n")
            count += 1

            if count == size - 1:
                count = size



char_to_draw = "." + " "
size = 3

draw_hollow_square(char_to_draw, size)     
















