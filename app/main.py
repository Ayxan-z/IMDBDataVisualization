from app import App
import pandas as pd


class Main():
    def __init__(self):
        self.app = App(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')
        data = self.uploadFile()
        self.sideBar(data)
        
        self.addStyle()

    def sideBar(self, data: pd.DataFrame):
        data_genres_count = self.app.getDataGenresCount(data, 'all')
        genres_radio_btn = self.app.st.sidebar.radio('', ['All', 'Movie', 'Series'])
        graphics_radio_btn = self.app.st.sidebar.radio('', ['Pie Chart', 'Bar Chart'])
        # radio buttons vertical to horizontal
        # self.app.st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # self.app.st.sidebar.header('Data by Genre:')
        data_genre_filter = self.app.st.sidebar.multiselect(
            'Select Genre:',
            options = data_genres_count.keys(),
            default = data_genres_count.keys()
        )

        if data is not None:
            try:
                if graphics_radio_btn == 'Pie Chart':
                    self.app.st.plotly_chart(self.app.createPieChart(data, genres_radio_btn, data_genre_filter))
                else:
                    self.app.st.plotly_chart(self.app.createBarChart(data, genres_radio_btn, data_genre_filter))
            except: pass

    def uploadFile(self) -> pd.DataFrame:
        uploaded_file = 'app\\WATCHLIST.csv' # app.st.file_uploader("Choose a file")
        data = self.app.preprocessingData(uploaded_file)
        return data
    
    def addStyle(self):
        hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
        self.app.st.markdown(hide_st_style, unsafe_allow_html=True)