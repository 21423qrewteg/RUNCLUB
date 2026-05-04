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

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        margin-bottom: 18px;
        border: 1px solid #e5e7eb;
    }

    .small-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        margin-bottom: 12px;
        border: 1px solid #e5e7eb;
    }

    .feed-card {
        background-color: #ffffff;
        padding: 0;
        border-radius: 20px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.08);
        margin-bottom: 24px;
        border: 1px solid #e5e7eb;
        overflow: hidden;
    }

    .feed-header {
        padding: 18px 20px 10px 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, #fb923c, #f97316);
        color: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 700;
    }

    .feed-user {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
    }

    .feed-date {
        font-size: 14px;
        color: #6b7280;
    }

    .feed-map {
        height: 220px;
        margin: 12px 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #dbeafe, #bbf7d0);
        position: relative;
        overflow: hidden;
        border: 1px solid #d1d5db;
    }

    .feed-road-1 {
        position: absolute;
        width: 80%;
        height: 10px;
        background-color: #374151;
        border-radius: 20px;
        top: 105px;
        left: 10%;
        transform: rotate(-8deg);
    }

    .feed-road-2 {
        position: absolute;
        width: 55%;
        height: 10px;
        background-color: #374151;
        border-radius: 20px;
        top: 145px;
        left: 22%;
        transform: rotate(14deg);
    }

    .feed-pin-start {
        position: absolute;
        left: 12%;
        top: 120px;
        font-size: 28px;
    }

    .feed-pin-finish {
        position: absolute;
        right: 13%;
        top: 75px;
        font-size: 28px;
    }

    .feed-park {
        position: absolute;
        left: 32px;
        top: 25px;
        font-size: 28px;
    }

    .feed-water {
        position: absolute;
        right: 38px;
        bottom: 26px;
        font-size: 30px;
    }

    .feed-content {
        padding: 8px 20px 18px 20px;
    }

    .feed-title {
        font-size: 22px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 8px;
    }

    .feed-text {
        color: #4b5563;
        font-size: 15px;
        margin-bottom: 14px;
    }

    .stats-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 14px;
        margin-bottom: 14px;
    }

    .stat-box {
        background-color: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 12px 14px;
        min-width: 110px;
    }

    .stat-number {
        font-size: 22px;
        font-weight: 800;
        color: #111827;
    }

    .stat-label {
        font-size: 13px;
        color: #6b7280;
    }

    .reaction-row {
        display: flex;
        gap: 10px;
        color: #6b7280;
        font-size: 15px;
        border-top: 1px solid #e5e7eb;
        padding-top: 12px;
        margin-top: 10px;
    }

    .success-box {
        background-color: #dcfce7;
        color: #166534;
        padding: 15px;
        border-radius: 14px;
        border: 1px solid #86efac;
        margin-top: 15px;
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

    .status-planned {
        color: #1d4ed8;
        font-weight: 700;
    }

    .status-done {
        color: #15803d;
        font-weight: 700;
    }

    .status-cancelled {
        color: #b91c1c;
        font-weight: 700;
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
        "emoji": "Д",
        "date": "Сегодня, 08:20",
        "title": "Утренняя пробежка по набережной",
        "text": "Хорошая погода, лёгкий темп и красивый вид на Енисей.",
        "distance": "5.2 км",
        "pace": "5:48",
        "time": "30 мин",
        "likes": 12,
        "comments": 3
    },
    {
        "user": "Аня",
        "emoji": "А",
        "date": "Вчера, 19:10",
        "title": "Вечерний бег в парке",
        "text": "Пробежала спокойную тренировку после школы. Ищу компанию на следующую.",
        "distance": "3.8 км",
        "pace": "6:20",
        "time": "24 мин",
        "likes": 18,
        "comments": 5
    },
    {
        "user": "Маша",
        "emoji": "М",
        "date": "Вчера, 17:45",
        "title": "Быстрая тренировка на стадионе",
        "text": "Сделала интервалы и улучшила средний темп.",
        "distance": "4.0 км",
        "pace": "5:10",
        "time": "21 мин",
        "likes": 21,
        "comments": 4
    },
    {
        "user": "Игорь",
        "emoji": "И",
        "date": "2 дня назад",
        "title": "Длинный маршрут по Красноярску",
        "text": "Пробежал новый маршрут и добавил его в свои события.",
        "distance": "8.5 км",
        "pace": "6:05",
        "time": "52 мин",
        "likes": 15,
        "comments": 2
    }
]

# Доступные пробежки для раздела поиска компании
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

# Демонстрационные переписки
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
def show_card(title, text):
    """Показывает простую информационную карточку."""
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def get_status_class(status):
    """Возвращает CSS-класс для статуса пробежки."""
    if status == "запланировано":
        return "status-planned"
    if status == "завершено":
        return "status-done"
    return "status-cancelled"


