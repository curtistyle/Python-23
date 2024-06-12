def FilterByLetter(lyst : list, key, *args):
    temp_list = list()
    for element in lyst:
        for letter in args:
            if str(letter).lower() == str(element[key][0]).lower():
                temp_list.append(element)
    return temp_list

def FrequencyCounter(lyst : list, key, *args):
    list_temp = [[0, item] for item in args]
    
    for element in lyst:
        for index, ocurrence in enumerate(args):
            if (ocurrence == element[key]):
                list_temp[index][0] += 1
    return list_temp
                

def barrido(lyst : list, *keys):
    if lyst == []:
        raise ValueError("No hay nada en la lista")
        
    
    if type(lyst[0]) == type(dict()):
        if keys == ():
            for items in lyst:
                for key, value in items.items():
                    print(f"'{key}' = {value}")
                print()   
        else:
            for items in lyst:
                for key in keys:
                    print(f"{key} : {items[key]}")
                print()
    else:
        print("[ ", end="")
        for item in lyst:
            print(f"{item}, ", end="")
        print("\b\b ]")

def barrido_dict(lyst : list):
    for items in lyst:
        for key, value in items.items():
            print(f"'{key}' = {value}")
        print() 

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index
    
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

def show(list_values, position, *keys):
    for key in keys:
        print(f"{key} : {list_values[position][key]}")
    print()

def search_to_list(lyst : list, key=None,*args):
    new_list = list()
    if key is not None:
        for element in lyst:
            for sought in args:
                if element[key] == sought:
                    new_list.append(element)
    return new_list
    

def quitar(lyst : list, item):
    position = lyst.index(item)
    lyst.pop(position)