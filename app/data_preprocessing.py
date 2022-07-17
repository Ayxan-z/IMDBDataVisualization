import pandas as pd
import plotly.express as px
from collections import Counter
from typing import Optional, List


class DataPreprocessing:
    @staticmethod
    def getDataGenresCount(data: pd.DataFrame, genres_type: str) -> Counter:
        if genres_type == 'Movie':
            data = data.query("Title_Type == 'movie' or Title_Type == 'tvMovie'")
        elif genres_type == 'Series':
            data = data.query("Title_Type == 'tvSeries' or Title_Type == 'tvMiniSeries'")

        data_genres = pd.DataFrame({'title': data['Title'], 'genres': data['Genres']})

        genres = []
        for i in data_genres['genres']:
            genres += i.replace(' ', '').split(',')
        return Counter(genres)

    @staticmethod
    def createPieChart(data: pd.DataFrame, genres_type: str, selected_genres: List[str]):
        genres_count = DataPreprocessing.getDataGenresCount(data, genres_type)
        if len(selected_genres) < 2: return None
        df = pd.DataFrame({'title': genres_count.keys(), 'count': genres_count.values()}).\
            query('title == @selected_genres')
        return px.pie(df, names='title', values='count', title=f'{genres_type} genres')

    @staticmethod
    def createBarChart(data: pd.DataFrame, genres_type: str, selected_genres: List[str]):
        genres_count = DataPreprocessing.getDataGenresCount(data, genres_type)
        if len(selected_genres) < 2: return None
        genres_count_selected = {i: j for i, j in genres_count.items() if i in selected_genres}
        return px.bar(x=genres_count_selected.keys(), y=genres_count_selected.values())

    @staticmethod
    def preprocessingData(upload_file: str) -> Optional[pd.DataFrame]:
        if upload_file is not None:
            data = pd.read_csv(upload_file)
            data.rename(columns = {'Title Type': 'Title_Type'}, inplace = True)
            return data
