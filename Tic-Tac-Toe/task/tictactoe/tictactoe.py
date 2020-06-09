cells = list("_________")
print("-" * 9)
print("| {} {} {} |".format(*cells[0:3]))
print("| {} {} {} |".format(*cells[3:6]))
print("| {} {} {} |".format(*cells[6:9]))
print("-" * 9)
enter_coordinates = True
no_inline = True

cells_index_x = [index for index, cell in enumerate(cells) if cell == "X"]
cells_index_o = [index for index, cell in enumerate(cells) if cell == "O"]
cells_index__ = [index for index, cell in enumerate(cells) if cell == "_"]
position = [[1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]
position_index = [index for index, position in enumerate(position)]
nums = [str(num) for num in range(10)]
enter_count = 0


def user_input_position(x, y):
    input_coordinate = [int(x), int(y)]
    count = 0
    for _ in position:
        if input_coordinate == _:
            return count
        else:
            count += 1


def find_inline():
    x_indices = [i for i, el in enumerate(cells) if el == "X"]
    o_indices = [i for i, el in enumerate(cells) if el == "O"]
    inline = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    x_wins, o_wins = False, False
    global enter_coordinates
    global no_inline
    for el_inline in inline:
        if set(x_indices).issuperset(el_inline):
            x_wins = True
        elif set(o_indices).issuperset(el_inline):
            o_wins = True
    if x_wins and not o_wins:
        print("X wins")
        enter_coordinates = False
        no_inline = False
    elif o_wins and not x_wins:
        print("O wins")
        enter_coordinates = False
        no_inline = False
    elif x_wins and o_wins:
        print("Impossible")
        enter_coordinates = False
        no_inline = False
    else:
        no_inline = True


while enter_coordinates:
    user_input_1, user_input_2 = input("Enter the coordinates: ").split()
    if user_input_1 not in nums or user_input_2 not in nums:
        print("You should enter numbers!")
    elif not 1 <= int(user_input_1) <= 3 or not 1 <= int(user_input_2) <= 3:
        print("Coordinates should be from 1 to 3!")
    elif user_input_position(user_input_1, user_input_2) not in cells_index__:
        print("This cell is occupied! Choose another one!")
    else:
        input_index = user_input_position(user_input_1, user_input_2)
        if not enter_count % 2:
            cells[input_index] = "X"
        else:
            cells[input_index] = "O"
        enter_count += 1
        print("-" * 9)
        print("| {} {} {} |".format(*cells[0:3]))
        print("| {} {} {} |".format(*cells[3:6]))
        print("| {} {} {} |".format(*cells[6:9]))
        print("-" * 9)
        find_inline()
        if cells.count("X") + cells.count("O") == 9 and no_inline:
            print("Draw")
            enter_coordinates = False



