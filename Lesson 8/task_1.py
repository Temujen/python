class Data:
    day_mon_year = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        Data.day_mon_year = data

    @classmethod
    def convert_to_int(cls):
        cls.day, cls.month, cls.year = map(int, cls.day_mon_year.split('-'))
        # print(f"day = {cls.day}, {type(cls.day)}\n"
        #       f"month = {cls.month}, {type(cls.month)}\n"
        #       f"year = {cls.year}, {type(cls.year)}")

    @staticmethod
    def validate():
        if 1 <= Data.day <= 31 and 1 <= Data.month <= 12 and 1918 <= Data.year <= 2020:
            print("Date entered correctly")
        else:
            print("Wrong date\n"
                  "Enter day between 1-31, month between 1-12, year between 1918-2020")


a = Data(input("Enter date in format day-month-year: "))
a.convert_to_int()
a.validate()
