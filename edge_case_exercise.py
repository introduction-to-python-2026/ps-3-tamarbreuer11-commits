def move(my_list, direction):

    # Finds the index of the one in the list
    index_of_one = my_list.index(1)
    # Move the one to the left or to the right
    if direction == 'right':
    # chek if one is in the edge
       if index_of_one == len(my_list) -1:
           return my_list
       else  my_list[index_of_one] = 0
             my_list[index_of_one + 1] = 1
            return my_list
    elif direction == 'left':
    # chek if one is in the edge
       if index_of_one == 0:
           return my_list
        else my_list[index_of_one] = 0
             my_list[index_of_one - 1] = 1
            return my_list
