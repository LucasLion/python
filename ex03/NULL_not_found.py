





def NULL_not_found(object: any) -> int:
    match object:
        case int:
            print(f"Zero: {type(object)}")
        case float:
            print(f"Cheese: {type(object)}")
        case str:
            print(f"Empty: {type(object)}")
        case bool:
            print(f"Fake: {type(object)}")
        case None:
            print(f"Nothing: {type(object)}")
        case _:
            print("Type not Found")

    return 1;

