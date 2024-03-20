

def all_thing_is_obj(object: any) -> int:
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    string = "string"

    if type(object) == type(ft_list):
        print(f"{type(object).__name__} : {type(object)}".capitalize())
    elif type(object) == type(ft_tuple):
        print(f"{type(object).__name__} : {type(object)}".capitalize())
    elif type(object) == type(ft_set):
        print(f"{type(object).__name__} : {type(object)}".capitalize())
    elif type(object) == type(ft_dict):
        print(f"{type(object).__name__} : {type(object)}".capitalize())
    elif type(object) == type(string):
        print(f"{object} is in the kitchen : {type(object)}".capitalize())
    else:
        print("Type not found")
        
    return 42

