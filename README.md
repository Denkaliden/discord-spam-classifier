# discord-spam-classifier
university project: spam classifier for discord/ ml bot

Университетский проект по разработке ML-модели для автоматической модерации сообщений в Discord.

* **Источник:** Выгрузка логов публичных серверов Discord (тематические каналы поиска игры, LOLRU Community).
* **Инструмент сбора:** [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) (формат CSV).
* **Объем:** ~2500 сообщений.
* **Воспроизводимость:** Сырые данные не правятся руками. Скрипт `src/prepare.py` реализует пайплайн raw -> processed (очистка от системного мусора, пустых строк и формирование файла для разметки).

## Структура проекта
* `src/` — исходный код.
    * `prepare.py` — скрипт первичной обработки сырых логов.
* `data/` — папка для данных (игнорируется Git).
    * `raw/` — сырые выгрузки от DiscordChatExporter.
    * `processed/` — очищенные данные для разметки.
