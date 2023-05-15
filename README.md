# Vacation Balance Manager

A Flask web application for managing annual and sick leave balances for employees.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository
2. Install the required Python modules using the following command:

```
 pip install -r requirements.txt
```

3. Create a Config/app.config file and specify the database connection details. You can use the current Config/app.config file as a template.
4. Execute VacationBalanceManagerDatabase/SetupQuery.sql in your MYSQL Workbench.
5. Run the Flask app using the following command:

```
python app.py
```

5. Navigate to VacationBalanceManagerFrontend/index.html in your web browser to access the application.

## Usage

This application provides two routes for managing vacation balances and calculating vacation durations.

### Update Vacation Balance

To update the vacation balance, send a POST request to the /balanceManager endpoint with the following JSON data:

```JSON
{
  "VacationDuration": "2 days",
  "vacationType": "annual"
}
```

Replace 2 days with the number of days of vacation to add or subtract, and annual or sick with the type of vacation.

The response will be a JSON object containing the updated annual and sick leave balances:

```JSON
{
  "annual": 20,
  "sick": 10
}
```

### Calculate Vacation Duration

To calculate the vacation duration, send a POST request to the /calculateDuration endpoint with the following JSON data:

```JSON
{
  "startDate": "2022-05-01",
  "endDate": "2022-05-05"
}
```

Replace 2022-05-01 and 2022-05-05 with the start and end dates of the vacation in YYYY-MM-DD format.

The response will be a JSON object containing the duration of the vacation in days:

```JSON
{
  "duration": 5
}
```

## Class Diagram
![alt text](https://github.com/AhmedAbouzaid1/HR-Vacation-Tool/blob/main/VacationAppClassDiagram.jpeg)

## Sequence Diagram
![alt text](https://github.com/AhmedAbouzaid1/HR-Vacation-Tool/blob/main/VacationAppSequenceDiagram.jpeg)

## User Stories

The system implements the following user stories:

- The system allows employees to select a vacation type from a list that contains the options of Annual and Sick.
- The system allows employees to select the start and end date of their vacation.
- The system allows employees to submit their vacation request.
- The system allows employees to view their current annaul and sick balance, which is assumed to be 21 and 14 days for annual and sick vacation respectively.
- The system updates the balance based on the start and end dates selected, excluding weekends.
- The system automatically deducts the requested vacation days from the employee's balance without the need for manager approval.
- The system updates the balance in real-time and displays the updated balance to the employee.

## Built With

- Python
- Flask
- Flask-RESTful
- Flask-CORS
