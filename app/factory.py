import datetime
import sys

def parse_time(time_str):
        now = datetime.date.today()
        hour, minute = map(int, time_str.split(":"))
        return datetime.datetime.combine(now, datetime.time(hour, minute))

class Worker():
    def __init__(self, name):
        self.name = name
        self.time_in = None
        self.time_out = None

    def check_in(self, time_in):
        self.time_in = time_in

    def check_out(self, time_out):
        self.time_out = time_out

    def get_work_time(self):
        if self.time_in and self.time_out:
            delta = self.time_out - self.time_in
            return delta
        else:
            return None
        
    @staticmethod
    def flex_bank(start_day, end_day):
        start_limit = start_day.replace(hour=7, minute=0, second=0, microsecond=0)
        end_limit = start_day.replace(hour=16, minute=0, second=0, microsecond=0)

        if start_day < start_limit:
            start_limit = start_limit
        if end_day > end_limit:
            end_day = end_limit

        delta = end_day - start_day
        return delta
    
    def calculate_overtime(start_time, end_time):
        day_start = start_time.replace(hour=6, minute=0, second=0, microsecond=0)
        day_end = start_time.replace(hour=17, minute=0, second=0, microsecond=0)
        total_time = end_time - start_time
        outside_time = datetime.timedelta(0)
        if start_time < day_start:
            if end_time > day_start:
                outside_time += day_start - start_time
            else:
                outside_time += end_time - start_time
        elif start_time > day_end:
            outside_time += start_time - day_end
        
        if end_time > day_end:
                outside_time += end_time - day_end
        return outside_time
    
#worker_sessions = {}
#in_time = datetime()
#worker_sessions.setdefaoult(name, []).append(('in', in_time))
#out_time = datetime()
#worker_sessions.setdefaoult(name, []).append(('out', out_time))
    
    def flexbank(name):
        sessions = worker_sessions.get(name)
        if not sessions:
            print(f"Inga tider registrerade för {name}.")
            return
        
        total_time = datetime.timedelta()
        in_time = None
        for event, time in sessions:
            if event == "in":
                in_time = time
            elif event == "ut":
                if in_time:
                    delta = time -in_time
                    total_time += delta
                    in_time = None
        print(f"Flexbank för {name}: {total_time}")
    
    def add_worker(self, name):
        new_worker = Worker(name)
        self.worker_in.append(new_worker)
        return new_worker


worker_in = {}

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
        #flexbank(name)
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
    