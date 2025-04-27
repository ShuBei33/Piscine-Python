from load_csv import load
# import matplotlib
# matplotlib.use("TkAgg")  # enlever avant correction !!!!!!
import matplotlib.pyplot as plt


def main():
    """
    Filter a DataFrame to keep only the rows matching a specific country.

    Args:
        df (pd.DataFrame): The DataFrame containing a 'country' column.
        country_name (str): The name of the country to select.

    Returns:
        pd.DataFrame: The filtered DataFrame containing only the specified
        country.
    """

    df = load("life_expectancy_years.csv")
    if df is None:
        return None
    df = df[df["country"] == "France"]
    years = df.columns[1:]
    values = df.iloc[0, 1:]  # by position, first line, second columns
    plt.plot(years, values)
    plt.title("France Life expectancy Projections")
    plt.xlabel('Year')
    plt.ylabel("Life expectancy")
    plt.xticks(years[::40])
    plt.show()
    return df


if __name__ == "__main__":
    main()
