#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    list_last = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            print("wrong type")
            result.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            continue
        except IndexError:
            print("out of range")
            result.append(0)
            continue
        finally:
            j = 0
    for i in range(list_length):
        list_last.append(result[i])
    return list_last

