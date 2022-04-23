def list_manipulation(lst,command, location, value=None):
    if((command == "add") and (location == "beginning")):
        lst.insert(0,value)
        print(lst)
    elif((command == "add") and (location == "end")):
        lst.append(value)
        print(lst)
    elif((command == "remove") and (location == "beginning")):
        lst.pop(0)
        print(lst)
    elif((command == "remove") and (location == "end")):
        lst.pop(-1)
        print(lst)
    else:
        return None