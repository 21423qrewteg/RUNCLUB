import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# Настройка страницы
# ---------------------------------------------------------
st.set_page_config(
    page_title="RunMate — команда для бега",
    page_icon="🏃",
    layout="wide"
)

# ---------------------------------------------------------
# Стили приложения
# ---------------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .big-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 19px;
        color: #4b5563;
        margin-bottom: 24px;
    }

    .orange-text {
        color: #fc4c02;
        font-weight: 800;
    }

    .status-done {
        color: #15803d;
        font-weight: 700;
    }

    .status-planned {
        color: #1d4ed8;
        font-weight: 700;
    }

    .status-cancelled {
        color: #b91c1c;
        font-weight: 700;
    }

    .badge {
        display: inline-block;
        background-color: #eef2ff;
        color: #3730a3;
        padding: 7px 12px;
        border-radius: 999px;
        margin: 4px;
        font-size: 14px;
    }

    .small-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        margin-bottom: 12px;
        border: 1px solid #e5e7eb;
    }

    .success-box {
        background-color: #dcfce7;
        color: #166534;
        padding: 15px;
        border-radius: 14px;
        border: 1px solid #86efac;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Демонстрационные данные
# ---------------------------------------------------------

# Лента завершённых тренировок
feed_activities = [
    {
        "user": "Даня",
        "avatar": "🧢",
        "date": "Сегодня, 08:20",
        "title": "Утренняя пробежка по набережной",
        "description": "Хорошая погода, лёгкий темп и красивый вид на Енисей.",
        "distance": "5.2 км",
        "pace": "5:48 мин/км",
        "time": "30 мин",
        "likes": 12,
        "comments": 3,
        "status": "Завершено",
        "map_url": "https://yandex.ru/map-widget/v1/?ll=92.865202%2C56.012441&z=13"
    },
    {
        "user": "Аня",
        "avatar": "🎧",
        "date": "Вчера, 19:10",
        "title": "Вечерний бег в парке",
        "description": "Пробежала спокойную тренировку после школы. В следующий раз хочу собрать компанию.",
        "distance": "3.8 км",
        "pace": "6:20 мин/км",
        "time": "24 мин",
        "likes": 18,
        "comments": 5,
        "status": "Завершено",
        "map_url": "https://yandex.ru/map-widget/v1/?ll=92.852572%2C56.010563&z=12"
    },
    {
        "user": "Маша",
        "avatar": "🏃‍♀️",
        "date": "Вчера, 17:45",
        "title": "Быстрая тренировка на стадионе",
        "description": "Сделала интервалы и улучшила средний темп. Было сложно, но результат отличный.",
        "distance": "4.0 км",
        "pace": "5:10 мин/км",
        "time": "21 мин",
        "likes": 21,
        "comments": 4,
        "status": "Завершено",
        "map_url": "https://yandex.ru/map-widget/v1/?ll=92.893247%2C56.015283&z=13"
    },
    {
        "user": "Игорь",
        "avatar": "⌚",
        "date": "2 дня назад",
        "title": "Длинный маршрут по Красноярску",
        "description": "Пробежал новый маршрут через несколько районов города и сохранил его в события.",
        "distance": "8.5 км",
        "pace": "6:05 мин/км",
        "time": "52 мин",
        "likes": 15,
        "comments": 2,
        "status": "Завершено",
        "map_url": "https://yandex.ru/map-widget/v1/?ll=92.934280%2C56.046548&z=12"
    }
]

# Доступные пробежки
runs = [
    {
        "place": "Парк Победы",
        "district": "Центр",
        "distance": "5 км",
        "time": "18:30",
        "pace": "Средний",
        "members": 4
    },
    {
        "place": "Набережная Енисея",
        "district": "Север",
        "distance": "3 км",
        "time": "17:00",
        "pace": "Лёгкий",
        "members": 2
    },
    {
        "place": "Стадион школы №7",
        "district": "Юг",
        "distance": "10 км",
        "time": "19:15",
        "pace": "Быстрый",
        "members": 5
    },
    {
        "place": "Лесная тропа",
        "district": "Запад",
        "distance": "7 км",
        "time": "08:30",
        "pace": "Средний",
        "members": 3
    }
]

# Переписки
chats = {
    "Аня": [
        "Привет! Побежим сегодня вечером?",
        "Я могу после 18:00."
    ],
    "Даня": [
        "Я пробежал 5 км утром.",
        "Завтра хочу повторить маршрут."
    ],
    "Маша": [
        "Ищу компанию для лёгкой пробежки.",
        "Лучше в парке."
    ]
}

# Маршруты пользователя
my_routes = [
    "Набережная Енисея — Центральный парк, 5 км",
    "Школа — Стадион, 3 км",
    "Лесная тропа, 7 км"
]

# События пользователя
my_events = [
    {
        "name": "Вечерняя пробежка в парке",
        "date": "15 мая",
        "status": "запланировано"
    },
    {
        "name": "Забег по набережной",
        "date": "10 мая",
        "status": "завершено"
    },
    {
        "name": "Утренняя тренировка",
        "date": "8 мая",
        "status": "отменено"
    }
]


# ---------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------
def get_status_class(status):
    """Возвращает CSS-класс для статуса события."""
    if status == "запланировано":
        return "status-planned"
    if status == "завершено":
        return "status-done"
    return "status-cancelled"


def show_yandex_map(map_url, height=300):
    """
    Показывает интерактивную карту Яндекса.
    Карту можно двигать, увеличивать и уменьшать прямо в приложении.
    """
    components.html(
        f"""
        <iframe
            src="{map_url}"
            width="100%"
            height="{height}"
            frameborder="0"
            allowfullscreen="true"
            style="border-radius: 18px; border: 1px solid #e5e7eb;">
        </iframe>
        """,
        height=height + 20
    )


def show_activity_card(activity, index):
    """
    Показывает карточку тренировки в ленте.
    Сделано через обычные элементы Streamlit, чтобы HTML-код не выводился текстом.
    """
    with st.container(border=True):
        # Верхняя часть карточки: аватар, имя, дата
        col_avatar, col_info = st.columns([1, 8])

        with col_avatar:
            st.markdown(f"## {activity['avatar']}")

        with col_info:
            st.markdown(f"### {activity['user']}")
            st.caption(activity["date"])

        # Название и описание тренировки
        st.markdown(f"## {activity['title']}")
        st.write(activity["description"])

        # Карта Яндекса
        show_yandex_map(activity["map_url"], height=280)

        # Статистика тренировки
        stat1, stat2, stat3, stat4 = st.columns(4)

        with stat1:
            st.metric("Дистанция", activity["distance"])

        with stat2:
            st.metric("Темп", activity["pace"])

        with stat3:
            st.metric("Время", activity["time"])

        with stat4:
            st.markdown("**Статус**")
            st.markdown(
                f"<span class='status-done'>{activity['status']}</span>",
                unsafe_allow_html=True
            )

        # Лайки и комментарии
        st.markdown("---")
        react1, react2, react3 = st.columns([1, 1, 4])

        with react1:
            st.write(f"🔥 {activity['likes']} лайков")

        with react2:
            st.write(f"💬 {activity['comments']} комментариев")

        with react3:
            if st.button("Поставить лайк", key=f"like_{index}"):
                st.success("Вы поставили лайк!")


# ---------------------------------------------------------
# Боковое меню
# ---------------------------------------------------------
st.sidebar.title("🏃 RunMate")
st.sidebar.write("Меню приложения")

page = st.sidebar.radio(
    "Выберите раздел:",
    [
        "Стартовое окно",
        "Создать маршрут",
        "Найти компанию",
        "Чат",
        "Профиль",
        "Мои пробежки"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Школьный проект по информатике: поиск компании для бега.")


# ---------------------------------------------------------
# 1. Стартовое окно — лента тренировок
# ---------------------------------------------------------
if page == "Стартовое окно":
    st.markdown('<div class="big-title">RunMate 🏃‍♂️</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Лента завершённых тренировок друзей и бегунов рядом с вами.</div>',
        unsafe_allow_html=True
    )

    top1, top2, top3 = st.columns(3)

    with top1:
        st.metric("Активностей сегодня", "14")

    with top2:
        st.metric("Километров в ленте", "82 км")

    with top3:
        st.metric("Новых участников", "6")

    st.markdown("## Лента активности")

    for index, activity in enumerate(feed_activities):
        show_activity_card(activity, index)
        st.write("")


# ---------------------------------------------------------
# 2. Создать маршрут
# ---------------------------------------------------------
elif page == "Создать маршрут":
    st.markdown('<div class="big-title">Создать маршрут 🗺️</div>', unsafe_allow_html=True)
    st.write("Выберите параметры пробежки и посмотрите район на интерактивной карте Красноярска.")

    st.markdown("## Карта Красноярска")

    # Интерактивная карта Яндекса города Красноярск
    show_yandex_map(
        "https://yandex.ru/map-widget/v1/?ll=92.852572%2C56.010563&z=12",
        height=430
    )

    st.markdown("## Параметры маршрута")

    col1, col2 = st.columns(2)

    with col1:
        route_name = st.text_input("Название маршрута", "Пробежка по Красноярску")

        place = st.text_input(
            "Место пробежки или финиш",
            "Набережная Енисея"
        )

        distance = st.selectbox(
            "Дистанция",
            ["1 км", "3 км", "5 км", "7 км", "10 км", "15 км"]
        )

    with col2:
        pace_type = st.selectbox(
            "Темп",
            ["Лёгкий", "Средний", "Быстрый"]
        )

        exact_pace = st.text_input(
            "Точный темп, мин/км",
            "6:00"
        )

        run_time = st.time_input("Время пробежки")

    if st.button("Создать маршрут"):
        st.markdown(
            f"""
            <div class="success-box">
                ✅ Маршрут <b>{route_name}</b> создан!<br>
                Место: <b>{place}</b><br>
                Дистанция: <b>{distance}</b><br>
                Темп: <b>{pace_type}</b><br>
                Точный темп: <b>{exact_pace} мин/км</b><br>
                Время пробежки: <b>{run_time}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# 3. Найти компанию
# ---------------------------------------------------------
elif page == "Найти компанию":
    st.markdown('<div class="big-title">Найти компанию 👥</div>', unsafe_allow_html=True)
    st.write("Выберите подходящую пробежку и присоединяйтесь к команде.")

    st.markdown("## Фильтры поиска")

    col1, col2, col3 = st.columns(3)

    with col1:
        distance_filter = st.selectbox(
            "Дистанция",
            ["Любая", "3 км", "5 км", "7 км", "10 км"]
        )

    with col2:
        pace_filter = st.selectbox(
            "Темп",
            ["Любой", "Лёгкий", "Средний", "Быстрый"]
        )

    with col3:
        district_filter = st.selectbox(
            "Район",
            ["Любой", "Центр", "Север", "Юг", "Запад"]
        )

    st.markdown("## Доступные пробежки")

    # Фильтрация демонстрационных данных
    filtered_runs = []

    for run in runs:
        distance_ok = distance_filter == "Любая" or run["distance"] == distance_filter
        pace_ok = pace_filter == "Любой" or run["pace"] == pace_filter
        district_ok = district_filter == "Любой" or run["district"] == district_filter

        if distance_ok and pace_ok and district_ok:
            filtered_runs.append(run)

    if len(filtered_runs) == 0:
        st.warning("Подходящих пробежек пока нет. Попробуйте изменить фильтры.")

    for index, run in enumerate(filtered_runs):
        with st.container(border=True):
            st.markdown(f"### 📍 {run['place']}")
            st.write(f"**Район:** {run['district']}")
            st.write(f"**Дистанция:** {run['distance']}")
            st.write(f"**Время:** {run['time']}")
            st.write(f"**Темп:** {run['pace']}")
            st.write(f"**Участников:** {run['members']}")

            if st.button("Присоединиться", key=f"join_{index}"):
                st.success(f"Вы присоединились к пробежке: {run['place']}!")


# ---------------------------------------------------------
# 4. Чат
# ---------------------------------------------------------
elif page == "Чат":
    st.markdown('<div class="big-title">Чат 💬</div>', unsafe_allow_html=True)
    st.write("Здесь можно общаться с другими бегунами. Это демонстрационная версия чата.")

    # Сохраняем сообщения в памяти приложения во время работы
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = chats.copy()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("## Переписки")

        selected_user = st.radio(
            "Выберите чат:",
            list(st.session_state.chat_messages.keys())
        )

        st.markdown("## Последние сообщения")
        for user, messages in st.session_state.chat_messages.items():
            st.markdown(
                f"""
                <div class="small-card">
                    <b>{user}</b><br>
                    <span>{messages[-1]}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:
        st.markdown(f"## Чат с пользователем: {selected_user}")

        for message in st.session_state.chat_messages[selected_user]:
            st.markdown(
                f"""
                <div class="small-card">
                    {message}
                </div>
                """,
                unsafe_allow_html=True
            )

        new_message = st.text_input("Введите сообщение")

        if st.button("Отправить"):
            if new_message.strip() != "":
                st.session_state.chat_messages[selected_user].append(
                    "Вы: " + new_message
                )
                st.success("Сообщение отправлено!")
                st.rerun()
            else:
                st.warning("Введите текст сообщения.")


# ---------------------------------------------------------
# 5. Профиль
# ---------------------------------------------------------
elif page == "Профиль":
    st.markdown('<div class="big-title">Профиль 👤</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        with st.container(border=True):
            st.markdown("# 😎")
            st.markdown("## Алексей")
            st.write("Люблю бегать вечером, открывать новые маршруты и тренироваться с друзьями.")

    with col2:
        st.markdown("## Любимые тренировки")
        st.markdown("""
        <span class="badge">Лёгкий бег</span>
        <span class="badge">Пробежки в парке</span>
        <span class="badge">Интервалы</span>
        <span class="badge">Забеги 5 км</span>
        """, unsafe_allow_html=True)

        st.markdown("## Статистика")

        stat1, stat2, stat3 = st.columns(3)

        with stat1:
            st.metric("Километров пробежал", "128 км")

        with stat2:
            st.metric("Количество пробежек", "32")

        with stat3:
            st.metric("Средний темп", "6:10 мин/км")

    st.markdown("## Мои маршруты")
    for route in my_routes:
        st.markdown(
            f"""
            <div class="small-card">
                🗺️ {route}
            </div>
            """,
            unsafe_allow_html=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("## Награды")
        with st.container(border=True):
            st.write("🏅 Первая пробежка")
            st.write("🥈 10 тренировок")
            st.write("🏆 100 километров")
            st.write("🔥 Неделя активности")

    with col4:
        st.markdown("## Снаряжение")
        with st.container(border=True):
            st.write("👟 Кроссовки: Nike Revolution")
            st.write("⌚ Часы: фитнес-браслет")
            st.write("🎧 Наушники: спортивные")
            st.write("🧢 Аксессуар: кепка для бега")


# ---------------------------------------------------------
# 6. Мои пробежки / Мои события
# ---------------------------------------------------------
elif page == "Мои пробежки":
    st.markdown('<div class="big-title">Мои пробежки 📅</div>', unsafe_allow_html=True)
    st.write("Здесь показаны созданные и запланированные пробежки пользователя.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Созданные маршруты")
        for route in my_routes:
            st.markdown(
                f"""
                <div class="small-card">
                    🗺️ {route}
                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:
        st.markdown("## Запланированные пробежки")
        for event in my_events:
            status_class = get_status_class(event["status"])

            st.markdown(
                f"""
                <div class="small-card">
                    <b>{event["name"]}</b><br>
                    Дата: {event["date"]}<br>
                    Статус: <span class="{status_class}">{event["status"]}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## История участия")

    history = [
        "Участвовал в пробежке «Забег по набережной» — 10 мая",
        "Присоединился к команде «Утренний парк» — 5 мая",
        "Создал маршрут «Школа — Стадион» — 1 мая"
    ]

    for item in history:
        st.markdown(
            f"""
            <div class="small-card">
                ✅ {item}
            </div>
            """,
            unsafe_allow_html=True
        )
