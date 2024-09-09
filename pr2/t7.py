import time

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import umap


def main():
    # 7. Выполнить визуализацию многомерных данных, используя UMAP
    # с различными параметрами n_neighbors и min_dist
    data = pd.read_csv("my_datasets/Wholesale customers data.csv")

    # исключение категориальных признаков
    region_labels = data["Region"]
    data.drop(["Region", "Channel"], axis=1)

    # предобработка данных
    scaler = StandardScaler()
    d = scaler.fit_transform(data)

    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    n_neigh = [5, 25, 50]
    min_dist = [0.1, 0.5]

    # разгогреть umap для точных замеров
    reducer = umap.UMAP(n_neighbors=3, min_dist=0.08, random_state=33, n_jobs=1)
    umap_results = reducer.fit_transform(d)

    for i, md in enumerate(min_dist):
        for j, nn in enumerate(n_neigh):
            # Измерение времени выполнения UMAP
            start_time = time.time()

            # Применение UMAP
            reducer = umap.UMAP(n_neighbors=nn, min_dist=md, random_state=33, n_jobs=1)
            umap_results = reducer.fit_transform(d)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"UMAP with n_neighbors={nn} and min_dist={md} took {elapsed_time:.2f} seconds"
            )

            # Добавление результатов UMAP в данные
            d = pd.DataFrame(umap_results, columns=["x", "y"])
            d["Region"] = region_labels

            # Визуализация с окраской точек по регионам
            sns.scatterplot(
                x="x", y="y", hue="Region", palette="bright", data=d, ax=axs[i, j]
            )
            axs[i, j].set_title(f"UMAP (n_neighbors={nn}, min_dist={md})")

            # Увеличение размера легенды
            legend = axs[i, j].legend()
            legend.set_bbox_to_anchor((1, 1))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
