import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Goal

# def getMostReplayed(video_id):

#     most_replayed = {}
#     return most_replayed


def getMostReplayed(video_id):
    most_replayed = {}
    return most_replayed

if __name__ == "__main__":
    df = pd.read_csv('filtered_with_headers.csv')
    youtube_id_list = df['youtube_id'].tolist()
    id = youtube_id_list[0]
    print(id)
    getMostReplayed(id)