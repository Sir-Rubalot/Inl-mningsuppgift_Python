import datetime
import sys

class Worker ():
    def __init__(self, name):
        self.name = name
        self.time_in = None
        self.time_out = None

    def parse_time(time_str):
        now = datetime.date.today()
        hour, minute = map(int, time_str.split(":"))
        return datetime.datetime.combine(now, datetime.time(hour, minute))
    
    def add_worker(self, name):
        new_worker = Worker(name)
        self.worker_in.append(new_worker)
        return new_worker

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

    def flexbank(name):
        sessions = worker_flex.get(name)
        if not sessions:
            print(f"Inga tider registrerade för {name}.")
            return
    
#worker_sessions = {}
#in_time = datetime()
#worker_sessions.setdefaoult(name, []).append(('in', in_time))
#out_time = datetime()
#worker_sessions.setdefaoult(name, []).append(('out', out_time))
        
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
    
