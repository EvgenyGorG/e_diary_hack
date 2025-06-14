import random

from datacenter.models import Schoolkid, Teacher, Subject, Lesson
from datacenter.models import Mark, Chastisement, Commendation


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print('''Найдено несколько учеников с данным именем,
         введите полное имя чтобы избежать совпадений.''')
        return None
    except Schoolkid.DoesNotExist:
        print('''Учащийся не найден, проверьте корректность введенных данных,
        а затем попробуйте еще раз''')
        return None

    print('Учетная запись успешно получена.')
    return schoolkid


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid):
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]

    subjects = Subject.object.filter(year_of_study=schoolkid.year_of_study)
    subjects = [subject.title for subject in subjects]

    subject = random.choice(subjects)
    commendation = random.choice(commendations)

    last_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
    ).last()

    Commendation.objects.create(
        text=random.choice(commendation),
        created=last_lesson.date,
        teacher=last_lesson.teacher,
        subject=last_lesson.subject,
        schoolkid=schoolkid
    )