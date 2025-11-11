import sys

class Factory:
    def __init__(self):
        self = name

    factory = Factory()
    factory.add_worker("Charlie")
    factory.add_worker("Maja")
    factory.start_day("Charlie")
    factory.end_day("Charlie")

    start_day = datetime.datetime(2025, 11, 7, 6, 30)
    end_day = datetime.datetime(2025, 11, 7, 16, 15)

    worked_time = Worker.flex_bank(start_day, end_day)
    #print(f"Timmar arbetade: {worked_time}")

    while True:
        print("Välkommen till en ny dag!")
        print("[1] Stämpla in.")
        print("[2] Kolla tidbank.")
        print("[3] Stämpla ut.")
        print("[4] Visa instämplade kollegor.")
        print("[0] Avsluta. ")
        user_choice = input(">: ").strip().lower()

        if user_choice == "1":
            name = input(f"Vem ska stämpla in? ")
            name == {name}
            print(f"{name} stämplade in kl")
        elif user_choice == "2":
            print(Worker.flex_bank(start_day, end_day))
        elif user_choice == "3":
            name = input(f" vem ska stämpla ut? ")
            print(f"{name} stämplade ut kl ")
        elif user_choice == "4":
            print(name)
        elif user_choice == "0":
            print("Avslutar.")
            sys.exit()
        else:
            print("Ogiltigt val. Du får sparken!")
