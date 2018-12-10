import timeit

def create_rand_list_with_choice(x=1, y=9):
    from random import choice
    list_known=[]
    for i in range(x,y+1):
        list_known.append(i)
    list_constructed_random=[]
    while len(list_constructed_random) < y:
        choice_nr = choice(list_known)
        list_known.remove(choice_nr)
        list_constructed_random.append(choice_nr)
    return list_constructed_random

def sum_01(list_name):
    """Sum up horizontal
    """
    row1=sum(list_name[0:3])
    row2=sum(list_name[3:6])
    row3=sum(list_name[6:9])
    list_sums = [row1, row2, row3]
    return list_sums

def sum_02(list_names):
    """Sum up vertical
    """
    column1=list_names[0]+list_names[3]+list_names[6]
    column2=list_names[1]+list_names[4]+list_names[7]
    column3=list_names[2]+list_names[5]+list_names[8]
    list_col_sums = [column1, column2, column3]
    return list_col_sums

def sum_03(list_names):
    """Sum up diagonal
    """
    diag1=list_names[0]+list_names[4]+list_names[8]
    diag2=list_names[2]+list_names[4]+list_names[6]
    list_diags_sums = [diag1, diag2]
    return list_diags_sums



def perfect_rand_list():
    """All members in lines add up to precisely 15
    """
    list_temp = create_rand_list_with_choice()
    list_temp_sums = sum_01(list_temp)
    while (list_temp_sums[0] != 15) or (list_temp_sums[1] != 15):
        # print(list_temp)
        list_temp = create_rand_list_with_choice()
        list_temp_sums = sum_01(list_temp)
    return list_temp

def even_more_perfect_rand_list():
    """All members in lines and columns add up to precisely 15
    """
    list_temp = create_rand_list_with_choice()
    list_temp_sums_rows = sum_01(list_temp)
    list_temp_sums_cols = sum_02(list_temp)
    while (list_temp_sums_rows[0] != 15) or (list_temp_sums_rows[1] != 15) or (list_temp_sums_cols[0] != 15) or (list_temp_sums_cols[1] !=15):
        print(list_temp)
        list_temp = create_rand_list_with_choice()
        list_temp_sums_rows = sum_01(list_temp)
        list_temp_sums_cols = sum_02(list_temp)
    return list_temp

def magic_square():
    """All members in lines and columns and diagonals add up to precisely 15
    """
    list_temp = create_rand_list_with_choice()
    list_temp_sums_rows = sum_01(list_temp)
    list_temp_sums_cols = sum_02(list_temp)
    list_temp_diags = sum_03(list_temp)
    while (list_temp_sums_rows[0] != 15) or (list_temp_sums_rows[1] != 15) or (list_temp_sums_cols[0] != 15) or (list_temp_sums_cols[1] !=15) or (list_temp_diags[0] != 15) or (list_temp_diags[1] != 15):
        # print(list_temp)
        list_temp = create_rand_list_with_choice()
        list_temp_sums_rows = sum_01(list_temp)
        list_temp_sums_cols = sum_02(list_temp)
        list_temp_diags = sum_03(list_temp)
    return list_temp

def create_diff_perf_rand_lists(x):
    diff_perf_rand_list=[perfect_rand_list()]
    for i in range(x):
        tmp_diff_perf_rand_list = perfect_rand_list()
        diff_perf_rand_list.sort()
        if tmp_diff_perf_rand_list not in diff_perf_rand_list:
            diff_perf_rand_list.append(tmp_diff_perf_rand_list)
    return_list = sorted(diff_perf_rand_list)
    return return_list

def create_diff_magic_squares(x):
    """8 possiblities http://www.mathematische-basteleien.de/magsquare.htm
    """
    start_time = timeit.default_timer()
    diff_perf_rand_list=[magic_square()]
    for i in range(x):
        tmp_diff_perf_rand_list = magic_square()
        diff_perf_rand_list.sort()
        if tmp_diff_perf_rand_list not in diff_perf_rand_list:
            diff_perf_rand_list.append(tmp_diff_perf_rand_list)
    return_list = sorted(diff_perf_rand_list)
    time_it_took = timeit.default_timer() - start_time
    return return_list, time_it_took
