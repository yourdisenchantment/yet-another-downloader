# tests/test.py

import os

from src.yet_another_downloader.main import downloader


def test_multiple_downloads():
    """Тестирует загрузку нескольких изображений из разных источников.

    Функция пытается загрузить тестовый набор изображений с различных хостингов, используя разные форматы URL (с протоколом и без). Сохраняет загруженные изображения в директорию 'output' с последовательной нумерацией.

    В случае успешной загрузки каждое изображение сохраняется как 'image_N.jpg', где N - порядковый номер изображения. При возникновении ошибок выводит соответствующее сообщение, но продолжает загрузку остальных изображений.

    :return:
    :rtype:
    """

    test_urls = [
        "//avatars.mds.yandex.net/i?id=b8e5c867c94ad050de65a7704bb5ef48_l-5593492-images-thumbs&n=13",
        "https://upload.wikimedia.org/wikipedia/commons/4/44/Brown_Rat_%28Rattus_norvegicus%29.jpg",
        "//external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fres.cloudinary.com%2Fdk-find-out%2Fimage%2Fupload%2Fq_80%2Cw_1440%2Cf_auto%2F50491001_kupidw.png&f=1&nofb=1&ipt=e58036a8ead7e410546f4751bd9026d3a74cd0bf1fc1858a28b9e2a119fb2a63",
        "https://th.bing.com/th/id/R.d960a815a8de3ec1609f587f746509b0?rik=dIS35l6IIRJ%2fbA&pid=ImgRaw&r=0",
    ]

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for i, url in enumerate(test_urls):
        try:
            image_data = downloader(url)
            output_path = os.path.join(output_dir, f"image_{i + 1}.jpg")

            with open(output_path, "wb") as file:
                file.write(image_data)

            print(f"Изображение {i + 1} сохранено: {output_path}")

        except Exception as error:
            print(f"Ошибка при загрузке изображения {i + 1}: {error}")


if __name__ == "__main__":
    test_multiple_downloads()