def show_feed_activity(activity, number):
    """Показывает одну карточку тренировки в ленте."""
    st.markdown(
        f"""
        <div class="feed-card">
            <div class="feed-header">
                <div class="avatar">{activity["emoji"]}</div>
                <div>
                    <div class="feed-user">{activity["user"]}</div>
                    <div class="feed-date">{activity["date"]}</div>
                </div>
            </div>

            <div class="feed-map">
                <div class="feed-park">🌳</div>
                <div class="feed-water">💧</div>
                <div class="feed-road-1"></div>
                <div class="feed-road-2"></div>
                <div class="feed-pin-start">📍</div>
                <div class="feed-pin-finish">🏁</div>
            </div>

            <div class="feed-content">
                <div class="feed-title">{activity["title"]}</div>
                <div class="feed-text">{activity["text"]}</div>

                <div class="stats-row">
                    <div class="stat-box">
                        <div class="stat-number">{activity["distance"]}</div>
                        <div class="stat-label">Дистанция</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">{activity["pace"]}</div>
                        <div class="stat-label">Темп, мин/км</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">{activity["time"]}</div>
                        <div class="stat-label">Время</div>
                    </div>
                </div>

                <div class="reaction-row">
                    <span>🔥 {activity["likes"]} лайков</span>
                    <span>💬 {activity["comments"]} комментария</span>
                    <span>🏃 Завершено</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        if st.button("🔥 Лайк", key=f"like_{number}"):
            st.success("Вы поставили лайк!")

    with col2:
        if st.button("💬 Комментировать", key=f"comment_{number}"):
            st.info("В школьном проекте это демонстрационная кнопка.")


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

    st.markdown("### Лента активности")

    for index, activity in enumerate(feed_activities):
        show_feed_activity(activity, index)


# ---------------------------------------------------------
# 2. Создать маршрут
# ---------------------------------------------------------
elif page == "Создать маршрут":
    st.markdown('<div class="big-title">Создать маршрут 🗺️</div>', unsafe_allow_html=True)
    st.write("Выберите параметры пробежки и посмотрите район на интерактивной карте Красноярска.")

    st.markdown("### Карта Красноярска")

    # Интерактивная карта Яндекса.
    # Координаты указывают на город Красноярск.
    components.html(
        """
        <iframe
            src="https://yandex.ru/map-widget/v1/?ll=92.852572%2C56.010563&z=12"
            width="100%"
            height="430"
            frameborder="0"
            allowfullscreen="true"
            style="border-radius: 18px; border: 1px solid #e5e7eb;">
        </iframe>
        """,
        height=450
    )

    st.markdown("### Параметры маршрута")

    col1, col2 = st.columns(2)

    with col1:
        route_name = st.text_input("Название маршрута", "Пробежка по Красноярску")

        finish_point = st.text_input(
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
                Место: <b>{finish_point}</b><br>
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

    st.markdown("### Фильтры поиска")

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

    st.markdown("### Доступные пробежки")

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
        st.markdown(
            f"""
            <div class="card">
                <h3>📍 {run["place"]}</h3>
                <p><b>Район:</b> {run["district"]}</p>
                <p><b>Дистанция:</b> {run["distance"]}</p>
                <p><b>Время:</b> {run["time"]}</p>
                <p><b>Темп:</b> {run["pace"]}</p>
                <p><b>Участников:</b> {run["members"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

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
        st.markdown("### Переписки")

        selected_user = st.radio(
            "Выберите чат:",
            list(st.session_state.chat_messages.keys())
        )

        st.markdown("### Последние сообщения")
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
        st.markdown(f"### Чат с пользователем: {selected_user}")

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
        st.markdown("""
        <div class="card" style="text-align:center;">
            <div style="font-size:80px;">😎</div>
            <h2>Алексей</h2>
            <p>Люблю бегать вечером, открывать новые маршруты и тренироваться с друзьями.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Любимые тренировки")
        st.markdown("""
        <span class="badge">Лёгкий бег</span>
        <span class="badge">Пробежки в парке</span>
        <span class="badge">Интервалы</span>
        <span class="badge">Забеги 5 км</span>
        """, unsafe_allow_html=True)

        st.markdown("### Статистика")

        stat1, stat2, stat3 = st.columns(3)

        with stat1:
            st.metric("Километров пробежал", "128 км")

        with stat2:
            st.metric("Количество пробежек", "32")

        with stat3:
            st.metric("Средний темп", "6:10 мин/км")

    st.markdown("### Мои маршруты")
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
        st.markdown("### Награды")
        st.markdown("""
        <div class="card">
            🏅 Первая пробежка<br>
            🥈 10 тренировок<br>
            🏆 100 километров<br>
            🔥 Неделя активности
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("### Снаряжение")
        st.markdown("""
        <div class="card">
            👟 Кроссовки: Nike Revolution<br>
            ⌚ Часы: фитнес-браслет<br>
            🎧 Наушники: спортивные<br>
            🧢 Аксессуар: кепка для бега
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# 6. Мои пробежки / Мои события
# ---------------------------------------------------------
elif page == "Мои пробежки":
    st.markdown('<div class="big-title">Мои пробежки 📅</div>', unsafe_allow_html=True)
    st.write("Здесь показаны созданные и запланированные пробежки пользователя.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Созданные маршруты")
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
        st.markdown("### Запланированные пробежки")
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

    st.markdown("### История участия")

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
