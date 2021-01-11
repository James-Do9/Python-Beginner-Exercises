def number_of_bottles():
    for i in reversed(range(1, 100)):
        if i == 1:
            print(f"""{i} bottle of milk on the wall, {i} bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.\n\nNo more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.""")
        else:
            print(f"""{i} bottles of milk on the wall, {i} bottles of milk.\nTake one down and pass it around, {i - 1} milk on the wall.\n""")


number_of_bottles()