import mysql.connector


class VacationBalanceHandler:
    def __init__(self, query_executor):

        self.query_executor = query_executor

    def get_vacation_balance(self, type):

        id = 1  # Assuming the system has only one exmployee
        try:
            query = "SELECT {}_balance FROM VacationBalance WHERE employee_id = {}".format(type,
                                                                                           id)
            result = self.query_executor.selection_query(query)
            return result[0] if result else None

        except:
            print("Error Receiving the Employee Vacation Balance")
            return None

    def update_vacation_balance(self, duration, type):
        id = 1
        try:
            current_balance = self.get_vacation_balance(type)[0]
            new_balance = current_balance - int(duration)
            if (new_balance >= 0):
                query = "UPDATE VacationBalance SET {}_balance = {} WHERE employee_id = {}".format(type,
                                                                                                   new_balance, id)
                result = self.query_executor.update_query(query)
        except:
            print("Error occured during updating the vacation balance")
