import streamlit as st

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
        background-color: #f6f8fb;
    }

    .big-title {
        font-size: 42px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 20px;
        color: #4b5563;
        margin-bottom: 25px;
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
    }

    .success-box {
        background-color: #dcfce7;
        color: #166534;
        padding: 15px;
        border-radius: 14px;
        border: 1px solid #86efac;
        margin-top: 15px;
    }

    .map-box {
        height: 320px;
        border-radius: 20px;
        background: linear-gradient(135deg, #bbf7d0, #bfdbfe);
        position: relative;
        border: 3px solid white;
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
        margin-bottom: 20px;
    }

    .road {
        position: absolute;
        width: 75%;
        height: 12px;
        background-color: #374151;
        border-radius: 20px;
        top: 150px;
        left: 12%;
        transform: rotate(-12deg);
    }

    .point-start {
        position: absolute;
        top: 190px;
        left: 15%;
        font-size: 32px;
    }

    .point-finish {
        position: absolute;
        top: 92px;
        right: 14%;
        font-size: 32px;
    }

    .park {
        position: absolute;
        top: 30px;
        left: 40px;
        font-size: 28px;
    }

    .lake {
        position: absolute;
        bottom: 35px;
        right: 60px;
        font-size: 32px;
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
        "place": "Набережная",
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

my_routes = [
    "Парк Победы — Набережная, 5 км",
    "Школа — Стадион, 3 км",
    "Лесная тропа, 7 км"
]

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
# Функции для красивого вывода карточек
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
st.sidebar.info("Проект по информатике: приложение для поиска компании для бега.")


# ---------------------------------------------------------
# 1. Стартовое окно
# ---------------------------------------------------------
if page == "Стартовое окно":
    st.markdown('<div class="big-title">RunMate 🏃‍♂️</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Приложение для поиска новых сокомандников для бега.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        show_card(
            "Зачем нужно приложение?",
            "RunMate помогает находить людей, которые хотят бегать вместе. "
            "Можно создать маршрут, выбрать дистанцию, найти команду и запланировать тренировку."
        )

        show_card(
            "Мотивация дня",
            "Даже короткая пробежка лучше, чем её отсутствие. "
            "Позови друга, выбери маршрут и сделай первый шаг!"
        )

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Активность друзей</h3>
            <p>🔥 Даня пробежал 5 км</p>
            <p>🌆 Аня ищет компанию для вечерней пробежки</p>
            <p>🏅 Маша получила награду «10 тренировок»</p>
            <p>🌳 Игорь создал маршрут в парке</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Что можно делать в приложении?")
    c1, c2, c3 = st.columns(3)

    with c1:
        show_card("🗺️ Создавать маршруты", "Выбирайте старт, финиш, дистанцию, темп и время.")

    with c2:
        show_card("👥 Искать компанию", "Находите пробежки рядом с собой и присоединяйтесь.")

    with c3:
        show_card("💬 Общаться", "Пишите другим бегунам в простом чате.")


# ---------------------------------------------------------
# 2. Создать маршрут
# ---------------------------------------------------------
elif page == "Создать маршрут":
    st.markdown('<div class="big-title">Создать маршрут 🗺️</div>', unsafe_allow_html=True)
    st.write("Заполните данные будущей пробежки.")

    # Имитация карты
    st.markdown("""
    <div class="map-box">
        <div class="park">🌳 Парк</div>
        <div class="lake">💧 Озеро</div>
        <div class="road"></div>
        <div class="point-start">📍</div>
        <div class="point-finish">🏁</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        start_point = st.text_input("Точка старта", "Школа №7")
        finish_point = st.text_input("Точка финиша", "Парк Победы")
        distance = st.selectbox(
            "Дистанция",
            ["1 км", "3 км", "5 км", "7 км", "10 км", "15 км"]
        )

    with col2:
        pace = st.selectbox(
            "Темп",
            ["Лёгкий", "Средний", "Быстрый"]
        )
        run_time = st.time_input("Время пробежки")
        route_name = st.text_input("Название маршрута", "Вечерняя пробежка")

    if st.button("Создать маршрут"):
        st.markdown(
            f"""
            <div class="success-box">
                ✅ Маршрут <b>{route_name}</b> создан!<br>
                Старт: <b>{start_point}</b><br>
                Финиш: <b>{finish_point}</b><br>
                Дистанция: <b>{distance}</b>, темп: <b>{pace}</b>, время: <b>{run_time}</b>
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
            ⌚ Часы: обычный фитнес-браслет<br>
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
