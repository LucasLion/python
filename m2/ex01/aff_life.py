import seaborn as sns
import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt

def main(path: str) -> None:
    try:
        sns.set_theme()
        data = load(path)
        if data is None:
            raise FileNotFoundError(f"File '{path}' not found")
        elif data.empty:
            raise ValueError(f"Data in '{path}' is empty") 
        data_melted = pd.melt(
            data,
            id_vars=['country'],
            var_name='year',
            value_name='life_expectancy'
        )
        data_melted['year'] = data_melted['year'].astype(int)
        data_france = data_melted[data_melted['country'] == 'France']
        sns.relplot(
            data=data_france,
            x="year",
            y="life_expectancy",
            kind="line",
            height=4,
            aspect=1,
        )
        plt.title('France Life expectancy Projections')
        plt.show()
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main("life_expectancy_years.csv")

