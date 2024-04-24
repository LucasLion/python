import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except pd.errors.ParserError:
        print(f"Error: Impossible to read file '{path}'. Check format")
        return None
