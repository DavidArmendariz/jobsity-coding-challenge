# Jobsity challenge

To create, activate the virtual environment and install dependencies, run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Database

If the migration repository is not present, run the following command:
```
flask db init
```
To make the migrations and upgrade the database, run the following commands:
```
flask db migrate
flask db upgrade
```