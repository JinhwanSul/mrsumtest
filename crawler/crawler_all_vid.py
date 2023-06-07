import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import numpy as np
import re
import json

# Goal


def getMostReplayed(youtube_id):
    most_replayed = {}
    url = f'https://www.youtube.com/watch?v={youtube_id}'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    data = re.search(r'var ytInitialData = ({.*?});', soup.prettify()).group(1)
    data = json.loads(data)

    # Some video's Most Replayed features disappeared. Therefore, I will use the try-except block 
    try:
        markersMap = data['playerOverlays']['playerOverlayRenderer']['decoratedPlayerBarRenderer']['decoratedPlayerBarRenderer']['playerBar']['multiMarkersPlayerBarRenderer']['markersMap']
        mostReplayed = markersMap[-1]['value']['heatmap']['heatmapRenderer'] if markersMap is not None else None
        return mostReplayed
    except:
        print("Most Replayed features are removed or the video is no longer available")
    
    return None


if __name__ == "__main__":
    video_most_replayed_info = {}
    df = pd.read_csv('dataset/filtered_with_headers.csv')
    youtube_id_list = df['youtube_id'].tolist()
    for id in youtube_id_list:
        print(id)
        most_replayed_statistics = getMostReplayed(id)
        if most_replayed_statistics != None:
            video_most_replayed_info[id] = most_replayed_statistics
    with open("most_replayed.json", "w") as outfile:
        json.dump(video_most_replayed_info, outfile)

