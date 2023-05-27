# Google Calendar Evetns

## Fetch your Google calendar events

### 👨‍💻 Project Setup: 

- Clone this repository
- Enter the shell by typing `$ pipenv shell`
- Install dependencies by typing `$ pipenv install`
- Complete the steps mentioned in **Environment variables** section
- Run migrations `$ python manage.py migrate`
- Run local server `$ python manage.py runserver`

### 🔐 Environment variables: 

- Create file `.env` inside `calender` directory
- Copy contents from `.env.example` file and paste it in the `.env` file you just created.
- After copying the contents, edit the `GOOGLE_CLIENT_ID` and `GOGGLE_CLIENT_SECRET` with your respective credentials.
