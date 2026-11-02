# Functional routes. Explicit selection avoids running these in player builds.
testsuite routes:
    testcase home_0:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Подписать возвращение домой'
        advance until screen "choice"
        assert eval bonus_available()
        click "Оставить дверь открытой — увидеть бонусный эпилог"
        advance until screen "ending_result"
        assert eval current_ending == "open_door"
        assert eval "home" in persistent.unlocked_endings
        assert eval "open_door" in persistent.unlocked_endings
    testcase home_1:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Мне нужен перерыв'
        advance until screen "choice"
        click 'Проверить телефон'
        advance until screen "choice"
        click 'Спросить Бри напрямую'
        advance until screen "choice"
        click 'Устроить спокойный разговор без публики'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Попросить Миранду разобрать договоренности'
        advance until screen "choice"
        click 'Отказаться от одной просьбы и предложить замену'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Разобрать предложение Картмана'
        advance until screen "choice"
        click 'Развести мероприятия по времени и отменить ловушку штрафов'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Идти к деревне до темноты'
        advance until screen "choice"
        click 'Собрать детали самостоятельно'
        advance until screen "choice"
        click 'Переждать в укрытии'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Провести собственный эксперимент'
        advance until screen "choice"
        click 'Отменить команды и составить собственную очередь'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Проверить условие вместе с Вонгом'
        advance until screen "choice"
        click 'Сначала испытать небольшой собственный знак'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Подписать возвращение домой'
        advance until screen "choice"
        assert eval bonus_available()
        click "Оставить дверь открытой — увидеть бонусный эпилог"
        advance until screen "ending_result"
        assert eval current_ending == "open_door"
        assert eval "home" in persistent.unlocked_endings
        assert eval "open_door" in persistent.unlocked_endings
    testcase home_2:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Посмотрю, что там вообще'
        advance until screen "choice"
        click 'Поставить пирог'
        advance until screen "choice"
        click 'Проверить обстоятельства вместе с Габи'
        advance until screen "choice"
        click 'Прикрыть Сьюзан и самой организовать перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Собрать людей на одной встрече'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Пусть организаторы испытают собственные уведомления'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Подготовить факелы и безопасный проход'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Изменить условия дома, чтобы команда потеряла смысл'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Подписать возвращение домой'
        advance until screen "choice"
        assert eval bonus_available()
        click "Оставить дверь открытой — увидеть бонусный эпилог"
        advance until screen "ending_result"
        assert eval current_ending == "open_door"
        assert eval "home" in persistent.unlocked_endings
        assert eval "open_door" in persistent.unlocked_endings
    testcase stay_housewives:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Мне нужен перерыв'
        advance until screen "choice"
        click 'Проверить телефон'
        advance until screen "choice"
        click 'Спросить Бри напрямую'
        advance until screen "choice"
        click 'Устроить спокойный разговор без публики'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Остаться на Вистерия-Лейн — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_housewives'
        assert eval current_ending in persistent.unlocked_endings
    testcase stay_manhattan:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Посмотрю, что там вообще'
        advance until screen "choice"
        click 'Поставить пирог'
        advance until screen "choice"
        click 'Проверить обстоятельства вместе с Габи'
        advance until screen "choice"
        click 'Прикрыть Сьюзан и самой организовать перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Собрать людей на одной встрече'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Остаться на Манхэттене — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_manhattan'
        assert eval current_ending in persistent.unlocked_endings
    testcase stay_southpark:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Остаться в South Park — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_southpark'
        assert eval current_ending in persistent.unlocked_endings
    testcase stay_minecraft:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Мне нужен перерыв'
        advance until screen "choice"
        click 'Проверить телефон'
        advance until screen "choice"
        click 'Спросить Бри напрямую'
        advance until screen "choice"
        click 'Устроить спокойный разговор без публики'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Попросить Миранду разобрать договоренности'
        advance until screen "choice"
        click 'Отказаться от одной просьбы и предложить замену'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Разобрать предложение Картмана'
        advance until screen "choice"
        click 'Развести мероприятия по времени и отменить ловушку штрафов'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Идти к деревне до темноты'
        advance until screen "choice"
        click 'Собрать детали самостоятельно'
        advance until screen "choice"
        click 'Переждать в укрытии'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Остаться в Minecraft — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_minecraft'
        assert eval current_ending in persistent.unlocked_endings
    testcase stay_sims:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Посмотрю, что там вообще'
        advance until screen "choice"
        click 'Поставить пирог'
        advance until screen "choice"
        click 'Проверить обстоятельства вместе с Габи'
        advance until screen "choice"
        click 'Прикрыть Сьюзан и самой организовать перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Собрать людей на одной встрече'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Пусть организаторы испытают собственные уведомления'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Подготовить факелы и безопасный проход'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Изменить условия дома, чтобы команда потеряла смысл'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Остаться в The Sims — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_sims'
        assert eval current_ending in persistent.unlocked_endings
    testcase stay_marvel:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Остаться в Marvel — завершить путешествие'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_marvel'
        assert eval current_ending in persistent.unlocked_endings
    testcase return_housewives:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'Вистерия-Лейн'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_housewives'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
    testcase return_manhattan:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'Манхэттен'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_manhattan'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
    testcase return_southpark:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'South Park'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_southpark'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
    testcase return_minecraft:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'Minecraft'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_minecraft'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
    testcase return_sims:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'The Sims'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_sims'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
    testcase return_marvel:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        advance until screen "choice"
        click 'Сначала разберусь с этим'
        advance until screen "choice"
        click 'Осмотреться'
        advance until screen "choice"
        click 'Выслушать Сьюзан до конца'
        advance until screen "choice"
        click 'Сказать прямо о накладке и попросить перенос'
        assert eval current_world == 'housewives'
        advance until screen "choice"
        click 'Попрощаться и отправиться на Манхэттен'
        advance until screen "choice"
        click 'Восстановить обещания вместе с Кэрри'
        advance until screen "choice"
        click 'Выполнить обещание, но заранее ограничить время'
        assert eval current_world == 'manhattan'
        advance until screen "choice"
        click 'Попрощаться и проверить вакансию в South Park'
        advance until screen "choice"
        click 'Проверить правила и счета вместе с Кайлом'
        advance until screen "choice"
        click 'Публично показать противоречие'
        assert eval current_world == 'southpark'
        advance until screen "choice"
        click 'Попрощаться и открыть строительный набор'
        advance until screen "choice"
        click 'Собрать дерево и построить свое укрытие'
        advance until screen "choice"
        click 'Обменяться с жителем'
        advance until screen "choice"
        click 'Обойти по освещенному гребню'
        assert eval current_world == 'minecraft'
        advance until screen "choice"
        click 'Попрощаться с жителем и пройти к экрану «Создать жизнь»'
        advance until screen "choice"
        click 'Проверить отмену вместе с Беллой'
        advance until screen "choice"
        click 'Выполнить безопасную последовательность и изучить систему'
        assert eval current_world == 'sims'
        advance until screen "choice"
        click 'Поблагодарить Беллу и подтвердить переход в Marvel'
        advance until screen "choice"
        click 'Попросить Стрэнджа объяснить устройство'
        advance until screen "choice"
        click 'Осторожно стабилизировать проход вместе со Стрэнджем'
        assert eval current_world == 'marvel'
        advance until screen "choice"
        click 'Вернуться в один из посещенных миров'
        assert screen "return_worlds"
        click 'Marvel'
        advance until screen "ending_result"
        assert eval current_ending == 'stay_marvel'
        assert eval chapter_choices["housewives"]["solution"] == "honest"
