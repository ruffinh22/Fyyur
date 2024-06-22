import os
import psycopg2
from flask import Flask

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
DB_URI = 'postgresql+psycopg2://admin:wI8I8Pl3DNrFNKFrEAYC9McJjEll3Iyx@dpg-cpoinq2j1k6c73a81if0-a/attendance_3r8v'
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False


