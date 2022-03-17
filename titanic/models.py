from icecream import ic

from context.domains import Dataset
from context.models import Model

class TitanicModel(object):
    model = Model()
    dataset = Dataset()
    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_dframe(train_fname)
        self.test = self.model.new_dframe(test_fname)
        #ic(f'트레인 컬럼 {self.train.columns}')
        #ic(f'트레인 헤드 {self.train.head()}')
        # id 추출


    def preprocess(self):
        df = self.train
        ic(df)
        df = self.sibsp_garbage(df)
        df = self.parch_garbage(df)
        df = self.ticket_garbage(df)
        df = self.cabin_garbage(df)
        df = self.create_train(df)
        df = self.create_label(df)
        df = self.name_nominal(df)
        df = self.sex_nominal(df)
        df = self.age_ratio(df)
        df = self.embarked_nominal(df)
        df = self.pclass_ordinal(df)
        df = self.fare_ratio(df)
        return df

        @statcmethod
        def create_label(df)->object:
            return df

        @statcmethod
        def create_train(df)->object:
            return df

        def drop_feature(self, df) -> object:
            a = [i for i in []]

        self.preprocess(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.sib_sp_garbage(df)
        return df
    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''
    def pclass_ordinal(self)->object:
        pass

    def name_nominal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sib_sp_garbage(self) -> object:
        self.drop_feature()

    def parch_garbage(self) -> object:
        self.drop_feature()

    def ticket_garbage(self) -> object:
        pass

    def sex_nominal(self)->object:
        pass

    def cabin_garbage(self) -> object:
        pass

    def embarked_nominal(self) -> object:
        pass


    def fare_ratio(self) -> object:
        pass
