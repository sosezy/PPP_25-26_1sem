

if __name__ == "__main__":
    from abc import ABC, abstractmethod

class TimeInterval(ABC):
    @abstractmethod
    def to_seconds(self):
        pass

    def format(self):
        total = self.to_seconds()
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return f"{h} h {m} min {s} s"

class HMSInterval(TimeInterval):
    def __init__(self, time_str):
        h, m, s = map(int, time_str.split(":"))
        self.h = h
        self.m = m
        self.s = s
    def to_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

class MillisecondInterval(TimeInterval):
    def __init__(self, ms):
        self.ms = int(ms)
    def to_seconds(self):
        return self.ms // 1000

class MinSecInterval(TimeInterval):
    def __init__(self, minutes, seconds):
        self.minutes = int(minutes)
        self.seconds = int(seconds)
    def to_seconds(self):
        return self.minutes * 60 + self.seconds

class HoursInterval(TimeInterval):
    def __init__(self, hours):
        self.hours = float(hours)
    def to_seconds(self):
        return int(self.hours * 3600)

def parse_interval(line):
    parts = line.split()
    type_name = parts[0]
    if type_name == "hms":
        return HMSInterval(parts[1])
    elif type_name == "ms":
        return MillisecondInterval(parts[1])
    elif type_name == "minsec":
        return MinSecInterval(parts[1], parts[2])
    elif type_name == "hours":
        return HoursInterval(parts[1])
    else:
        raise ValueError("Неизвестный формат: " + type_name)

if __name__ == "__main__":
    lines = [
        "hms 01:30:00",
        "ms 90000",
        "minsec 3 45",
        "hours 2.5"
    ]
    intervals = [parse_interval(line) for line in lines]

    total_sec = sum(i.to_seconds() for i in intervals)
    avg_sec = total_sec // len(intervals)
    max_sec = max(i.to_seconds() for i in intervals)

    def format_human(sec):
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return f"{h} h {m} min {s} s"


    print("Total:", format_human(total_sec))
    print("Average:", format_human(avg_sec))
    print("Max:", format_human(max_sec))
