import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main(path: str):
    try:
        data = load(path)
        if data is None:
            raise FileNotFoundError(f"File '{path}' not found")
        elif data.empty:
            raise ValueError(f"Data in '{path}' is empty") 
        data_melted = pd.melt(
            data,
            id_vars=['country'],
            var_name='year',
            value_name='Population',
        )
        data_melted['year'] = data_melted['year'].astype(int)
        data_selected = data_melted[data_melted['country'].isin(['France', 'Belgium'])]
        sns.relplot(
            data=data_selected,
            x="year",
            y="Population",
            hue="country",
            kind="line",
            height=4,
            aspect=2,
        )
        sns.axes_style(
            {
                'axes.grid': True,
                'text.color': 'green',
            }
        )
        plt.title('Population Projections')
        plt.xlim(1800, 2050)
        plt.show()
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Eroror: {str(e)}")


if __name__ == "__main__":
    main("population_total.csv")
