from os import system
def cls():
    system("clear")

list01=[]
for i in range(1,10):
    list01.append(i)

list_name=[]

def create_rand_list(x,y):
    from random import randint
    list_name = []
    i = 0
    while len(list_name) < y:
        rand_nr=randint(x,y)
        # print(i,list_name,rand_nr)
        if rand_nr not in list_name:
            list_name.append(rand_nr)
        i+=1
    # return list_name,i
    return list_name

def create_rand_list_01(x,y):
    """The idea is to random more efficient, by setting a range to choose from.
    Sort the list -list.sort()- and the list will be sorted for good, and
    with sorted(list) is will NOT.
    Get list[0] - min -  and  list[-1] -max-
    Introducing new function: randrange(start, stop) ->stop not including, so
    we can set range where randoms come from.
    I think trick is switch min - max - min etc.
    Maybe sets
    random.choice(s)(list)
    """
    from random import choice #, choices
    list_known=[]
    for i in range(x,y+1):
        list_known.append(i)
    list_constructed_random=[]
    i=0
    while len(list_constructed_random) < y:
        choice_nr = choice(list_known)
        list_known.remove(choice_nr)
        list_constructed_random.append(choice_nr)
        i+=1
    # return list_constructed_random,i
    return list_constructed_random

def sudoku_list(list_name):
    """3x3
    """
    list_row1=list_name[0:3]
    list_row1_added = sum(list_row1)
    list_row2=list_name[3:6]
    list_row2_added=sum(list_row2)
    list_row3=list_name[6:9]
    list_row3_added=sum(list_row3)
    list_matrix = f"{list_row1}\n{list_row2}\n{list_row3}"
    return list_matrix

def hor_sum(list_name):
    """3x3 sums
    """
    list_row1=list_name[0:3]
    list_row1_added = sum(list_row1)
    list_row2=list_name[3:6]
    list_row2_added=sum(list_row2)
    list_row3=list_name[6:9]
    list_row3_added=sum(list_row3)
    list_matrix = f"{list_row1_added}\n{list_row2_added}\n{list_row3_added}"
    return print(list_matrix)

def hor_sum_01(list_name):
    """3x3 sums individual
    """
    list_row1=list_name[0:3]
    list_row1_added = sum(list_row1)
    list_row2=list_name[3:6]
    list_row2_added=sum(list_row2)
    list_row3=list_name[6:9]
    list_row3_added=sum(list_row3)
    list_matrix = list_row1_added, list_row2_added, list_row3_added
    return list_matrix


def vert_sum(list_name):
    """3x3 sums vert
    """
    list_column1=list_name[0],list_name[3],list_name[6]
    list_column1_added = sum(list_column1)
    list_column2=list_name[1],list_name[4],list_name[7]
    list_column2_added = sum(list_column2)
    list_column3=list_name[2],list_name[5],list_name[8]
    list_column3_added = sum(list_column3)
    list_matrix = f"{list_column1_added} {list_column2_added} {list_column3_added}"
    return print(list_matrix)

def rand_list():
    from random import randint
    list_name = []
    while len(list_name) < 9:
        rand_nr=randint(1,9)
        if rand_nr not in list_name:
            list_name.append(rand_nr)
    return list_name


def perfect_rand_list():
    """All members in lines add up to precisely 15
    """
    list_temp = rand_list()
    if hor_sum(list_temp) != 15:
        list_temp = rand(list)
    else:
        return list_temp







# cls()
# list02=create_rand_list(1,9)
# sudoku_list(list02[0])
# print("\n")
# hor_sum(list02[0])
# print("\n")
# vert_sum(list02[0])
