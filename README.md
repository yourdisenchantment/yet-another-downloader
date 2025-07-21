# Stealth Image Downloader

Библиотека для надёжной загрузки изображений с различных веб-ресурсов, включая сайты с защитой от ботов.

## Особенности

- Поддержка различных форматов URL (HTTP, HTTPS, сокращённые URL)
- Автоматическая нормализация URL-адресов
- Два метода загрузки:
    - Стандартный с случайным User-Agent
    - Продвинутый с эмуляцией браузера для обхода защиты
- Автоматическое переключение между методами при неудаче

## Установка

```bash
# Установка из PyPI
pip install stealth-image-downloader

# Установка из исходного кода
git clone https://github.com/yourdisenchantment/stealth-image-downloader.git
cd stealth-image-downloader
poetry install
```

## Использование

```python
from yet_another_downloader import downloader

# Загрузка изображения
try:
    # Поддерживаются разные форматы URL
    image_data = downloader("//example.com/image.jpg")

    # Сохранение изображения
    with open("image.jpg", "wb") as file:
        file.write(image_data)

except Exception as error:
    print(f"Ошибка загрузки: {error}")
```

## Тестирование

Для запуска тестов выполните:

```bash
python -m tests.test
```

Тесты загрузят несколько изображений из разных источников и сохранят их в директории `tests/output/`.

## Требования

- Python 3.13+
- requests
- fake-useragent
- stealth-requests

## Структура проекта

```
stealth-image-downloader/
├── src/
│   └── stealth_image_downloader/
│       ├── utils/
│       │   └── utils.py    # Утилиты для обработки URL
│       ├── fetcher.py      # Методы загрузки
│       └── main.py         # Основной интерфейс
└── tests/
    └── test.py            # Тесты
```
