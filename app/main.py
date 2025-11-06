import datetime

class Worker():
    def __init__(self, name):
        self.name = name
        self.time_in = None
        self.time_out = None
    
    def start_day(self):
        self.start_day = datetime.datetime.now()
    
    def end_day(self):
        self.end_day = datetime.datetime.now()

    def get_work_time(self):
        if self.time_in and self.time_out:
            delta = self.time_out - self.time_in
            return delta
        else:
            return None
        

class Factory():
    def __init__(self):
        self.workers = []

    def add_worker(self, name):
        new_worker = Worker(name)
        self.workers.append(new_worker)
        return new_worker
    
    def start_day(self, name):
        for worker in self.workers:
            if worker.name == name:
                worker.check_in()
                print(f"{name} stämplar in kl.")
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

factory = Factory()
factory.add_worker("Charlie")
factory.add_worker("Maja")

factory.start_day("Charlie")

factory.end_day("Charlie")