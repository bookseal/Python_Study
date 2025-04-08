def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    result = ""
    return_num = 42

    if (object_type == list):
        result += "List :"
    elif (object_type == tuple):
        result += "Tuple :"
    elif (object_type == set):
        result += "Set :"
    elif (object_type == dict):
        result += "Dict :"
    elif (object_type == str):
        result += object + " is in the kitchen :"
    else:
        print("Type not found")
        return return_num

    print(result, type(object))
    return return_num


# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello": "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))