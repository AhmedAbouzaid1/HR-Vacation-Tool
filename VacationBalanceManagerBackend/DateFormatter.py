from datetime import datetime


class DateFormatter:
    def __init__(self) -> None:
        pass

    def __init__(self, start_date_str, end_date_str):
        self.start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    def get_dates(self):
        return self.start_date, self.end_date
