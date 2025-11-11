import datetime
import sys
import factory 
import worker

while True:
    print("Välkommen till en ny dag!")
    print("[1] Stämpla in.")
    print("[2] Visa tidbank.")
    print("[3] Stämpla ut.")
    print("[4] Visa instämplade kollegor.")
    print("[0] Avsluta. ")
    user_choice = input(">: ").strip()

    if user_choice == "1":
        name = input(f"Vem ska stämpla in? ")
        try:
            time_str = input("När började du jobba? (HH:MM) ")
        except ValueError:
            print("Ogiltig inmatning! Skriv in tiden i formatet '07:00'")
        time_in = parse_time(time_str)
        worker_in[name] = time_in
        print(f"{name} stämplade in kl {worker_in[name]}")
    elif user_choice == "2":
        name = input(f"Vems flextid vill du se? ")
        flexbank(name)
    elif user_choice == "3":
        name = input(f"vem ska stämpla ut? ")
        if name in worker_in:
            try:
                out_time_str = input("När slutade du? (HH:MM) ")
            except ValueError:
                print("Ogiltig inmatning! Skriv in tiden i formatet '16:00'")
            out_time = parse_time(out_time_str)
            time_in = worker_in.pop(name)
            work_duration = out_time - time_in
            print(f"{name} stämplade ut kl {out_time} och arbetade i {work_duration}")
    elif user_choice == "4":
        print("Instämplade kollegor:")
        for name in worker_in:
            print(f" - {name}")
    elif user_choice == "0":
        print("Avslutar.")
        sys.exit()
    else:
        print("Ogiltigt val. Du får sparken!")
        break
