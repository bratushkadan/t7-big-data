import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

if __name__ == "__main__":
    df = pd.read_csv("my_datasets/titanic.csv")

    missing_values = df.isna().sum()

    if missing_values.any():
        df = df.dropna()

    # 5.
    # Определение зависимости между 'Survived' и другими параметрами
    age_bins = np.arange(0, 81, 5)
    df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins)

    df_male = df[df["Sex"] == "male"]
    df_female = df[df["Sex"] == "female"]

    age_group_survival = df.groupby("AgeGroup")["Survived"].mean()
    age_group_survival_male = df_male.groupby("AgeGroup")["Survived"].mean()
    age_group_survival_female = df_female.groupby("AgeGroup")["Survived"].mean()

    # возрастные интервалы (0-5,...)
    age_group_labels = [
        f"{int(b.left)}-{int(b.right)}" for b in age_group_survival.index.categories
    ]

    plt.figure(figsize=(15, 9))
    plt.plot(
        age_group_labels,
        age_group_survival,
        marker="o",
        linestyle="-",
        color="g",
        label="Male/Female",
        markerfacecolor="white",
        markeredgewidth=2,
        markeredgecolor="black",
    )

    plt.plot(
        age_group_labels,
        age_group_survival_male,
        marker="o",
        linestyle="-",
        color="b",
        label="Male",
        markerfacecolor="white",
        markeredgewidth=2,
        markeredgecolor="black",
    )

    plt.plot(
        age_group_labels,
        age_group_survival_female,
        marker="o",
        linestyle="-",
        color="crimson",
        label="Female",
        markerfacecolor="white",
        markeredgewidth=2,
        markeredgecolor="black",
    )

    plt.xlabel("Age Group")
    plt.ylabel("Survival Rate")
    plt.title("Survival Rate by Age Group")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linewidth=2, color="mistyrose")  # 5.2 настройка сетки
    plt.show()

    # средняя выживаемость по пассажирским классам по полам
    pclass_sex_survival = df.groupby(["Pclass", "Sex"])["Survived"].mean().unstack()

    fig, ax = plt.subplots(1, 2, figsize=(24, 10))

    pclass_sex_survival.plot(kind="bar", ax=ax[0], color=["red", "blue"])
    ax[0].set_xlabel("Pclass")
    ax[0].set_ylabel("Survival Rate")
    ax[0].set_xticklabels(["Class 1", "Class 2", "Class 3"], rotation=0)
    ax[0].set_title("Survival Rate by Pclass and Sex (Bar Chart)")
    ax[0].grid(axis="y")

    pclass_survival = df.groupby("Pclass")["Survived"].mean()
    ax[1].plot(
        pclass_survival.index,
        pclass_survival.values,
        marker="o",
        linestyle="-",
        color="crimson",
        markerfacecolor="white",
        markeredgewidth=2,
        markeredgecolor="black",
    )
    ax[1].set_xlabel("Pclass")
    ax[1].set_ylabel("Survival Rate")
    ax[1].set_title("Survival Rate by Pclass (Line Chart)")
    ax[1].set_xticks([1, 2, 3])
    ax[1].set_xticklabels(["Class 1", "Class 2", "Class 3"], rotation=0)
    ax[1].grid(True, linewidth=2, color="mistyrose")

    # Показываем графики
    plt.tight_layout()
    plt.show()
