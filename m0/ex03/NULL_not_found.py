def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, type(float("Nan"))):
        print(f"Cheese: nan {type(object)}")
    elif isinstance(object, type(int)):
        print(f"Zero: 0 {type(object)}")
    elif isinstance(object, type('')) and len(object) == 0:
        print(f"Empty: {type(object)}")
    elif isinstance(object, type(False)):
        print(f"Fake: False {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
