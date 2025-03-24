def NULL_not_found(object: any) -> int:

#your code here
    if object is None:
        print(f"Nothing: {object}", type(object))
    elif type(object) is float:
        print(f"Cheese: {object}", type(object))
    elif type(object) is int:
        print(f"Zero: {object}", type(object))
    elif type(object) is str and len(object) == 0:
        print(f"Empty:{object}", type(object))
    elif type(object) is bool:
        print(f"Fake: {object}", type(object))
    else:
        print("Type not found")
        return 1
    return 0
#--------------