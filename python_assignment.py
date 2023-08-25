class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def sort_by_p_id(self):
        for i in range(len(self.flights)):
            for j in range(i + 1, len(self.flights)):
                if self.flights[i].p_id > self.flights[j].p_id:
                    self.flights[i], self.flights[j] = self.flights[j], self.flights[i]

    def sort_by_start_time(self):
        for i in range(len(self.flights)):
            for j in range(i + 1, len(self.flights)):
                if self.flights[i].start_time > self.flights[j].start_time:
                    self.flights[i], self.flights[j] = self.flights[j], self.flights[i]

    def sort_by_priority(self):
        priority_mapping = {"Low": 0, "MID": 1, "High": 2}
        for i in range(len(self.flights)):
            for j in range(i + 1, len(self.flights)):
                if priority_mapping[self.flights[i].priority] > priority_mapping[self.flights[j].priority]:
                    self.flights[i], self.flights[j] = self.flights[j], self.flights[i]

    def display(self):
        print("{:<5} {:<10} {:<15} {:<10}".format("P_ID", "Process", "Start Time", "Priority"))
        for flight in self.flights:
            print("{:<5} {:<10} {:<15} {:<10}".format(flight.p_id, flight.process, flight.start_time, flight.priority))

flight_table = FlightTable()
flight_table.add_flight(Flight("P01", "VSCode", 100, "MID"))
flight_table.add_flight(Flight("P23", "Eclipse", 234, "MID"))
flight_table.add_flight(Flight("P93", "Chrome", 189, "High"))
flight_table.add_flight(Flight("P42", "JDK", 9, "High"))
flight_table.add_flight(Flight("P09", "CMD", 7, "High"))
flight_table.add_flight(Flight("P87", "NotePad", 23, "Low"))

print("Flight Table")
print("[1. Sort by P_ID, 2. Sort by Start Time, 3. Sort by Priority]")
sorting_parameter = int(input("Enter your choice: "))

if sorting_parameter == 1:
    flight_table.sort_by_p_id()
elif sorting_parameter == 2:
    flight_table.sort_by_start_time()
elif sorting_parameter == 3:
    flight_table.sort_by_priority()
else:
    print("Invalid sorting parameter")
    
flight_table.display()
