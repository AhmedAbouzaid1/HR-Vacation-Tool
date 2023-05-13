from VacationBalanceManagerBackend.DateFormatter import DateFormatter
from VacationBalanceManagerBackend.VacationDurationCalculator import VacationDurationCalculator


class DurationHandler:

    def __init__(self) -> None:
        pass

    def adjust_date_format(start_date, end_date):
        try:
            date_formatter = DateFormatter(start_date, end_date)
            start_date, end_date = date_formatter.get_dates()
            return start_date, end_date
        except:
            return("An error occurred during adjusting the date format")

    def duration_calculator(start_date, end_date):
        try:
            vacation_duration_calculator = VacationDurationCalculator(
                start_date, end_date)
            duration = vacation_duration_calculator.exclude_weekends()
            return(duration)
        except:
            return("An error occurred during calculating the vacation duration")
