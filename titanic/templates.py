from context.domains import Dataset
from context.models import Model
from icecream import ic
import matplotlib.pyplot as plt

class TitanicTemplate(object):
    dataset = Dataset()
    model - Model()
    def __init__(self,fname):
        self.entity = self.model.new_model(fname)
        ic(f'트레인의 타입:{type(this)}')
        ic(f'트레인의 컬럼:{this.columns}')
        ic(f'트레인의 상위5행: {this.head()}')
        ic(f'트레인의 하위5행: {this.tail()}')
    def visualize(self)-> None:
        this = self.entity
        self.draw_survived(this)
        self.draw_pclass(this)
        self.draw_sec(this)
        self.draw_embarked(this)
    @staticmethod
    def draw_survied_dead(this)-> None:
        f, ax = plt.subplots(1,2, figsize=(18,8))
        this['Survived']
        plt.show()

    @staticmethod
    def draw_pclass(this) -> None:
        plt.show()

    @staticmethod
    def draw_sex(this) -> None:
        plt.show()

    @staticmethod
    def draw_embarked(this) -> None:
        plt.show()

