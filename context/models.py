from context.domains import Dataset
import pandas as pd


class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dname = './data/'
        this.sname = './save/'

    def new_dframe(self, fname) -> object:
        this = self.ds
        # pd.read_csv('경로/파일명.csv') Index 지정하지 않음
        return pd.read_csv(f'{this.dname}{fname}')

    def save_model(self, fname, dframe):
        this = self.ds
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
         '''
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')