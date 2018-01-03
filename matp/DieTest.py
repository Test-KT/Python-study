from random import randint
import pygal


class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


if __name__ == '__main__':

    d = Die()
    d2 = Die()
    results = []
    results2 = []
    for i in range(100):
        result = d.roll()
        result2 = d2.roll()
        results.append(result)
        results2.append(result2)
    fres = []
    fres2 = []
    for v in range(1, d.num_sides + 1):
        fre = results.count(v)
        fre2 = results2.count(v)
        fres.append(fre)
        fres2.append(fre2)
    print(fres)
    print(fres2)

    hist = pygal.StackedBar()
    hist.title = 'title'
    hist.x_title = 'x_title'
    hist.y_title = 'y_title'
    hist.x_labels = ['1', '2', '3', '4', '5', '6']

    hist.add('Roll1', fres)
    hist.add('Roll2', fres2)

    hist.render_to_file('die.svg')
