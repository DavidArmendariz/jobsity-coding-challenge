import os
root = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(root, 'app.db')


class Config(object):
    SECRET_KEY = '8b0a09c13362a93285ba520b436e65f83d3fab17d48d25ae6b573f9477bfb0e8'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
