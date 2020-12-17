import ast 

def to_dict(item):  
    # initializing string  
    test_string = item 
    # using ast.literal_eval() 
    # convert dictionary string to dictionary 
    res = ast.literal_eval(test_string) 
    # print result 
    return res
def to_str(item):
    str1=str(item)
    return str1
def to_arr(item):
    li = list(item.split(" ")) 
    return li 
def list_to_str(item):
    listToStr = ' '.join(map(str, item)) 
    return listToStr
