import pandas as pd
import plotly.express as px
from collections import Counter
import streamlit as st


st.set_page_config(page_title='Dashboard',
                    page_icon=':bar_chart:',
                    layout='wide')


uploaded_file = 'app\\WATCHLIST.csv' # st.file_uploader("Choose a file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    data.rename(columns = {'Title Type': 'Title_Type'}, inplace = True)

    # ======================================== All ========================================

    data_all = pd.DataFrame({'title': data['Title'], 'genres': data['Genres']})

    genres_all = []
    for i in data_all['genres']:
        genres_all += i.replace(' ', '').split(',')
    genres_all_count = Counter(genres_all)

    # ======================================== tvSeries, tvMiniSeries ========================================

    data_series = data.query("Title_Type == 'tvSeries' or Title_Type == 'tvMiniSeries'")
    data_series = pd.DataFrame({'title': data_series['Title'], 'genres': data_series['Genres']})

    genres_series = []
    for i in data_series['genres']:
        genres_series += i.replace(' ', '').split(',')
    genres_series_count = Counter(genres_series)

    # ======================================== movie, tvMovie ========================================

    data_movie = data.query("Title_Type == 'movie' or Title_Type == 'tvMovie'")
    data_movie = pd.DataFrame({'title': data_movie['Title'], 'genres': data_movie['Genres']})

    genres_movie = []
    for i in data_movie['genres']:
        genres_movie += i.replace(' ', '').split(',')
    genres_movie_count = Counter(genres_movie)

    genres_all_pie_chart = px.pie(pd.DataFrame({'title': genres_all_count.keys(), 'count': genres_all_count.values()}),
            names='title', values='count', title='All genres')

    st.plotly_chart(genres_all_pie_chart)