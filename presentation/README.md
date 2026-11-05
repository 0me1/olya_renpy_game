# Презентация для Оли

8 слайдов 16:9 для показа перед запуском игры «В порядке перевода». Заметки выступающего встроены в PPTX; рассказ рассчитан примерно на 3 минуты. Текст на слайдах редактируется в PowerPoint. Графика взята из проекта; сюжет финалов и объяснение переходов не раскрываются.

Готовые файлы:

- [PPTX](../downloads/olya_birthday_presentation.pptx)
- [PDF](../downloads/olya_birthday_presentation.pdf)
- [Текст выступления](../downloads/olya_birthday_speaker_notes.txt)

Для пересборки нужны Python, python-pptx, Pillow. Из корня репозитория: `python3 presentation/build_deck.py`. Временные изображения создаются в `/workspace/presentation_build`. Для PDF нужен LibreOffice: `soffice --headless --convert-to pdf --outdir downloads downloads/olya_birthday_presentation.pptx`. В PPTX используются Georgia и Arial; PDF сохраняет внешний вид экспорта.

Источники: пролог и главы в `game/chapters/`, актуальное название в `game/options.rpy`, фоны в `game/images/backgrounds`, спрайты в `game/images_normalized/olya`, иконка в `art_sources/icon`, панели в `game/gui/worlds`. Пример двух решений и реплика Оли взяты из начала `04_minecraft.rpy`.

Проверка: 8 страниц PDF, формат 16:9, 8 наборов заметок, весь текст слайдов сохранен при экспорте, буква с двумя точками отсутствует. Все слайды просмотрены после экспорта; проверены подписи, края персонажей, контраст и отсутствие спойлеров.
