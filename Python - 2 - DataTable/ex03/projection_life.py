from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Load GDP and life expectancy data for the year 1900.

    The function loads two CSV files: one for GDP per capita and one for life
    expectancy. It filters the data for the year 1900, renames the columns for
    clarity, merges the datasets on country, cleans missing or invalid entries,
    and plots a scatter plot with GDP (log scale) on the x-axis and life
    expectancy on the y-axis.

    Args:
        None

    Returns:
        pd.DataFrame: The merged and filtered DataFrame used for plotting.
    """

    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    df_life = load("life_expectancy_years.csv")
    if df_life is None or df_income is None:
        return None
    df_income = df_income[["country", "1900"]]
    df_income.columns = ["country", "gdp"]
    df_life = df_life[["country", "1900"]]
    df_life.columns = ["country", "life_expectancy"]
    df_merge = pd.merge(df_income, df_life, on="country")
    df_merge = df_merge.dropna()  # del lines without gdp or life_ex
    df_merge = df_merge[df_merge["gdp"] > 0]  # del countries gdp null

    plt.scatter(
        x=df_merge["gdp"],
        y=df_merge["life_expectancy"]
    )
    plt.xscale("log")
    plt.xticks(
        ticks=[300, 1000, 10000],
        labels=["300", "1k", "10k"]
    )
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()
    return df_merge


if __name__ == "__main__":
    main()
