import contextlib
from data_preprocessing import DataPreprocessing
import pandas as pd
import streamlit as st


class Main():
    def __init__(self):
        self.st = st
        self.st.set_page_config(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')
        self.sideBar(self.uploadFile())
        self.addStyle()

    def sideBar(self, data: pd.DataFrame):
        data_genres_count = DataPreprocessing.getDataGenresCount(data, 'all')
        genres_radio_btn = self.st.sidebar.radio('', ['All', 'Movie', 'Series'])
        graphics_radio_btn = self.st.sidebar.radio('', ['Pie Chart', 'Bar Chart'])
        # radio buttons vertical to horizontal
        self.st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # self.st.sidebar.header('Data by Genre:')
        data_genre_filter = self.st.sidebar.multiselect(
            'Select Genre:',
            options = data_genres_count.keys(),
            default = data_genres_count.keys()
        )

        if data is not None:
            with contextlib.suppress(Exception):
                if graphics_radio_btn == 'Pie Chart':
                    self.st.plotly_chart(DataPreprocessing.createPieChart(data, genres_radio_btn, data_genre_filter))
                else:
                    self.st.plotly_chart(DataPreprocessing.createBarChart(data, genres_radio_btn, data_genre_filter))

    def uploadFile(self) -> pd.DataFrame:
        uploaded_file = 'app/WATCHLIST.csv' # self.st.file_uploader("Choose a file")
        return DataPreprocessing.preprocessingData(uploaded_file)
    
    def addStyle(self):
        hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
        self.st.markdown(hide_st_style, unsafe_allow_html=True)