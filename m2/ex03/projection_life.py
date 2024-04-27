from load_csv import load


def main(path1: str, path2: str):
    pib = load(path1)
    life = load(path2)

    print(pib['1900'])
    print(life['1900'])


if __name__ == "__main__":
    main("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")
