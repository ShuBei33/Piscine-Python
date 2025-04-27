import pandas as pd


def err_handling(path):
    """
    Safely loads a CSV file using pandas.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame or None:
        The loaded DataFrame, or None if an error occurred.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: file not found → {path}")
    except pd.errors.EmptyDataError:
        print(f"Error: the file is empty → {path}")
    except pd.errors.ParserError:
        print(f"Error: the file is not a valid CSV → {path}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None


def load(path: str):
    """
    Wrapper function to load a CSV file and print its shape if successful.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame or None: The loaded DataFrame, or None if loading failed.
    """
    df = err_handling(path)
    if df is not None:
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    else:
        return None
