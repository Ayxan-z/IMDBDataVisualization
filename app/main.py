from app import App
import pandas as pd


class Main():
    def __init__(self):
        self.app = App(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')
        data = self.uploadFile()
        selected_genres = self.sideBar(data)
        if data is not None:
            self.app.st.plotly_chart(self.app.createPieChart(data, 'All', selected_genres))
            # self.app.st.plotly_chart(self.app.createPieChart(data, 'Movie', selected_genres))
            # self.app.st.plotly_chart(self.app.createPieChart(data, 'Series'))

    def sideBar(self, data: pd.DataFrame):
        data = self.app.getDataGenresCount(data, 'all')
        self.app.st.sidebar.header('Data by Genre:')
        data_genre_filter = self.app.st.sidebar.multiselect(
            'Select Genre:',
            options = data.keys(),
            default = data.keys()
        )

        return data_genre_filter

    def uploadFile(self) -> pd.DataFrame:
        uploaded_file = 'app\\WATCHLIST.csv' # app.st.file_uploader("Choose a file")
        data = self.app.preprocessingData(uploaded_file)
        return data


if __name__ == '__main__': Main()