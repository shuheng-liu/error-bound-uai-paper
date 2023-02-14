import matplotlib.pyplot as plt

def setup():
    # import seaborn as sns
    # sns.set()
    params = {
        "ytick.color": "black",
        "xtick.color": "black",
        "axes.labelcolor": "black",
        "axes.edgecolor": "black",
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern Serif"],
    }
    plt.rcParams.update(params)
