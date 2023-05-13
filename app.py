# Import required modules
import os
import sys
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, date, timedelta

# Import custom modules
from VacationBalanceManagerBackend.DurationHandler import DurationHandler
from VacationBalanceManagerDatabase.DBConnector import DBConnector
from VacationBalanceManagerDatabase.QueryExecutor import QueryExecutor
from VacationBalanceManagerBackend.VacationBalanceHandler import VacationBalanceHandler

# Create a Flask app
app = Flask(__name__)
CORS(app)

# Load the Flask app configuration from the config file
app.config.from_pyfile(os.path.join(".", "Config/app.config"), silent=False)

# Create a DBConnector instance and connect to the database
db_connector = DBConnector(app.config.get('HOST'),
                           app.config.get('USER'),
                           app.config.get('PASSWORD'),
                           app.config.get('DATABASE'))
db_connector.connect()

# Create a QueryExecutor instance to execute queries on the database
query_executor = QueryExecutor(db_connector.conn)

# Define a route to handle vacation requests


@app.route("/balanceManager", methods=['POST'])
def vacation_balance_manager():
    try:
        if request.method == 'POST':
            # Get the JSON data from the request
            data = request.json
            vacation_duration = data['VacationDuration']
            vacation_type = data['vacationType']

            # Create a VacationBalanceHandler instance and update the vacation balance in the database
            vacation_balance_handler = VacationBalanceHandler(query_executor)
            vacation_balance_handler.update_vacation_balance(
                vacation_duration, vacation_type)

            # Get the updated annual and sick leave balances from the database
            annual_balance = vacation_balance_handler.get_vacation_balance(
                'annual')
            sick_balance = vacation_balance_handler.get_vacation_balance(
                'sick')

            # Return the updated balances as a JSON response
            return(jsonify(annual_balance, sick_balance))
    except:
        # Return an error message if an exception occurs
        return(jsonify("Error occurred during handeling the vacation balance"))

# Define a route to display the vacation duration


@app.route("/calculateDuration", methods=['POST'])
def calculate_vacation_duration():
    try:
        if request.method == 'POST':
            # Get the JSON data from the request
            data = request.json

            # Convert the start and end dates formats
            start_date, end_date = DurationHandler.adjust_date_format(
                data['startDate'], data['endDate'])

            # Calculate the duration between the start and end dates
            duration = DurationHandler.duration_calculator(
                start_date, end_date)

            # Return the calculated duration as a JSON response
            return(jsonify(duration))
    except:
        # Return an error message if an exception occurs
        return(jsonify("An error occurred during calculating the vacation duration"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
