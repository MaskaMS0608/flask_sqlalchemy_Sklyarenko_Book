from database import Book, db, Genre

# db.drop_all()
db.create_all()

detective = Genre(name="Детектив")
db.session.add(detective)

fantastic = Genre(name="Фантастика")
db.session.add(fantastic)

mysticism = Genre(name="Мистика")
db.session.add(mysticism)

historical = Genre(name="Исторические романы")
db.session.add(historical)

romance_novels = Genre(name="Любовные романы")
db.session.add(romance_novels)

db.session.add(
    Book(fullname="Вокруг света за 80 дней", author="Жюль Верн", genre=fantastic)
)
db.session.add(Book(fullname="Война миров", author="Герберт Уэллс", genre=fantastic))
db.session.add(Book(fullname="Повелитель света", author="Морис Ренар", genre=fantastic))
db.session.add(
    Book(fullname="Человек-амфибия", author="Александр Беляев", genre=fantastic)
)
db.session.add(Book(fullname="1984", author="Джордж Оруэл", genre=fantastic))
db.session.add(Book(fullname="День триффидов", author="Джон Уиндем", genre=fantastic))
db.session.add(
    Book(fullname="О дивный новый мир", author="Олдос Хаксли", genre=fantastic)
)
db.session.add(
    Book(fullname="Марсианские хроники", author="Рэй Брэдбери", genre=fantastic)
)
db.session.add(Book(fullname="Академия", author="Айзек Азимов", genre=fantastic))
db.session.add(Book(fullname="Солярис", author="Станислав Лем", genre=fantastic))
db.session.add(
    Book(
        fullname="Пикник на обочине",
        author="Аркадий и Борис Стругацкие",
        genre=fantastic,
    )
)
db.session.add(Book(fullname="Марсианин", author="Энди Вейер", genre=fantastic))
db.session.add(
    Book(fullname="Дьявол и темная вода", author="Стюарт Тёртон", genre=detective)
)
db.session.add(
    Book(fullname="Письмо от русалки", author="Камилла Лэкберг", genre=detective)
)
db.session.add(
    Book(
        fullname="Пока смерть не разлучит нас",
        author="Кирстен Модглин",
        genre=detective,
    )
)
db.session.add(
    Book(
        fullname="Отель с привидениями",
        author="Уильям Уилки Коллинз",
        genre=detective,
    )
)
db.session.add(Book(fullname="Дом у озера", author="Кейт Мортон", genre=detective))
db.session.add(Book(fullname="Взаперти", author="Лора Кейли", genre=detective))
db.session.add(Book(fullname="Десять негритят", author="Агата Кристи", genre=detective))
db.session.add(Book(fullname="Последний пассажир", author="Уилл Дин", genre=detective))
db.session.add(Book(fullname="Странные игры", author="Майк Омер", genre=detective))
db.session.add(
    Book(fullname="Каштановый человечек", author="Сорен Свейструп", genre=detective)
)
db.session.add(Book(fullname="Молчание ягнят", author="Томас Харрис", genre=detective))
db.session.add(
    Book(fullname="Один из нас лжет", author="Карен Макманус", genre=detective)
)
db.session.add(
    Book(fullname="Безмолвный пациент", author="Алекс Михаэлидес", genre=detective)
)
db.session.add(Book(fullname="Код да Винчи", author="Браун Дэн", genre=detective))
db.session.add(Book(fullname="Поклонник", author="Анна Джейн", genre=romance_novels))
db.session.add(Book(fullname="Моя вина", author="Мерседес Рон", genre=romance_novels))
db.session.add(
    Book(fullname="Доля вероятности", author="Ребекка Яррос", genre=romance_novels)
)
db.session.add(Book(fullname="Цианид", author="Кристина Старк", genre=romance_novels))
db.session.add(
    Book(fullname="Идеальный план", author="Лиз Томфорд", genre=romance_novels)
)
db.session.add(
    Book(
        fullname="Поющие в терновнике",
        author="Колин Маккалоу",
        genre=romance_novels,
    )
)
db.session.add(Book(fullname="Исповедь", author="Сьерра Симоне", genre=romance_novels))
db.session.add(Book(fullname="Творец слёз", author="Эрин Дум", genre=romance_novels))
db.session.add(
    Book(fullname="Связанные местью", author="Кора Рейли", genre=romance_novels)
)
db.session.add(Book(fullname="Почему нет?", author="Алекс Хилл", genre=romance_novels))
db.session.add(
    Book(fullname="Рыжий доктор", author="Екатерина Вильмонт", genre=romance_novels)
)
db.session.add(
    Book(fullname="Спеши любить", author="Николас Спаркс", genre=romance_novels)
)
db.session.add(Book(fullname="Грешник", author="Эмма Скотт", genre=romance_novels))
db.session.add(
    Book(fullname="Это всегда был он", author="Алекс Хилл", genre=romance_novels)
)
db.session.add(
    Book(fullname="Счастье под запретом", author="Джо Беверли", genre=romance_novels)
)
db.session.add(
    Book(fullname="Когда горит огонь", author="Ханна Грейс", genre=romance_novels)
)
db.session.add(
    Book(fullname="Пустая могила", author="Джонатан Страуд", genre=mysticism)
)
db.session.add(
    Book(fullname="История с кладбищем", author="Нил Гейман", genre=mysticism)
)
db.session.add(
    Book(fullname="Ночь перед Рождеством", author="Николай Гоголь", genre=mysticism)
)
db.session.add(
    Book(fullname="Лабиринт призраков", author="Карлос Руис Сафон", genre=mysticism)
)
db.session.add(
    Book(fullname="Портрет Дориана Грея", author="Оскар Уайльд", genre=mysticism)
)
db.session.add(Book(fullname="Лисьи броды", author="Анна Старобинец", genre=mysticism))
db.session.add(Book(fullname="Скорбь Сатаны", author="Мария Корелли", genre=mysticism))
db.session.add(Book(fullname="Воронята", author="Мэгги Стивотер", genre=mysticism))
db.session.add(Book(fullname="Интервью с вампиром", author="Энн Райс", genre=mysticism))
db.session.add(
    Book(fullname="Пока течет река", author="Диана Сеттерфилд", genre=mysticism)
)
db.session.add(Book(fullname="Престиж", author="Кристофер Прист", genre=mysticism))
db.session.add(Book(fullname="Призрак оперы", author="Гастон Леру", genre=mysticism))
db.session.add(
    Book(fullname="Призрачный омут", author="Адриана Мэзер", genre=mysticism)
)
db.session.add(Book(fullname="Звонок", author="Кодзи Судзуки", genre=mysticism))
db.session.add(Book(fullname="Спартак", author="Рафаэлло Джованьоли", genre=historical))
db.session.add(
    Book(fullname="Камо грядеши", author="Генрик Сенкевич", genre=historical)
)
db.session.add(Book(fullname="Угрюм-река", author="Вячеслав Шишков", genre=historical))
db.session.add(
    Book(fullname="Жестокий век", author="Исай Калашников", genre=historical)
)
db.session.add(Book(fullname="Сердце пармы", author="Алексей Иванов", genre=historical))
db.session.add(
    Book(
        fullname="Восстание в пустыне",
        author="Лоуренс Аравийский",
        genre=historical,
    )
)
db.session.add(
    Book(fullname="Список Шиндлера", author="Томас Кенилли", genre=historical)
)
db.session.add(
    Book(
        fullname="Княжна Тараканова",
        author="Григорий Данилевский",
        genre=historical,
    )
)
db.session.add(
    Book(fullname="Амур-батюшка", author="Николай Задорнов", genre=historical)
)
db.session.add(Book(fullname="Железный король", author="Морис Дрюон", genre=historical))
db.session.add(
    Book(fullname="Гамбит королевы", author="Элизабет Фримантл", genre=historical)
)
db.session.add(Book(fullname="Электра", author="Дженнифер Сэйнт", genre=historical))
db.session.add(Book(fullname="Петр Первый", author="Алексей Толстой", genre=historical))
db.session.add(Book(fullname="Сталин", author="Эдвард Радзинский", genre=historical))
db.session.add(
    Book(
        fullname="Тайна двух реликвий",
        author="Дмитрий Миропольский",
        genre=historical,
    )
)
db.session.add(Book(fullname="Ваша честь", author="Жауме Кабре", genre=historical))
db.session.add(Book(fullname="Барбаросса", author="Валентин Пикуль", genre=historical))
db.session.add(
    Book(fullname="Железный человек", author="Поль Анри Феваль", genre=historical)
)
db.session.add(Book(fullname="Таис Афинская", author="Иван Ефремов", genre=historical))
db.session.add(
    Book(fullname="Итальянец", author="Артуро Перес-Реверте", genre=historical)
)
db.session.commit()
