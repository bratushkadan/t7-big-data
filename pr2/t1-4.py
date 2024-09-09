import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

if __name__ == "__main__":
    # 1. загрузить датасет
    df = pd.read_csv("my_datasets/titanic.csv")

    # 2. вывести информацию о датасете
    df.info()

    # 2. вывести первые 10 записей датасета
    print(df.head(10))

    # 2 выяснить, есть ли пропущенные значения в датасете
    # если больше 0 в каком-то из столбцов - есть пропущенное значение
    missing_values = df.isna().sum()

    if missing_values.any():
        print("Пропущены значения", missing_values)

        # 2. Удаление строк с пропущенными значениями
        df = df.dropna()
        print("Пропущенные значения были удалены.")

        # 2. Или интерполяция (замена) пропущенных значений
        # df_interpolated = df.fillna(df.mean())
        # print("Пропущенные значения были интерполированы.")

    # 2. предобработка данных для дальнейшей работы
    # one-hot encoding столбцов Pclass (пассажирский класс) и Sex (пол),
    # имеющих 3 и 2 различных значений соответственно
    # df = pd.get_dummies(df, columns=["Pclass"])
    # df.info()  # Pclass -> Pclass_1, Pclass_2, Pclass_3 | Sex -> Sex_female, Sex_male

    # 3.

    # (опционально - отфильтровать df по признаку)
    # df = df[df["Survived"] == 0]
    # df = df[df["Sex"] == "female"]

    # Группировка данных по возрасту и подсчет количества людей в каждом возрасте
    age_counts = (
        df["Age"].value_counts().sort_index()
    )  # Группировка данных по возрасту и подсчет количества людей в каждом возрасте

    fig = go.Figure(
        data=[
            go.Bar(
                # 3.1 По оси Х указать дату или название (возраст),
                # 3.2 по оси У указать количественный показатель (к-во людей возраста)
                x=age_counts.index,
                y=age_counts.values,
                marker=dict(
                    # 3.2 Сделать так, чтобы столбец принимал цвет
                    # в зависимости от значения показателя
                    color=age_counts.values,
                    coloraxis="coloraxis",
                    # 3.3 Сделать так, чтобы границы каждого столбца были
                    # выделены чёрной линией с толщиной равной 2.
                    line=dict(color="black", width=0.33),
                ),
            )
        ]
    )

    fig.update_layout(
        title=dict(
            text="Age Distribution",
            font=dict(size=20),
            x=0.5,
            xanchor="center",  # 3.4. Отобразить заголовок диаграммы, разместив его по центру сверху, с 20 размером текста.
        ),
        xaxis=dict(
            title=dict(
                text="Name", font=dict(size=16)
            ),  # 3.5 Добавить подписи для осей X и Y с размером текста, равным 16.
            tickangle=315,  # 3.5. Для оси абсцисс развернуть метки так, чтобы они читались под углом, равным 315.
            tickfont=dict(size=14),  # 3.6 Размер текста меток осей сделать равным 14.
            showgrid=True,
            gridwidth=2,
            gridcolor="ivory",
        ),
        yaxis=dict(
            title=dict(text="Age", font=dict(size=16)),
            tickfont=dict(size=14),  # 3.6 Размер текста меток осей сделать равным 14.
            showgrid=True,
            gridwidth=2,  # 3.8 Добавить сетку на график, сделать её цвет 'ivory' и толщину равную 2.
            gridcolor="ivory",
        ),
        coloraxis=dict(colorscale="Viridis"),
        width=1900,  # 3.7 Расположить график во всю ширину рабочей области
        # и присвоить высоту, равную 700 пикселей.
        height=700,
        margin=dict(l=0, r=0, t=50, b=0),  # 3.9 Убрать лишние отступы по краям.
    )

    # 3. записать график в файл
    fig.write_image("t3-chart.png", engine="kaleido")

    # 4.
    # Создаем интервалы как для гистограммы
    bins = [0, 9, 19, 29, 39, 49, 59, 100]
    labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-100"]

    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

    age_group_counts = df["AgeGroup"].value_counts().sort_index()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=age_group_counts.index,
                values=age_group_counts.values,
                marker=dict(line=dict(color="black", width=2)),  # Границы секций
                textinfo="label+percent",  # Информация о секциях: метка и процент
                insidetextorientation="radial",  # Ориентация текста внутри секций
            )
        ]
    )

    fig.update_layout(
        title=dict(
            text="Distribution of People by Age",
            font=dict(size=20),
            x=0.5,
            xanchor="center",
        ),
        width=1200,
        height=700,
        margin=dict(l=0, r=0, t=50, b=0),  # Убираем лишние отступы
    )

    # 4. записать график в файл
    fig.write_image("t4-chart.png", engine="kaleido")
