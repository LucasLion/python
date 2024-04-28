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
            var_name='Year',
            value_name='Population',
        )
        data_melted['Year'] = data_melted['Year'].astype(int)
        data_melted['Population'] = data_melted['Population'].apply(clean_population)
        data_selected = data_melted[(data_melted['Year'] <= 2050) & (data_melted['country'].isin(['France', 'Belgium']))]
        g = sns.lineplot(
            data=data_selected,
            x="Year",
            y="Population",
            hue="country",
        )
        #g.set_axis_labels("Annee,", "Population")
        g.set(title='Projections de Population', xlim=(1800, 2050))
        g.legend(loc='lower right')
        pop_legend = ['20M', '40M', '60M']
        plt.yticks([20000000, 40000000, 60000000], pop_legend)
        plt.xlim(1795, 2060)
        plt.show()

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Eroror: {str(e)}")


if __name__ == "__main__":
    main("population_total.csv")
