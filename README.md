# Хакаем электронный дневник 

Этот набор скриптов позволяет изменять данные в электронном дневнике сайта
[Репозиторий сайта](https://github.com/devmanorg/e-diary/tree/master).

## Описание функций

В наборе присутствуют 4 функции, каждая выполняет определенную задачу:
- `get_schoolkid(имя_ученика)`, получает учетную запись искомого ученика;
- `fix_marks(учетная_запись_ученика)`, изменяет плохие оценки на хорошие;
- `remove_chastisements(учетная_запись_ученика)`, удаляет замечания учителей;
- `create_commendation(учетная_запись_ученика)`, добавляет похвалу учителя для
случайного предмета.

## Запуск и использование

- Для корректной работы скриптов скачайте 
[Репозиторий сайта](https://github.com/devmanorg/e-diary/tree/master), прочтите
основную информацию и выполните настройку согласно README;
- Скачайте набор скриптов `el_diary_hack.py` и поместите его в корень проекта
рядом с файлом `manage.py`;
- Запустите сервер командой `python3 manage.py runserver`;
- Откройте еще одно окно терминала и наберите команду `python manage.py shell`,
после удачного запуска вы увидите надпись `(InteractiveConsole)`.

Введите следующие команды:
```shell
import el_diary_hack.py
schoolkid = el_diary_hack.get_schoolkid('имя_ученика')
el_diary_hack.fix_mark(schoolkid)
el_diary_hack.remove_chastisements(schoolkid)
el_diary_hack.create_commendation(schoolkid)
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
