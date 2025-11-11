import datetime
import sys

def parse_time(time_str):
        now = datetime.date.today()
        hour, minute = map(int, time_str.split(":"))
        return datetime.datetime.combine(now, datetime(hour, minute))

class Worker():
    def __init__(self, name):
        self.name = name
        self.time_in = None
        self.time_out = None

    def check_in(self, time_in):
        self.time_in = time_in

    def check_out(self, time_out):
        self.time_out = time_out
    
    #def start_day(self):
    #    self.start_day = datetime.datetime.now()
    #
    #def end_day(self):
    #    self.end_day = datetime.datetime.now()

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
        day_start = start_time.replace(hour=7, minute=0, second=0, microsecond=0)
        day_end = start_time.replace(hour=16, minute=0, second=0, microsecond=0)
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
    
    def add_worker(self, name):
        return Worker(name)
    
    #start = datetime.datetime(2024, 11, 7, 6, 10) #stämplade in 10 över 6
    #end = datetime.datetime(2024, 11, 7, 16, 0)

    #overtime = calculate_overtime(start, end)
    #print(f"Tiden utanför 7-16 är: {overtime}")

    def add_worker(self, name):
        new_worker = Worker(name)
        self.workers.append(new_worker)
        return new_worker
    
    def start_day(self, name):
        for worker in self.workers:
            if worker.name == name:
                worker.check_in()
                print(f"{name} stämplar in kl. ")
                break
    
    def end_day(self, name):
        for worker in self.workers:
            if worker.name == name:
                worker.check_out()
                work_time = worker.get_work_time()
                if work_time:
                    print(f"{name} jobbade i {work_time}")
                else:
                    print(f"{name} har inte stämplat in/ut korrekt")
                    break

    

#start_day = datetime.datetime(2025, 11, 7, 6, 30)
#end_day = datetime.datetime(2025, 11, 7, 16, 15)
#worked_time = Worker.flex_bank(start_day, end_day)

worker_in = {}

while True:
    print("Välkommen till en ny dag!")
    print("[1] Stämpla in.")
    print("[2] Visa tidbank.")
    print("[3] Stämpla ut.")
    print("[4] Visa instämplade kollegor.")
    print("[0] Avsluta. ")
    user_choice = input(">: ").strip().lower()

    if user_choice == "1":
        name = input(f"Vem ska stämpla in? ")
        worker_in[name] = datetime.datetime.now()
        start_day = input("När började du jobba? (HH:MM) ")
        in_time = parse_time(in_time_str)
        worker_in[name] = in_time
        print(f"{name} stämplade in kl {worker_in[name]}")
    elif user_choice == "2":
        print(Worker.flex_bank(start_day, end_day))
    elif user_choice == "3":
        name = input(f" vem ska stämpla ut? ")
        if name in worker_in:
            out_time_str = input("När slutade du? (HH:MM) ")
            out_time = parse_time(out_time_str)
            in_time = worker_in.pop(name)
            out_time = datetime.datetime.now()
            work_duration = out_time - in_time
            print(f"{name} stämplade ut kl {out_time} och arbetade i {work_duration}")
        worker_in_time = worker_in.pop(name)
    elif user_choice == "4":
        print(name)
    elif user_choice == "0":
        print("Avslutar.")
        sys.exit()
    else:
        print("Ogiltigt val. Du får sparken!")
