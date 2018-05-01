#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    add_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            add_list.append(result)
    return add_list
