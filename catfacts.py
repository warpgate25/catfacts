import requests

def main():
    # 1. Получаем первую страницу фактов
    url = "https://catfact.ninja/facts"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # 2. Узнаём общее количество фактов и сколько на странице
    total = data["total"]
    per_page = data["per_page"]

    # 3. Вычисляем последнюю страницу
    last_page = (total + per_page - 1) // per_page

    # 4. Получаем последнюю страницу
    response_last = requests.get(url, params={"page": last_page})
    response_last.raise_for_status()
    last_page_data = response_last.json()["data"]

    # 5. Находим самый короткий факт
    shortest_fact = min(last_page_data, key=lambda x: len(x["fact"]))
    print("Самый короткий факт с последней страницы:")
    print(shortest_fact["fact"])

if __name__ == "__main__":
    main()
