import pandas as pd
import plotly.express as px
from collections import Counter
import streamlit as st
from typing import Optional, List


class App():
    def __init__(self, page_title: str, page_icon: str, layout: str) -> None:
        self.st = st
        self.st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

    def getDataGenresCount(self, data: pd.DataFrame, genres_type: str) -> Counter:
        if genres_type == 'Movie':
            data = data.query("Title_Type == 'movie' or Title_Type == 'tvMovie'")
        elif genres_type == 'Series':
            data = data.query("Title_Type == 'tvSeries' or Title_Type == 'tvMiniSeries'")

        data_genres = pd.DataFrame({'title': data['Title'], 'genres': data['Genres']})

        genres = []
        for i in data_genres['genres']:
            genres += i.replace(' ', '').split(',')
        genres_count = Counter(genres)
        return genres_count
    
    def createPieChart(self, data: pd.DataFrame, genres_type: str, selected_genres: List[str]):
        genres_count = self.getDataGenresCount(data, genres_type)
        df = pd.DataFrame({'title': genres_count.keys(), 'count': genres_count.values()}).\
            query('title == @selected_genres')
        pie_chart = px.pie(df, names='title', values='count', title=genres_type + ' genres')
        return pie_chart

    def preprocessingData(self, upload_file: str) -> Optional[pd.DataFrame]:
        if upload_file is not None:
            data = pd.read_csv(upload_file)
            data.rename(columns = {'Title Type': 'Title_Type'}, inplace = True)
            return data
