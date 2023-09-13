lang = input("Pls enter your language :")

match lang.strip().lower():
    case "english":
        print("ENG")
    case "thai":
        print("THA")
    case _:
        print("Invalid language")
