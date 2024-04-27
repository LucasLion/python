import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def clean_population(population_str):
    multiplier = 1
    if population_str.endswith('M'):
        multiplier = 1000000
        population_str = population_str.replace('M', '')
    elif population_str.endswith('B'):
        multiplier = 1000000000
        population_str = population_str.replace('B', '')
    elif population_str.endswith('k'):
        multiplier = 1000
        population_str = population_str.replace('k', '')
    return int(float(population_str) * multiplier)


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
        data_melted['Population'] = data_melted['Population'].apply(clean_population)
        data_selected = data_melted[data_melted['country'].isin(['France', 'Belgium'])]
        g = sns.relplot(
            data=data_selected,
            x="year",
            y="Population",
            hue="country",
            kind="line",
            height=4,
            aspect=2,
        )
        g.set_axis_labels("Annee,", "Population")
        g.set(title='Projections de Population', xlim=(1800, 2050))
        plt.show()
        print(data_selected['Population'])

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Eroror: {str(e)}")


if __name__ == "__main__":
    main("population_total.csv")
