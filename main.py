```python
import tkinter as tk
import random


# ============================================================
# 🧙 АКАДЕМІЯ МАГІЇ
# Гра на Python + Tkinter
# ============================================================


# ============================================================
# НАЛАШТУВАННЯ
# ============================================================

WIDTH = 900
HEIGHT = 700

TILE = 50

PLAYER_SPEED = 50

MAX_HP = 100
MAX_MANA = 100

player_x = 4
player_y = 4

hp = MAX_HP
mana = MAX_MANA

level = 1
experience = 0
gold = 50

damage = 10

potions = 3
mana_potions = 2

game_running = True

enemies = []
coins = []
treasures = []

message_text = "Ласкаво просимо до Академії Магії!"


# ============================================================
# ВІКНО
# ============================================================

root = tk.Tk()

root.title("🧙 Академія Магії")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)


# ============================================================
# ЛІВА ПАНЕЛЬ
# ============================================================

left_panel = tk.Frame(
    root,
    width=220,
    height=HEIGHT
)

left_panel.pack(
    side="left",
    fill="y"
)

left_panel.pack_propagate(False)


# ============================================================
# НАЗВА
# ============================================================

title_label = tk.Label(
    left_panel,
    text="🧙\nАКАДЕМІЯ\nМАГІЇ",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


# ============================================================
# ІНФОРМАЦІЯ
# ============================================================

hp_label = tk.Label(
    left_panel,
    text="❤️ HP: 100 / 100",
    font=("Arial", 13)
)

hp_label.pack(pady=5)


mana_label = tk.Label(
    left_panel,
    text="💙 Мана: 100 / 100",
    font=("Arial", 13)
)

mana_label.pack(pady=5)


level_label = tk.Label(
    left_panel,
    text="⭐ Рівень: 1",
    font=("Arial", 13)
)

level_label.pack(pady=5)


exp_label = tk.Label(
    left_panel,
    text="✨ Досвід: 0 / 100",
    font=("Arial", 13)
)

exp_label.pack(pady=5)


gold_label = tk.Label(
    left_panel,
    text="💰 Золото: 50",
    font=("Arial", 13)
)

gold_label.pack(pady=5)


damage_label = tk.Label(
    left_panel,
    text="⚔️ Сила: 10",
    font=("Arial", 13)
)

damage_label.pack(pady=5)


# ============================================================
# РОЗДІЛЮВАЧ
# ============================================================

separator = tk.Frame(
    left_panel,
    height=2
)

separator.pack(
    fill="x",
    padx=20,
    pady=15
)


# ============================================================
# ІНВЕНТАР
# ============================================================

inventory_label = tk.Label(
    left_panel,
    text="🎒 Інвентар",
    font=("Arial", 16, "bold")
)

inventory_label.pack(pady=5)


potion_label = tk.Label(
    left_panel,
    text="🧪 Зілля HP: 3",
    font=("Arial", 12)
)

potion_label.pack(pady=3)


mana_potion_label = tk.Label(
    left_panel,
    text="🔵 Зілля мани: 2",
    font=("Arial", 12)
)

mana_potion_label.pack(pady=3)


# ============================================================
# КНОПКИ
# ============================================================

heal_button = tk.Button(
    left_panel,
    text="🧪 Використати HP",
    width=18,
    command=lambda: use_health_potion()
)

heal_button.pack(pady=5)


mana_button = tk.Button(
    left_panel,
    text="🔵 Використати ману",
    width=18,
    command=lambda: use_mana_potion()
)

mana_button.pack(pady=5)


shop_button = tk.Button(
    left_panel,
    text="🛒 Магазин",
    width=18,
    command=lambda: open_shop()
)

shop_button.pack(pady=5)


help_button = tk.Button(
    left_panel,
    text="❓ Допомога",
    width=18,
    command=lambda: show_help()
)

help_button.pack(pady=5)


restart_button = tk.Button(
    left_panel,
    text="🔄 Нова гра",
    width=18,
    command=lambda: restart_game()
)

restart_button.pack(pady=5)


# ============================================================
# ІГРОВА ОБЛАСТЬ
# ============================================================

game_frame = tk.Frame(
    root
)

game_frame.pack(
    side="right",
    fill="both",
    expand=True
)


# ============================================================
# CANVAS
# ============================================================

canvas = tk.Canvas(
    game_frame,
    width=680,
    height=600
)

canvas.pack(
    padx=10,
    pady=10
)


# ============================================================
# ПОВІДОМЛЕННЯ
# ============================================================

message_label = tk.Label(
    game_frame,
    text=message_text,
    font=("Arial", 13),
    wraplength=650
)

message_label.pack(
    pady=5
)


# ============================================================
# КАРТА
# ============================================================

MAP_WIDTH = 13
MAP_HEIGHT = 11

game_map = []


# ============================================================
# СТВОРЕННЯ КАРТИ
# ============================================================

def create_map():

    global game_map

    game_map = []

    for y in range(MAP_HEIGHT):

        row = []

        for x in range(MAP_WIDTH):

            if x == 0 or y == 0:
                row.append(1)

            elif x == MAP_WIDTH - 1:
                row.append(1)

            elif y == MAP_HEIGHT - 1:
                row.append(1)

            else:

                chance = random.randint(1, 10)

                if chance == 1:
                    row.append(1)
                else:
                    row.append(0)

        game_map.append(row)

    # Безпечна зона біля старту

    for y in range(2, 6):

        for x in range(2, 6):

            game_map[y][x] = 0


# ============================================================
# ПЕРЕВІРКА КАРТИ
# ============================================================

def is_wall(x, y):

    if x < 0:
        return True

    if y < 0:
        return True

    if x >= MAP_WIDTH:
        return True

    if y >= MAP_HEIGHT:
        return True

    return game_map[y][x] == 1


# ============================================================
# МАЛЮВАННЯ КАРТИ
# ============================================================

def draw_map():

    canvas.delete("all")

    for y in range(MAP_HEIGHT):

        for x in range(MAP_WIDTH):

            x1 = x * TILE
            y1 = y * TILE

            x2 = x1 + TILE
            y2 = y1 + TILE

            if game_map[y][x] == 1:

                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill="gray25",
                    outline="gray40"
                )

            else:

                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill="darkgreen",
                    outline="green4"
                )


# ============================================================
# МАЛЮВАННЯ ГРАВЦЯ
# ============================================================

def draw_player():

    x1 = player_x * TILE
    y1 = player_y * TILE

    x2 = x1 + TILE
    y2 = y1 + TILE

    canvas.create_oval(
        x1 + 7,
        y1 + 7,
        x2 - 7,
        y2 - 7,
        fill="blue",
        outline="white",
        width=2,
        tags="player"
    )

    canvas.create_text(
        x1 + TILE // 2,
        y1 + TILE // 2,
        text="🧙",
        font=("Arial", 22),
        tags="player"
    )


# ============================================================
# МАЛЮВАННЯ ВОРОГІВ
# ============================================================

def draw_enemies():

    for enemy in enemies:

        x = enemy["x"]
        y = enemy["y"]

        x1 = x * TILE
        y1 = y * TILE

        x2 = x1 + TILE
        y2 = y1 + TILE

        canvas.create_oval(
            x1 + 5,
            y1 + 5,
            x2 - 5,
            y2 - 5,
            fill="darkred",
            outline="red",
            width=2
        )

        canvas.create_text(
            x1 + TILE // 2,
            y1 + TILE // 2,
            text="👹",
            font=("Arial", 21)
        )


# ============================================================
# МАЛЮВАННЯ МОНЕТ
# ============================================================

def draw_coins():

    for coin in coins:

        x = coin["x"]
        y = coin["y"]

        x1 = x * TILE
        y1 = y * TILE

        x2 = x1 + TILE
        y2 = y1 + TILE

        canvas.create_text(
            (x1 + x2) // 2,
            (y1 + y2) // 2,
            text="💰",
            font=("Arial", 20)
        )


# ============================================================
# МАЛЮВАННЯ СКАРБІВ
# ============================================================

def draw_treasures():

    for treasure in treasures:

        x = treasure["x"]
        y = treasure["y"]

        x1 = x * TILE
        y1 = y * TILE

        x2 = x1 + TILE
        y2 = y1 + TILE

        canvas.create_text(
            (x1 + x2) // 2,
            (y1 + y2) // 2,
            text="🎁",
            font=("Arial", 21)
        )


# ============================================================
# ОНОВЛЕННЯ ГРИ
# ============================================================

def draw_game():

    draw_map()

    draw_coins()

    draw_treasures()

    draw_enemies()

    draw_player()


# ============================================================
# ОНОВЛЕННЯ ІНТЕРФЕЙСУ
# ============================================================

def update_interface():

    hp_label.config(
        text=f"❤️ HP: {hp} / {MAX_HP}"
    )

    mana_label.config(
        text=f"💙 Мана: {mana} / {MAX_MANA}"
    )

    level_label.config(
        text=f"⭐ Рівень: {level}"
    )

    exp_label.config(
        text=f"✨ Досвід: {experience} / {level * 100}"
    )

    gold_label.config(
        text=f"💰 Золото: {gold}"
    )

    damage_label.config(
        text=f"⚔️ Сила: {damage}"
    )

    potion_label.config(
        text=f"🧪 Зілля HP: {potions}"
    )

    mana_potion_label.config(
        text=f"🔵 Зілля мани: {mana_potions}"
    )


# ============================================================
# ПОВІДОМЛЕННЯ
# ============================================================

def message(text):

    message_label.config(
        text=text
    )


# ============================================================
# ПЕРЕВІРКА ПОЗИЦІЇ
# ============================================================

def enemy_at(x, y):

    for enemy in enemies:

        if enemy["x"] == x and enemy["y"] == y:

            return enemy

    return None


# ============================================================
# ПЕРЕВІРКА МОНЕТИ
# ============================================================

def coin_at(x, y):

    for coin in coins:

        if coin["x"] == x and coin["y"] == y:

            return coin

    return None


# ============================================================
# ПЕРЕВІРКА СКАРБУ
# ============================================================

def treasure_at(x, y):

    for treasure in treasures:

        if treasure["x"] == x and treasure["y"] == y:

            return treasure

    return None


# ============================================================
# РУХ
# ============================================================

def move_player(dx, dy):

    global player_x
    global player_y

    if not game_running:
        return

    new_x = player_x + dx
    new_y = player_y + dy

    if is_wall(new_x, new_y):

        message("🧱 Тут стіна!")

        return

    enemy = enemy_at(new_x, new_y)

    if enemy is not None:

        attack_enemy(enemy)

        return

    player_x = new_x
    player_y = new_y

    collect_coin()

    open_treasure()

    draw_game()


# ============================================================
# КЕРУВАННЯ
# ============================================================

def key_press(event):

    key = event.keysym.lower()

    if key == "w":
        move_player(0, -1)

    elif key == "s":
        move_player(0, 1)

    elif key == "a":
        move_player(-1, 0)

    elif key == "d":
        move_player(1, 0)

    elif key == "up":
        move_player(0, -1)

    elif key == "down":
        move_player(0, 1)

    elif key == "left":
        move_player(-1, 0)

    elif key == "right":
        move_player(1, 0)


root.bind(
    "<KeyPress>",
    key_press
)


# ============================================================
# ЗБІР МОНЕТ
# ============================================================

def collect_coin():

    global gold

    coin = coin_at(
        player_x,
        player_y
    )

    if coin is None:
        return

    gold += coin["value"]

    coins.remove(coin)

    message(
        f"💰 Ти знайшов {coin['value']} золота!"
    )

    update_interface()


# ============================================================
# ВІДКРИТТЯ СКАРБУ
# ============================================================

def open_treasure():

    global gold
    global potions
    global mana_potions

    treasure = treasure_at(
        player_x,
        player_y
    )

    if treasure is None:
        return

    reward = random.choice(
        [
            "gold",
            "gold",
            "potion",
            "mana"
        ]
    )

    if reward == "gold":

        amount = random.randint(20, 80)

        gold += amount

        message(
            f"🎁 У скрині було {amount} золота!"
        )

    elif reward == "potion":

        potions += 1

        message(
            "🎁 Ти знайшов зілля HP!"
        )

    else:

        mana_potions += 1

        message(
            "🎁 Ти знайшов зілля мани!"
        )

    treasures.remove(treasure)

    update_interface()


# ============================================================
# АТАКА
# ============================================================

def attack_enemy(enemy):

    global experience
    global gold

    enemy["hp"] -= damage

    if enemy["hp"] > 0:

        message(
            f"⚔️ Ти завдав {damage} шкоди!"
        )

        enemy_attack(enemy)

    else:

        reward = enemy["reward"]

        gold += reward

        experience += enemy["exp"]

        message(
            f"👹 Монстра переможено! +{reward} золота, "
            f"+{enemy['exp']} XP"
        )

        enemies.remove(enemy)

        check_level_up()

    update_interface()

    draw_game()


# ============================================================
# АТАКА МОНСТРА
# ============================================================

def enemy_attack(enemy):

    global hp

    enemy_damage = random.randint(
        enemy["min_damage"],
        enemy["max_damage"]
    )

    hp -= enemy_damage

    if hp < 0:
        hp = 0

    message(
        f"👹 Монстр атакує! -{enemy_damage} HP"
    )

    if hp <= 0:

        game_over()

    update_interface()


# ============================================================
# ПЕРЕВІРКА РІВНЯ
# ============================================================

def check_level_up():

    global level
    global experience
    global damage
    global hp
    global mana

    needed = level * 100

    while experience >= needed:

        experience -= needed

        level += 1

        damage += 5

        hp = MAX_HP

        mana = MAX_MANA

        message(
            f"🎉 НОВИЙ РІВЕНЬ! Тепер ти рівень {level}!"
        )

        needed = level * 100


# ============================================================
# ЗІЛЛЯ HP
# ============================================================

def use_health_potion():

    global hp
    global potions

    if potions <= 0:

        message(
            "❌ У тебе немає зіль HP!"
        )

        return

    if hp >= MAX_HP:

        message(
            "❤️ HP вже повне!"
        )

        return

    potions -= 1

    hp += 35

    if hp > MAX_HP:
        hp = MAX_HP

    message(
        "🧪 Ти відновив HP!"
    )

    update_interface()


# ============================================================
# ЗІЛЛЯ МАНИ
# ============================================================

def use_mana_potion():

    global mana
    global mana_potions

    if mana_potions <= 0:

        message(
            "❌ У тебе немає зіль мани!"
        )

        return

    if mana >= MAX_MANA:

        message(
            "💙 Мана вже повна!"
        )

        return

    mana_potions -= 1

    mana += 40

    if mana > MAX_MANA:
        mana = MAX_MANA

    message(
        "🔵 Ти відновив ману!"
    )

    update_interface()


# ============================================================
# ГРА ЗАКІНЧЕНА
# ============================================================

def game_over():

    global game_running

    game_running = False

    message(
        "💀 Ти програв! Натисни «Нова гра»."
    )

    canvas.create_rectangle(
        100,
        180,
        550,
        400,
        fill="black",
        outline="red",
        width=4
    )

    canvas.create_text(
        325,
        260,
        text="💀 GAME OVER 💀",
        fill="red",
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        325,
        320,
        text="Твоя пригода закінчилася",
        fill="white",
        font=("Arial", 16)
    )


# ============================================================
# МАГАЗИН
# ============================================================

def open_shop():

    shop = tk.Toplevel(root)

    shop.title("🛒 Магазин")
    shop.geometry("400x450")

    title = tk.Label(
        shop,
        text="🛒 МАГАЗИН",
        font=("Arial", 22, "bold")
    )

    title.pack(pady=20)

    info = tk.Label(
        shop,
        text="Тут можна купити корисні предмети",
        font=("Arial", 11)
    )

    info.pack(pady=5)

    buy_hp_button = tk.Button(
        shop,
        text="🧪 Зілля HP — 30 золота",
        width=30,
        command=lambda: buy_health_potion(shop)
    )

    buy_hp_button.pack(pady=10)

    buy_mana_button = tk.Button(
        shop,
        text="🔵 Зілля мани — 35 золота",
        width=30,
        command=lambda: buy_mana_potion(shop)
    )

    buy_mana_button.pack(pady=10)

    buy_damage_button = tk.Button(
        shop,
        text="⚔️ Покращити силу — 100 золота",
        width=30,
        command=lambda: buy_damage(shop)
    )

    buy_damage_button.pack(pady=10)


# ============================================================
# КУПІВЛЯ HP
# ============================================================

def buy_health_potion(window):

    global gold
    global potions

    if gold < 30:

        message(
            "❌ Недостатньо золота!"
        )

        return

    gold -= 30

    potions += 1

    message(
        "🧪 Ти купив зілля HP!"
    )

    update_interface()


# ============================================================
# КУПІВЛЯ МАНИ
# ============================================================

def buy_mana_potion(window):

    global gold
    global mana_potions

    if gold < 35:

        message(
            "❌ Недостатньо золота!"
        )

        return

    gold -= 35

    mana_potions += 1

    message(
        "🔵 Ти купив зілля мани!"
    )

    update_interface()


# ============================================================
# ПОКРАЩЕННЯ СИЛИ
# ============================================================

def buy_damage(window):

    global gold
    global damage

    if gold < 100:

        message(
            "❌ Недостатньо золота!"
        )

        return

    gold -= 100

    damage += 5

    message(
        f"⚔️ Сила збільшена! Тепер: {damage}"
    )

    update_interface()


# ============================================================
# ДОПОМОГА
# ============================================================

def show_help():

    help_window = tk.Toplevel(root)

    help_window.title("❓ Допомога")

    help_window.geometry("500x500")

    title = tk.Label(
        help_window,
        text="❓ ЯК ГРАТИ",
        font=("Arial", 22, "bold")
    )

    title.pack(pady=20)

    text = """
🧙 Ти — молодий маг Академії.

🎮 Керування:

W / ↑ — рух вгору
S / ↓ — рух вниз
A / ← — рух вліво
D / → — рух вправо

👹 Зустрічай монстрів
⚔️ Атакуй їх
💰 Збирай золото
🎁 Відкривай скарби
⭐ Отримуй досвід
🧪 Використовуй зілля
🛒 Купуй предмети

🎯 Мета:
Стань найсильнішим магом Академії!
"""

    label = tk.Label(
        help_window,
        text=text,
        font=("Arial", 13),
        justify="left"
    )

    label.pack(
        padx=20,
        pady=10
    )


# ============================================================
# СТВОРЕННЯ МОНСТРІВ
# ============================================================

def create_enemies():

    global enemies

    enemies = []

    for i in range(6):

        while True:

            x = random.randint(
                1,
                MAP_WIDTH - 2
            )

            y = random.randint(
                1,
                MAP_HEIGHT - 2
            )

            if is_wall(x, y):
                continue

            if x < 5 and y < 5:
                continue

            break

        enemy_type = random.choice(
            [
                "goblin",
                "slime",
                "skeleton"
            ]
        )

        if enemy_type == "goblin":

            enemy = {
                "x": x,
                "y": y,
                "hp": 25,
                "min_damage": 4,
                "max_damage": 8,
                "reward": 20,
                "exp": 25
            }

        elif enemy_type == "slime":

            enemy = {
                "x": x,
                "y": y,
                "hp": 18,
                "min_damage": 3,
                "max_damage": 6,
                "reward": 15,
                "exp": 20
            }

        else:

            enemy = {
                "x": x,
                "y": y,
                "hp": 35,
                "min_damage": 6,
                "max_damage": 10,
                "reward": 30,
                "exp": 35
            }

        enemies.append(enemy)


# ============================================================
# СТВОРЕННЯ МОНЕТ
# ============================================================

def create_coins():

    global coins

    coins = []

    for i in range(12):

        while True:

            x = random.randint(
                1,
                MAP_WIDTH - 2
            )

            y = random.randint(
                1,
                MAP_HEIGHT - 2
            )

            if is_wall(x, y):
                continue

            if x == player_x and y == player_y:
                continue

            break

        coins.append(
            {
                "x": x,
                "y": y,
                "value": random.randint(5, 20)
            }
        )


# ============================================================
# СТВОРЕННЯ СКАРБІВ
# ============================================================

def create_treasures():

    global treasures

    treasures = []

    for i in range(4):

        while True:

            x = random.randint(
                1,
                MAP_WIDTH - 2
            )

            y = random.randint(
                1,
                MAP_HEIGHT - 2
            )

            if is_wall(x, y):
                continue

            if x < 5 and y < 5:
                continue

            break

        treasures.append(
            {
                "x": x,
                "y": y
            }
        )


# ============================================================
# НОВА ГРА
# ============================================================

def restart_game():

    global player_x
    global player_y

    global hp
    global mana

    global level
    global experience
    global gold

    global damage

    global potions
    global mana_potions

    global game_running

    player_x = 4
    player_y = 4

    hp = MAX_HP
    mana = MAX_MANA

    level = 1
    experience = 0
    gold = 50

    damage = 10

    potions = 3
    mana_potions = 2

    game_running = True

    create_map()

    create_enemies()

    create_coins()

    create_treasures()

    message(
        "🧙 Нова пригода почалася!"
    )

    update_interface()

    draw_game()


# ============================================================
# СТАРТ ГРИ
# ============================================================

restart_game()


# ============================================================
# ЗАПУСК
# ============================================================

root.mainloop()
```

### 🎮 Що є в цій грі

* 🧙 персонаж
* 🗺️ випадкова карта
* 👹 3 типи монстрів
* ⚔️ бойова система
* ❤️ HP
* 💙 мана
* ⭐ рівні
* ✨ досвід
* 💰 золото
* 🎁 скарби
* 🧪 зілля
* 🛒 магазин
* ⚔️ покращення сили
* 🎮 керування WASD і стрілками
* 💀 Game Over
* 🔄 нова гра
* ❓ меню допомоги

**Назва файлу:** `magic_academy.py`

Це вже значно більше схоже на **повноцінну графічну гру**, а не на простий клікер.
