import time

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns


def main():
    # 6. Выполнить визуализацию многомерных данных, используя t-SNE.
    # Рассмотреть результаты визуализации для разных значений перплексии.
    data = pd.read_csv("my_datasets/Wholesale customers data.csv")

    # исключение категориальных признаков
    data.drop(["Region", "Channel"], axis=1)

    # предобработка данных
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    for perplexity in [5, 25, 50]:
        start_time = time.time()
        tsne = TSNE(n_components=2, perplexity=perplexity, random_state=123)
        tsne_results = tsne.fit_transform(scaled_data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"t-SNE with perplexity={perplexity} took {elapsed_time:.2f} seconds")
        d = data.copy()
        d["x"] = tsne_results[:, 0]
        d["y"] = tsne_results[:, 1]

        plt.figure(figsize=(10, 8))
        sns.scatterplot(x="x", y="y", hue=data["Region"], data=d, palette="bright")
        # plt.scatter(tsne_results 0], tsne_results[:, 1])
        plt.title(
            f"t-SNE Visualization of Wholesale Customers Data (perplexity = {perplexity})"
        )
        plt.show()


if __name__ == "__main__":
    main()
