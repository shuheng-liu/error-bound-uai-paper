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
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "xtick.labelsize": 16,
        "ytick.labelsize": 16,
        "legend.framealpha": 0.0,
        "legend.frameon": False,
    }
    plt.rcParams.update(params)