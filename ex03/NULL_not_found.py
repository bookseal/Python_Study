def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    return_value = 0

    output_message = ""

    if object is None:
        output_message += "Nothing: None <class 'NoneType'>"
    elif obj_type is float and object != object:  # NaN check: NaN is not equal to itself
        output_message += "Cheese: nan <class 'float'>"
    elif obj_type is int and object == 0:
        output_message += "Zero: 0 <class 'int'>"
    elif obj_type is str and object == "":
        output_message += "Empty: <class 'str'>"
    elif obj_type is bool and object is False:
        output_message += "Fake: False <class 'bool'>"
    else:
        output_message += "Type not found"
        return_value = 1
    print(output_message)
    return return_value


# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))