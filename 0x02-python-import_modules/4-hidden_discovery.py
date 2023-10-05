#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for items in dir(hidden_4):
        if items[0] != "_":
            print(items)
