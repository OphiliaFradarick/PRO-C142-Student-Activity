from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendations
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe


# variables to store data


# method to fetch data from database


# /movies api


# /like api


# /dislike api


# /did_not_watch api

# api to return list of popular movies




# api to return list of recommended movies



if __name__ == "__main__":
  app.run()
