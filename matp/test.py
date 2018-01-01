import matplotlib.pyplot as plt


def lineLayout():
    sq = [1, 4, 9, 16, 25]
    print(len(sq))
    input_value = list(range(1, len(sq) + 1))
    print(input_value)
    plt.plot(input_value, sq)
    plt.title('test')
    plt.xlabel("xTest", fontsize=14)
    plt.ylabel("yTest")
    plt.tick_params('both', labelsize=14)

    plt.show()


def scat():
    x_value = [1, 2, 3, 4, 5]
    y_value = [1, 4, 9, 16, 25]
    plt.scatter(x_value, y_value, s=10)
    # plt.show()
    plt.savefig('plot.png')


def scats():
    x_value = list(range(1, 1001))
    y_value = [x ** 2 for x in x_value]
    plt.scatter(x_value, y_value)
    plt.axis([0, 1100, 0, 1100000])
    plt.show()


def X2():
    pass


if __name__ == '__main__':
    # scat()
    X2()
