import random
# Пока добавил руками! Но сегодня/завтра разберусь с башами
# Балансировка событий происходит в main()

# Определяем события
events = [
    "Ничего не происходит",
    "Ты встретил моба",
    "Начинается некий квест",
    "Происходит какой-то саспенс"
]

# Генерируем карту с заданным количеством событий
def generate_map(size, mob_count, quest_count, suspense_count):
    map_events = [events[0]]  # Первая клетка - ничего не происходит
    remaining_slots = size - 2  # Остальные клетки

    # Распределяем события по клеткам
    for _ in range(mob_count):
        map_events.append(events[1])
        remaining_slots -= 1
    for _ in range(quest_count):
        map_events.append(events[2])
        remaining_slots -= 1
    for _ in range(suspense_count):
        map_events.append(events[3])
        remaining_slots -= 1

    # Заполняем оставшиеся клетки "Ничего не происходит"
    for _ in range(remaining_slots):
        map_events.append(events[0])

    # Перемешиваем события
    random.shuffle(map_events)

    # Добавляем последнюю клетку
    map_events.append("ТЫ НАШЕЛ НОВЫЙ УРОВЕНЬ")
    return map_events

# Перемещение игрока
def move_player(map_events):
    position = 0
    while position < len(map_events) - 1:
        print("Нажмите '1' на клавиатуре, чтобы бросить кубик...")
        user_input = input()
        if user_input == '1':
            roll = random.randint(1, 6)
            print(f"Вы бросили кубик: {roll}")
            position += roll
            if position >= len(map_events):
                position = len(map_events) - 1
            print(f"Вы находитесь на клетке {position + 1}: {map_events[position]}")
        else:
            print("Пожалуйста, нажмите '1' для броска кубика.")

# Основная функция
def main():
    map_size = 50
    mob_count = 5
    quest_count = 2
    suspense_count = 7 

    map_events = generate_map(map_size, mob_count, quest_count, suspense_count)
    print("Добро пожаловать в игру!")
    move_player(map_events)

if __name__ == "__main__":
    main()
