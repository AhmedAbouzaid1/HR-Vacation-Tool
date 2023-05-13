from datetime import datetime, date, timedelta


class VacationDurationCalculator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def count_weekdays(self, exclude_days):
        try:
            days_diff = (self.end_date - self.start_date).days + 1
            weekdays = [d for d in range(days_diff) if (
                self.start_date + timedelta(d)).weekday() not in exclude_days]
            return len(weekdays)
        except:
            return("An error occurred during counting the vacation days")

    def exclude_weekends(self):
        return self.count_weekdays([4, 5])
