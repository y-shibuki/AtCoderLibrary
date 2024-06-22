def print_bit(x, n):
    match x:
        case int():
            print(format(x, f"0{n}b").replace("0", ".").replace("1", "o"))
        case list():
            for i in x:
                print(format(i, f"0{n}b").replace("0", ".").replace("1", "o"))

