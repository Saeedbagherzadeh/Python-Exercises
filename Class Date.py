class Date:
    def init(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def show(self):
        print("Date: {}/{}/{}".format(self.day, self.month, self.year))

    def add(self, other_date):
        new_day = self.day + other_date.day
        new_month = self.month + other_date.month
        new_year = self.year + other_date.year

        if new_day > 30:
            new_day -= 30
            new_month += 1

        if new_month > 12:
            new_month -= 12
            new_year += 1

        return Date(new_day, new_month, new_year)

    def sub(self, other_date):
        new_day = self.day - other_date.day
        new_month = self.month - other_date.month
        new_year = self.year - other_date.year

        if new_day < 1:
            new_month -= 1
            new_day += 30

        if new_month < 1:
            new_year -= 1
            new_month += 12

        return Date(new_day, new_month, new_year)

    def get_month_name(self):
        month_names = {
            1: "فروردین",
            2: "اردیبهشت",
            3: "خرداد",
            4: "تیر",
            5: "مرداد",
            6: "شهریور",
            7: "مهر",
            8: "آبان",
            9: "آذر",
            10: "دی",
            11: "بهمن",
            12: "اسفند"
        }

        return month_names.get(self.month)

    def is_valid_date(self):
        if self.day < 1 or self.day > 30:
            return False
        if self.month < 1 or self.month > 12:
            return False
        if self.year < 1 or self.year > 9999:
            return False
        return True


# Usage Example
date1 = Date(15, 6, 2023)
date2 = Date(20, 7, 2023)

date1.show()
date2.show()

result = date1.add(date2)
result.show()

result = date2.sub(date1)
result.show()

month_name = date1.get_month_name()
print("Month Name:", month_name)

is_valid = date1.is_valid_date()
print("Is Valid Date:", is_valid)