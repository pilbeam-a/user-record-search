------
User Record Search Project
------

Lightweight app for searching, displaying and creating User records

Each User record requires:
- First name
- Last name
- Job title
- Phone
- Email

Constraints:
- Full name (First name and Last name) must be unique
- Phone and Email must be unique
- Phone must be a valid UK mobile phone number
- Email must be a valid email address

User record import:
- User records can be imported from .xlsx files using the following command
    `python manage.py import_user_records /path/to/file/Data.xlsx`

Page behaviour:
- User records are searched on full name once 2 or more characters are entered
- User record matches are shown in a dropdown list under the search box
- If selected by clicking, the full User record information is added as a card on a grid 3 wide
- New user records can be added by:
-   1. Clicking the "New user +" button
-   2. Entering the User record data following the constraints above
-   3. Clicking the "Create" button
-   4. On success, a new User record is created which can then be searched
-   5. On failure, any error messages are shown for correction


------
Setup
------

1. Create and activate a new Python virtualenv
2. Clone this repo
3. CD to project directory
4. Install pip packages
    `pip install -r requirements.txt`
5. Migrate the models to the database
    `python manage.py migrate`
6. Run the server
    `python manage.py runserver [port]`
    *Note: port is optional, default 8000
7. Browse to the app
    `http://localhost:[port]/`
