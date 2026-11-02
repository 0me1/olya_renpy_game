init -2 python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

define config.name = "В порядке перевода"
define config.version = "0.1.0"
define config.save_directory = "olya-v-poryadke-perevoda"
define config.window = "auto"
define config.rollback_enabled = True
define config.has_autosave = True
define config.has_quicksave = True
define config.default_text_cps = 35
define config.default_afm_time = 12
define config.history_length = 250
define config.audio_filename_callback = None

define build.name = "V_Poryadke_Perevoda"
define build.directory_name = "V_Poryadke_Perevoda-0.1.0"
init python:
    build.classify('**.rpyc', None)
    build.classify('docs/**', None)
    build.classify('tools/**', None)
    build.classify('tests/**', None)
    build.classify('**.md', None)
    build.classify('**.log', None)
    build.classify('game/*_tests.rpy', None)
    build.classify('game/test_support.rpy', None)
    build.classify('AGENTS.md', None)
    build.classify('tests/**', None)
    build.classify('game/test_results/**', None)
    build.classify('game/test_screenshots/**', None)

style default:
    font "DejaVuSans.ttf"
    size 32
    color "#f7efdf"
style button:
    padding (24, 14)
    background Solid("#24313f")
    hover_background Solid("#92506a")
    insensitive_background Solid("#26303a")
style button_text:
    color "#f7efdf"
    hover_color "#ffffff"
    insensitive_color "#74808b"
    selected_color "#ffc79c"
    size 30
style bar:
    xsize 550
    ysize 28
    left_bar Solid("#d2938f")
    right_bar Solid("#354452")
    thumb Solid("#fff1d9")
    thumb_shadow None
    thumb_offset 8
style scrollbar:
    xsize 14
    base_bar Solid("#354452")
    thumb Solid("#d2938f")
style slider is bar

init 10 python:
    _confirm_ru = {
        "ARE_YOU_SURE": "Подтвердить действие?",
        "DELETE_SAVE": "Удалить это сохранение?",
        "OVERWRITE_SAVE": "Перезаписать это сохранение?",
        "LOADING": "Загрузить игру? Несохраненный прогресс будет потерян.",
        "QUIT": "Выйти из игры?",
        "MAIN_MENU": "Вернуться в главное меню? Несохраненный прогресс будет потерян.",
        "CONTINUE": "Продолжить с последнего сохранения?",
        "END_REPLAY": "Закончить просмотр эпилога?",
        "SLOW_SKIP": "Начать пропуск прочитанного текста?",
        "FAST_SKIP_SEEN": "Перейти к следующему выбору?",
        "FAST_SKIP_UNSEEN": "Пропустить непрочитанный текст до следующего выбора?",
    }
    for _key, _value in _confirm_ru.items():
        setattr(layout, _key, _value)
        setattr(gui, _key, _value)
