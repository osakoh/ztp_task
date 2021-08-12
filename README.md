# ZTP Technical Test.

### Requirements(Windows)

------------

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [PostgreSQL v 13 for Windows 10](https://postgresql.en.uptodown.com/windows/download).

------------ 

### Installation

    > pip install -r requirements.txt
    > pip install virtualenv

### Create and activate environment

    > virtualenv venv
    > venv\Scripts\activate

### Run migration

    > py manage.py migrate
    > py manage.py runserver

------------

### Tasks given:

- Read the customer details from the Excel file.
- Render a html page that displays the customers’ personal and consumption details in a table format.
- Details of the customer with the highest ‘Day Rate’ consumption.
- Details of the customer with the highest ‘Night Rate’ consumption.
- Details of the customer with the highest ‘Total Energy Cost’.

----- 

### Tasks completed:

- [x] Can read the customer details from the Excel file individually.
- [x] Render a html page that displays the customers’ personal and consumption details in a table format.
- [x] Details of the customer with the highest ‘Day Rate’ consumption.
- [x] Details of the customer with the highest ‘Night Rate’ consumption.
- [x] Details of the customer with the highest ‘Total Energy Cost’.

