# Jobsity coding challenge

## First steps

To create, activate the virtual environment and install dependencies, run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the app and the chatbot

To run the app, simply run:

```
flask run
```

If you want to test the functionality in two different computers by accessing the public IP address of
the computer running the Flask App, then specify the host to be `0.0.0.0`:

```
flask run --host=0.0.0.0
```

To run the chatbot, use the following command:

```
python chatbot/stock_server.py
```

## To add a new chatroom

In order to add a new chatroom manually, run the following commands:

```
flask shell
c = Chatroom(chatroom_name="Custom chatroom name")
db.session.add(c)
db.session.commit()
```

## Database migrations

If for some reason the migration repository or the database itself is not present, run the following command:

```
flask db init
```

To make the migrations and upgrade the database, run the following commands:

```
flask db migrate
flask db upgrade
```
