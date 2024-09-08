from sklearn.datasets import fetch_california_housing

if __name__ == "__main__":
    print("7. Скачать и загрузить данные о стоимости домов в калифорнии")
    data = fetch_california_housing(as_frame=True)
    df = data.frame

    print("\n8. Использовать метод info().")
    info = df.info()

    print("\n9. Узнать, есть ли пропущенные значения")
    print(df.isna().sum())  # пропущенных значений нет (после "memory usage: 1.4MB...")

    print(
        "\n10. Вывести записи, где средний возраст домов в районе более 50 лет и население более 2500 человек, используя метод loc()."
    )
    cond = (df["HouseAge"] > 50) & (df["Population"] > 2500)

    filtered_df = df.loc[cond]
    print(filtered_df)

    print("\n11. Узнать максимальное и минимальное значения медианной стоимости дома.")
    print(
        f"Максимальное значение медианной стоимости домов: {df['MedHouseVal'].max()}\nМинимальное значение медианной стоимости домов: {df['MedHouseVal'].min()}"
    )

    print(
        "\n12. Используя метод apply(), вывести на экран название признака и его среднее значение"
    )
    # apply() позволяет применить пользовательскую функцию к каждой строке или каждому столбцу
    calc_mean_fn = lambda col: f"{col.name}: {col.mean()}"

    # axis=0 - столбцы
    print(df.apply(calc_mean_fn, axis=0))
