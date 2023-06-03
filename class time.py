class Time:
    def init(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        total_seconds = (self.hours  3600) + (self.minutes  60) + self.seconds
        return total_seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)


class TimeCalculator:
    def init(self):
        self.time = None

    def get_time(self):
        hours = int(input("Enter the hours: "))
        minutes = int(input("Enter the minutes: "))
        seconds = int(input("Enter the seconds: "))
        self.time = Time(hours, minutes, seconds)

    def convert_to_seconds(self):
        total_seconds = self.time.to_seconds()
        print("Total seconds:", total_seconds)

    def convert_from_seconds(self):
        total_seconds = int(input("Enter the total seconds: "))
        time = Time.from_seconds(total_seconds)
        print("Time:", time.hours, "hours,", time.minutes, "minutes,", time.seconds, "seconds")


# Usage Example
calculator = TimeCalculator()
calculator.get_time()
calculator.convert_to_seconds()
calculator.convert_from_seconds()