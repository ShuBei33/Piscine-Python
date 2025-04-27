from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def millions_formatter(x, pos):
    """
    Format the Y axis ticks with an 'M' for millions.
    """
    return f"{int(x / 1_000_000)}M"


def main():
    """
    Load the population dataset, plot France and Belgium populations
    over time.

    Args:
        None

    Returns:
        pd.DataFrame: The filtered DataFrame containing France and Belgium
        population data.
    """

    df = load("population_total.csv")
    if df is None:
        return None

    df = df[df["country"].isin(["France", "Belgium"])]
    df = df.loc[:, ["country"] + list(df.loc[:, "1800":"2050"].columns)]
    years = df.columns[1:]

    pop_bel = df[df["country"] == "Belgium"].iloc[0, 1:]
    pop_fr = df[df["country"] == "France"].iloc[0, 1:]
    pop_bel = pop_bel.str.replace('M', '').astype(float) * 1_000_000
    pop_fr = pop_fr.str.replace('M', '').astype(float) * 1_000_000

    plt.plot(years, pop_bel, label='Belgium', color='#6CA6CD')
    plt.plot(years, pop_fr, label='France', color='#32CD32')
    plt.suptitle("")
    plt.title("Population Projections")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.yticks([20000000, 40000000, 60000000])
    plt.xticks(range(0, len(years), 40), labels=years[::40])
    # plt.legend()
    plt.legend(loc="lower right")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.show()
    return df


if __name__ == "__main__":
    main()
