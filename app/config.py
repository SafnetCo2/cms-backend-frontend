import os
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/cmsdb')


    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY =os.environ.get('SECRET_KEY','mysecretkey')