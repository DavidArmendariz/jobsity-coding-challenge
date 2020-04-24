# Jobsity challenge

To create, activate the virtual environment and install dependencies, run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## To add a new chatroom

In order to add a new chatroom manually, run the following commands:
```
flask shell
c = Chatroom(chatroom_name="Custom chatroom name")
db.session.add(c)
db.session.commit()
```

## Database

If the migration repository or the database itself is not present, run the following command:
```
flask db init
```
To make the migrations and upgrade the database, run the following commands:
```
flask db migrate
flask db upgrade
```

