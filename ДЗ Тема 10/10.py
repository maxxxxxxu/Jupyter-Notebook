# Импортируем необходиые библитеки
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Загружаем данные из JSON-файла
file_path = "events.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Преобразовываем данные в DataFrame
df = pd.DataFrame(data["events"])

# Производим визуализацию данных по типам события
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="signature", order=df["signature"].value_counts().index)
plt.title("Распределение событий по типам")
plt.xlabel("Количество")
plt.ylabel("Тип события")
plt.show()