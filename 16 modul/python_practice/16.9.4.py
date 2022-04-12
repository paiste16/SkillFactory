class Volonteur:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def volonteur_invite(self):
        if self.status == "active":
            return f"Гость: {self.name}, город {self.city}, волонтер"
        else:
            pass

class Mentor:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def mentor_invite(self):
        if self.status == "ready":
            return f"Гость: {self.name}, город {self.city}, наставник"
        else:
            pass

class Actor:
    def __init__(self, name, city, skill, status):
        self.name = name
        self.city = city
        self.skill = skill
        self.status = status

    def actor_invite(self):
        if self.status == "paid":
            return f"Приглашенный {self.skill}: {self.name}, город {self.city}"
        else:
            pass


ment_1 = Mentor("Иван Петров", "Москва", "ready")
ment_2 = Mentor("Игорь Игорев", "Чешипузинск", "not ready")
ment_3 = Mentor("Сергей Сергеев", "Жирноград", "ready")

vol_1 = Volonteur("Алексей Алексеев", "Санкт-Петербург", "active")
vol_2 = Volonteur("Сергей Иванов", "Москва", "not active")
vol_3 = Volonteur("Александр Новиков", "Ярцево", "active")


act_1 = Actor("Кристина Арбокайте", "Воркута", "шпагоглотатель", "paid")
act_2 = Actor("Сергей Шнуров", "Смоленск", "Балерина", "paid")
act_3 = Actor("Николай Базсков", "Анадырь", "фокусник", "not paid")

guests = [ment_1, ment_2, ment_3, vol_1, vol_2, vol_3, act_1, act_2, act_3]
for guest in guests:
    if isinstance(guest, Volonteur):
        print(guest.volonteur_invite())
    elif isinstance(guest, Mentor):
        print(guest.mentor_invite())
    elif isinstance(guest, Actor):
        print(guest.actor_invite())
