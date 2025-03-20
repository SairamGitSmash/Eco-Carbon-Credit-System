import os
from dotenv import load_dotenv
load_dotenv()

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'ad2cabe3321c24621f1ce03a18b5940151295d434a491b5997024b8c6512399a')
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://user:root@localhost:3306/carbon_credit_db')
#     # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://user:password@localhost/carbon_credit_db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'c7295042e931c6d0b2b9fd3f47ac80c202ac5137cda125fdde09b8e63d249987')



class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:root@localhost:3306/carbon_credit_db'  # Change as needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'c7295042e931c6d0b2b9fd3f47ac80c202ac5137cda125fdde09b8e63d249987'
    SESSION_TYPE = 'filesystem'  # Needed for Flask-Session