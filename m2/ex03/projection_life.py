from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt


def main(path1: str, path2: str, year: str = '1900'):
    try:
        pib = load(path1)
        life = load(path2)
        if pib is None or life is None:
            raise FileNotFoundError(f"File not found")
        elif pib.empty or life.empty:
            raise ValueError(f"Data is empty")

        pib_year = pib[year]
        life_year = life[year]
        sns.relplot(
            x=pib_year,
            y=life_year,
            height=4,
            aspect=2,
        )
        plt.xlabel("PIB par habitant")
        plt.ylabel("Esperance de vie")
        plt.title(f"Esperance de vie en fonction du PIB par habitant en {year}")
        plt.show()

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")

        


if __name__ == "__main__":
    main("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")
