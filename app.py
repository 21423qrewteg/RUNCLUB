import json
import streamlit as st
import streamlit.components.v1 as components


# ---------------------------------------------------------
# Настройка страницы
# ---------------------------------------------------------
st.set_page_config(
    page_title="RUNCLUB — команда для бега",
    page_icon="🏃",
    layout="wide"
)


# ---------------------------------------------------------
# Общие стили
# ---------------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .big-title {
        font-size: 42px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 19px;
        color: #4b5563;
        margin-bottom: 24px;
    }

    .red-text {
        color: #dc2626;
        font-weight: 800;
    }

    .brand-box {
        background: linear-gradient(135deg, #dc2626, #991b1b);
        color: white;
        padding: 18px;
        border-radius: 18px;
        margin-bottom: 18px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(220, 38, 38, 0.25);
    }

    .brand-title {
        font-size: 30px;
        font-weight: 900;
        letter-spacing: 1px;
        color: white;
    }

    .brand-subtitle {
        color: #ffffff;
        font-size: 14px;
        margin-top: 4px;
        font-weight: 700;
    }

    .profile-header {
        background: linear-gradient(135deg, #dc2626, #7f1d1d);
        color: white;
        padding: 22px;
        border-radius: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 22px rgba(220, 38, 38, 0.2);
    }

    .profile-title {
        color: white;
        font-size: 36px;
        font-weight: 900;
        margin: 0;
    }

    .profile-subtitle {
        color: #fee2e2;
        font-size: 16px;
        margin-top: 6px;
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
        background-color: #fee2e2;
        color: #991b1b;
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

    .comment-card {
        background: #fff;
        border: 1px solid #fecaca;
        border-left: 7px solid #dc2626;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }

    .comment-author {
        display: inline-block;
        background: #dc2626;
        color: white;
        font-weight: 800;
        padding: 6px 12px;
        border-radius: 999px;
        margin-bottom: 10px;
        font-size: 14px;
    }

    .comment-text {
        color: #374151;
        font-size: 16px;
        line-height: 1.55;
    }

    .my-comment-card {
        background: #fef2f2;
        border: 1px solid #fca5a5;
        border-left: 7px solid #991b1b;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(153, 27, 27, 0.08);
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Демонстрационные данные
# ---------------------------------------------------------
people = {
    "Даня": {
        "avatar": "🧢",
        "description": "Любит утренние пробежки, спокойный темп и городские маршруты.",
        "kilometers": "356 км",
        "runs_count": "74",
        "avg_pace": "5:52 мин/км",
        "gear": [
            "Кроссовки: Adidas Duramo",
            "Часы: Xiaomi Band",
            "Наушники: JBL Sport"
        ],
        "last_runs": [
            "Утренняя пробежка по улицам — 5.2 км",
            "Лёгкий бег после школы — 3.1 км",
            "Темповая тренировка — 4.4 км"
        ]
    },
    "Аня": {
        "avatar": "🎧",
        "description": "Бегает вечером, любит короткие маршруты и тренировки с музыкой.",
        "kilometers": "214 км",
        "runs_count": "49",
        "avg_pace": "6:18 мин/км",
        "gear": [
            "Кроссовки: Nike Revolution",
            "Фитнес-браслет: Honor Band",
            "Наушники: беспроводные"
        ],
        "last_runs": [
            "Вечерний маршрут по району — 4.1 км",
            "Пробежка в парке — 3.4 км",
            "Лёгкая тренировка — 2.5 км"
        ]
    },
    "мария": {
        "avatar": "🏃‍♀️",
        "description": "Любит быстрые тренировки, интервальные маршруты.",
        "kilometers": "421 км",
        "runs_count": "91",
        "avg_pace": "5:20 мин/км",
        "gear": [
            "Кроссовки: Asics Gel 74",
            "Часы: Amazfit",
            "кроссовки  NIKE air pegasus 41"
        ],
        "last_runs": [
            "Круговая тренировка — 2.9 км",
            "Интервалы на районе — 4 км",
            "Быстрая пробежка — 3.2 км"
        ]
    },
    "Игорь": {
        "avatar": "⌚",
        "description": "Чаще выбирает длинные городские маршруты и тренировки на выносливость.",
        "kilometers": "612 км",
        "runs_count": "118",
        "avg_pace": "6:03 мин/км",
        "gear": [
            "Кроссовки: Puma Runner",
            "Часы: Garmin instinght 2",
            "Пояс для  телефона "
        ],
        "last_runs": [
            "Длинная пробежка по кварталам — 5.6 км",
            "Восстановительный бег — 3 км",
            "Маршрут по улицам — 6.4 км"
        ]
    }
}


feed_activities = [
    {
        "user": "Даниил",
        "avatar": "🧢",
        "date": "Сегодня, 08:23",
        "title": "Утренняя пробежка по улице",
        "description": "Спокойная тренировка по городским улицам. средний темп и хорошее настроение.",
        "distance": "5.2 км",
        "pace": "5:48 мин/км",
        "time": "30 мин",
        "status": "Завершено",
        "points": [
            [56.0212, 92.8380],
            [56.0198, 92.8465],
            [56.0182, 92.8555],
            [56.0168, 92.8640],
            [56.0150, 92.8720],
            [56.0134, 92.8810]
        ]
    },
    {
        "user": "Аня",
        "avatar": "🎧",
        "date": "Вчера, 19:10",
        "title": "Вечерний маршрут по району",
        "description": "Лёгкая пробежка вечером. Хороший вариант для спокойной тренировки после школы.",
        "distance": "4.1 км",
        "pace": "6:20 мин/км",
        "time": "26 мин",
        "status": "Завершено",
        "points": [
            [56.0105, 92.8060],
            [56.0120, 92.8140],
            [56.0138, 92.8225],
            [56.0150, 92.8310],
            [56.0165, 92.8390]
        ]
    },
    {
        "user": "Маша",
        "avatar": "🏃‍♀️",
        "date": "Вчера, 17:45",
        "title": "Круговая тренировка",
        "description": "Короткая тренировка на скорость. быстрый маршрут.",
        "distance": "2.9 км",
        "pace": "5:10 мин/км",
        "time": "15 мин",
        "status": "Завершено",
        "points": [
            [56.0150, 92.8900],
            [56.0155, 92.8950],
            [56.0140, 92.9000],
            [56.0120, 92.8985],
            [56.0125, 92.8925],
            [56.0150, 92.8900]
        ]
    },
    {
        "user": "Игорь",
        "avatar": "⌚",
        "date": "2 дня назад",
        "title": "Длинная пробежка по кварталам",
        "description": "Длинная городская пробежка на выносивость и прокачку задних икр.",
        "distance": "5.6 км",
        "pace": "6:05 мин/км",
        "time": "34 мин",
        "status": "Завершено",
        "points": [
            [56.0400, 92.9000],
            [56.0355, 92.8910],
            [56.0310, 92.8820],
            [56.0265, 92.8730],
            [56.0220, 92.8640],
            [56.0180, 92.8550],
            [56.0140, 92.8460]
        ]
    }
]


# Окно «Найти компанию»: единые маршруты с картой как на стартовом окне
company_runs = [
    {
        "id": "run_0",
        "title": "Утренняя пробежка по улицам",
        "creator": "Даня",
        "participants": ["Даня", "Аня", "Маша"],
        "friend": True,
        "distance": "5.2 км",
        "pace": "5:50 мин/км",
        "time": "30 мин",
        "description": "Городской маршрут для спокойной утренней пробежки.",
        "points": feed_activities[0]["points"]
    },
    {
        "id": "run_1",
        "title": "Вечерний маршрут по району",
        "creator": "Аня",
        "participants": ["Аня", "Игорь"],
        "friend": False,
        "distance": "4.1 км",
        "pace": "6:20 мин/км",
        "time": "26 мин",
        "description": "Лёгкая пробежка вечером. Подходит для новичков.",
        "points": feed_activities[1]["points"]
    },
    {
        "id": "run_2",
        "title": "Круговая тренировка",
        "creator": "Маша",
        "participants": ["Маша", "Даня", "Игорь"],
        "friend": True,
        "distance": "2.9 км",
        "pace": "5:10 мин/км",
        "time": "15 мин",
        "description": "Короткая тренировка на скорость и выносливость.",
        "points": feed_activities[2]["points"]
    }
]


chats = {
    "Аня": ["Привет! Побежим сегодня вечером?", "Я могу после 18:00."],
    "Даня": ["Я пробежал 5 км утром.", "Завтра хочу повторить маршрут."],
    "Маша": ["Ищу компанию для лёгкой пробежки.", "Лучше в парке."]
}

my_routes = [
    "Городской маршрут — 5 км",
    "Школа — Стадион, 3 км",
    "Квартальный круг, 4 км"
]

my_events = [
    {"name": "Вечерняя пробежка по району", "date": "15 мая", "status": "запланировано"},
    {"name": "Забег по городским улицам", "date": "10 мая", "status": "завершено"},
    {"name": "Утренняя тренировка", "date": "8 мая", "status": "отменено"}
]


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------
if "activity_likes" not in st.session_state:
    st.session_state.activity_likes = {
        "activity_0": 12,
        "activity_1": 18,
        "activity_2": 21,
        "activity_3": 15,
        "user_saved": 0
    }

if "activity_comments" not in st.session_state:
    st.session_state.activity_comments = {
        "activity_0": [
            {"author": "Аня", "text": "Очень классный маршрут! Я бы тоже хотела пробежать его утром, когда машин меньше и улицы свободнее."},
            {"author": "Маша", "text": "Темп хороший, маршрут выглядит понятным. Мне нравится, что тренировка не слишком длинная, но полезная."},
        ],
        "activity_1": [
            {"author": "Даня", "text": "Вечером такой маршрут должен быть очень приятным. Можно спокойно бежать и не торопиться."},
            {"author": "Катя", "text": "Я бы присоединилась к такой пробежке. Дистанция комфортная, а темп подходит почти всем."}
        ],
        "activity_2": [
            {"author": "Алексей", "text": "Круговой маршрут удобен тем, что можно закончить почти там же, где начал. Хорошая тренировка."}
        ],
        "activity_3": [
            {"author": "Маша", "text": "Длинная пробежка выглядит серьёзно. Для выходного дня прям отличный вариант."}
        ],
        "user_saved": []
    }

if "liked_by_me" not in st.session_state:
    st.session_state.liked_by_me = {}

if "company_members" not in st.session_state:
    st.session_state.company_members = {
        run["id"]: len(run["participants"]) for run in company_runs
    }

if "joined_runs" not in st.session_state:
    st.session_state.joined_runs = {}

if "profile_avatar" not in st.session_state:
    st.session_state.profile_avatar = None

if "my_description" not in st.session_state:
    st.session_state.my_description = "Люблю бегать вечером, открывать новые маршруты и тренироваться с друзьями в RUNCLUB."

if "edit_description" not in st.session_state:
    st.session_state.edit_description = False


# ---------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------
def get_query_value(name, default=""):
    value = st.query_params.get(name, default)

    if isinstance(value, list):
        return value[0] if len(value) > 0 else default

    return value


def get_status_class(status):
    if status in ["запланировано", "Запланировано"]:
        return "status-planned"
    if status in ["завершено", "Завершено"]:
        return "status-done"

    return "status-cancelled"


def show_activity_map(points, map_key, height=280):
    """Показывает карту с маршрутом."""
    points_json = json.dumps(points)

    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <style>
                body {{
                    margin: 0;
                }}

                #map_{map_key} {{
                    height: {height}px;
                    width: 100%;
                    border-radius: 16px;
                    border: 1px solid #d1d5db;
                }}
            </style>
        </head>
        <body>
            <div id="map_{map_key}"></div>

            <script>
                var points = {points_json};

                var map = L.map('map_{map_key}', {{
                    scrollWheelZoom: false
                }});

                L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }}).addTo(map);

                if (points.length > 0) {{
                    var line = L.polyline(points, {{
                        color: "#dc2626",
                        weight: 6,
                        opacity: 0.95
                    }}).addTo(map);

                    L.marker(points[0]).addTo(map).bindPopup("📍 Старт");

                    if (points.length > 1) {{
                        L.marker(points[points.length - 1]).addTo(map).bindPopup("🏁 Финиш");
                    }}

                    map.fitBounds(line.getBounds(), {{
                        padding: [35, 35]
                    }});
                }} else {{
                    map.setView([56.010563, 92.852572], 12);
                }}
            </script>
        </body>
        </html>
        """,
        height=height + 20
    )


def get_user_saved_activity():
    title = get_query_value("title", "Мой маршрут")
    description = get_query_value("description", "Маршрут создан в RUNCLUB.")
    date = get_query_value("date", "Дата не выбрана")
    distance = get_query_value("distance", "0.00")
    pace = get_query_value("pace", "6.0")
    time = get_query_value("time", "0 мин")
    points_text = get_query_value("points", "[]")

    try:
        user_points = json.loads(points_text)
    except Exception:
        user_points = []

    return {
        "user": "Вы",
        "avatar": "🙂",
        "date": date,
        "title": title,
        "description": description,
        "distance": f"{distance} км",
        "pace": f"{pace} мин/км",
        "time": time,
        "status": "Запланировано",
        "points": user_points
    }


def open_profile_button(name, key):
    """Кнопка имени, которая открывает профиль участника."""
    if st.button(name, key=key):
        st.query_params["page"] = "Профиль"
        st.query_params["profile_user"] = name
        st.rerun()


def show_activity_card(activity, activity_id, is_user=False):
    """Карточка тренировки на стартовом экране."""
    with st.container(border=True):
        col_avatar, col_info = st.columns([1, 8])

        with col_avatar:
            st.markdown(f"## {activity['avatar']}")

        with col_info:
            if is_user:
                st.markdown("### Вы <span class='red-text'>— ваш маршрут</span>", unsafe_allow_html=True)
            else:
                open_profile_button(activity["user"], f"profile_from_feed_{activity_id}")

            st.caption(activity["date"])

        st.markdown(f"## {activity['title']}")
        st.write(activity["description"])

        show_activity_map(activity["points"], f"map_{activity_id}")

        stat1, stat2, stat3, stat4 = st.columns(4)

        with stat1:
            st.metric("Дистанция", activity["distance"])

        with stat2:
            st.metric("Темп", activity["pace"])

        with stat3:
            st.metric("Время", activity["time"])

        with stat4:
            st.markdown("**Статус**")
            status_class = get_status_class(activity["status"])
            st.markdown(
                f"<span class='{status_class}'>{activity['status']}</span>",
                unsafe_allow_html=True
            )

        st.markdown("---")

        current_likes = st.session_state.activity_likes.get(activity_id, 0)
        comments_count = len(st.session_state.activity_comments.get(activity_id, []))

        react1, react2, react3 = st.columns([1, 1, 4])

        with react1:
            if st.button(f"❤️ {current_likes} лайков", key=f"like_{activity_id}"):
                if not st.session_state.liked_by_me.get(activity_id, False):
                    st.session_state.activity_likes[activity_id] = current_likes + 1
                    st.session_state.liked_by_me[activity_id] = True
                    st.rerun()
                else:
                    st.info("Вы уже поставили лайк.")

        with react2:
            if st.button(f"💬 {comments_count} комментариев", key=f"comments_{activity_id}"):
                st.query_params["page"] = "Комментарии"
                st.query_params["activity_id"] = activity_id
                st.rerun()

        with react3:
            st.write("Откройте комментарии, чтобы посмотреть обсуждение.")


def show_comment_card(author, text, is_mine=False):
    card_class = "my-comment-card" if is_mine else "comment-card"

    st.markdown(
        f"""
        <div class="{card_class}">
            <div class="comment-author">{author}</div>
            <div class="comment-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Боковое меню
# ---------------------------------------------------------
pages = [
    "Стартовое окно",
    "Создать маршрут",
    "Найти компанию",
    "Чат",
    "Профиль",
    "Мои пробежки",
    "Комментарии"
]

page_from_url = get_query_value("page", "Стартовое окно")
default_page_index = pages.index(page_from_url) if page_from_url in pages else 0

st.sidebar.markdown(
    """
    <div class="brand-box">
        <div class="brand-title">🏃 RUNCLUB</div>
        <div class="brand-subtitle">Будущий RUNCLUB</div>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Выберите раздел:",
    pages,
    index=default_page_index
)

st.sidebar.markdown("---")
st.sidebar.info("Школьный проект по информатике: поиск компании для бега.")


# ---------------------------------------------------------
# 1. Стартовое окно
# ---------------------------------------------------------
if page == "Стартовое окно":
    st.markdown('<div class="big-title">RUNCLUB 🏃‍♂️</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Лента завершённых и запланированных тренировок друзей и бегунов рядом с вами.</div>',
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

    saved_route = get_query_value("saved_route", "0")

    if saved_route == "1":
        user_activity = get_user_saved_activity()

        if "user_saved" not in st.session_state.activity_likes:
            st.session_state.activity_likes["user_saved"] = 0

        if "user_saved" not in st.session_state.activity_comments:
            st.session_state.activity_comments["user_saved"] = []

        show_activity_card(user_activity, "user_saved", is_user=True)
        st.write("")

    for index, activity in enumerate(feed_activities):
        activity_id = f"activity_{index}"
        show_activity_card(activity, activity_id)
        st.write("")


# ---------------------------------------------------------
# 2. Создать маршрут
# ---------------------------------------------------------
elif page == "Создать маршрут":
    st.markdown('<div class="big-title">Создать маршрут 🗺️</div>', unsafe_allow_html=True)
    st.write(
        "Поставьте точки маршрута в любом месте на карте. "
        "Маршрут не обязан быть замкнутым: можно поставить старт, промежуточные точки и финиш."
    )

    components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

            <style>
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #f5f7fb;
                }

                .app-box {
                    background: white;
                    border-radius: 18px;
                    padding: 14px;
                    border: 1px solid #e5e7eb;
                    box-sizing: border-box;
                }

                .hint {
                    background: #fef2f2;
                    border: 1px solid #fecaca;
                    color: #991b1b;
                    padding: 10px 12px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                    font-size: 14px;
                    line-height: 1.35;
                }

                .buttons {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-bottom: 10px;
                }

                button {
                    border: none;
                    border-radius: 10px;
                    padding: 10px 14px;
                    font-size: 14px;
                    font-weight: 700;
                    cursor: pointer;
                }

                .main-button {
                    background: #dc2626;
                    color: white;
                }

                .blue-button {
                    background: #2563eb;
                    color: white;
                }

                .green-button {
                    background: #16a34a;
                    color: white;
                }

                .gray-button {
                    background: #e5e7eb;
                    color: #111827;
                }

                .red-button {
                    background: #dc2626;
                    color: white;
                }

                #map {
                    height: 410px;
                    width: 100%;
                    border-radius: 16px;
                    border: 1px solid #d1d5db;
                    margin-bottom: 12px;
                }

                .controls {
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 10px;
                    margin-top: 10px;
                }

                .control-card {
                    background: #f9fafb;
                    border: 1px solid #e5e7eb;
                    border-radius: 12px;
                    padding: 10px;
                    min-height: 76px;
                    box-sizing: border-box;
                }

                .control-card label {
                    font-size: 12px;
                    color: #4b5563;
                    display: block;
                    margin-bottom: 6px;
                    font-weight: 700;
                }

                .control-card input {
                    width: 100%;
                    box-sizing: border-box;
                    padding: 8px;
                    border-radius: 8px;
                    border: 1px solid #d1d5db;
                    font-size: 14px;
                }

                .metric {
                    font-size: 22px;
                    font-weight: 800;
                    color: #111827;
                    margin-top: 4px;
                }

                .status {
                    background: #fee2e2;
                    color: #991b1b;
                    padding: 9px 10px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                    font-size: 14px;
                    font-weight: 700;
                }

                .save-button {
                    width: 100%;
                    margin-top: 2px;
                    background: #dc2626;
                    color: white;
                }

                .success-overlay {
                    position: fixed;
                    left: 0;
                    right: 0;
                    top: 0;
                    bottom: 0;
                    background: rgba(17, 24, 39, 0.55);
                    display: none;
                    align-items: center;
                    justify-content: center;
                    z-index: 9999;
                    opacity: 0;
                    transition: opacity 0.5s ease;
                }

                .success-overlay.show {
                    display: flex;
                    opacity: 1;
                }

                .success-modal {
                    background: white;
                    border-radius: 22px;
                    padding: 28px;
                    width: 420px;
                    max-width: 90%;
                    text-align: center;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
                    animation: slideUp 0.5s ease forwards;
                }

                .success-modal h2 {
                    margin: 0 0 10px 0;
                    color: #166534;
                    font-size: 26px;
                }

                .success-modal p {
                    color: #4b5563;
                    font-size: 15px;
                    line-height: 1.5;
                }

                .check {
                    width: 70px;
                    height: 70px;
                    border-radius: 50%;
                    background: #dcfce7;
                    color: #16a34a;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 38px;
                    margin: 0 auto 16px auto;
                }

                @keyframes slideUp {
                    from {
                        transform: translateY(25px);
                        opacity: 0;
                    }

                    to {
                        transform: translateY(0);
                        opacity: 1;
                    }
                }

                @media (max-width: 900px) {
                    .controls {
                        grid-template-columns: repeat(2, 1fr);
                    }

                    #map {
                        height: 360px;
                    }
                }
            </style>
        </head>

        <body>
            <div class="app-box">
                <div class="hint">
                    1. Нажмите «Начать маршрут».<br>
                    2. Кликайте в любом месте на карте, чтобы ставить точки маршрута.<br>
                    3. Маршрут может быть обычной линией: он не обязан замыкаться в фигуру.<br>
                    4. Нажмите «Поставить финиш», затем кликните по карте, чтобы поставить последнюю точку.<br>
                    5. Дата доступна только от сегодня до 5 дней вперёд.
                </div>

                <div class="status" id="statusText">
                    Режим: маршрут ещё не начат.
                </div>

                <div class="buttons">
                    <button class="main-button" onclick="startRoute()">▶️ Начать маршрут</button>
                    <button class="green-button" onclick="enableFinishMode()">🏁 Поставить финиш</button>
                    <button class="blue-button" onclick="finishRoute()">✅ Завершить маршрут</button>
                    <button class="gray-button" onclick="removeLastPoint()">↩️ Удалить точку</button>
                    <button class="red-button" onclick="clearRoute()">🗑️ Очистить</button>
                </div>

                <div id="map"></div>

                <div class="controls">
                    <div class="control-card">
                        <label>Название маршрута</label>
                        <input id="routeName" type="text" value="Пробежка по Красноярску">
                    </div>

                    <div class="control-card">
                        <label>Описание</label>
                        <input id="routeDescription" type="text" value="Маршрут создан в RUNCLUB.">
                    </div>

                    <div class="control-card">
                        <label>Дата начала</label>
                        <input id="runDate" type="date">
                    </div>

                    <div class="control-card">
                        <label>Темп, мин/км</label>
                        <input id="pace" type="number" value="6.0" min="3" max="12" step="0.1" oninput="updateInfo()">
                    </div>
                </div>

                <div class="controls">
                    <div class="control-card">
                        <label>Количество точек</label>
                        <div class="metric" id="pointsCount">0</div>
                    </div>

                    <div class="control-card">
                        <label>Длина маршрута</label>
                        <div class="metric" id="distance">0.00 км</div>
                    </div>

                    <div class="control-card">
                        <label>Примерное время</label>
                        <div class="metric" id="timeText">0 мин</div>
                    </div>

                    <div class="control-card">
                        <label>Сохранение</label>
                        <button class="save-button" onclick="saveRoute()">Создать</button>
                    </div>
                </div>
            </div>

            <div class="success-overlay" id="successOverlay">
                <div class="success-modal">
                    <div class="check">✓</div>
                    <h2>Ваш маршрут сохранён!</h2>
                    <p>Сейчас вы будете перенаправлены на стартовое окно RUNCLUB.</p>
                </div>
            </div>

            <script>
                function setupDateLimit() {
                    var dateInput = document.getElementById("runDate");
                    var today = new Date();
                    var maxDate = new Date();

                    maxDate.setDate(today.getDate() + 5);

                    var todayText = today.toISOString().split("T")[0];
                    var maxDateText = maxDate.toISOString().split("T")[0];

                    dateInput.min = todayText;
                    dateInput.max = maxDateText;
                    dateInput.value = todayText;
                }

                setupDateLimit();

                var map = L.map('map').setView([56.010563, 92.852572], 12);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }).addTo(map);

                var routePoints = [];
                var routeMarkers = [];
                var routeLine = null;
                var startMarker = null;
                var finishMarker = null;

                var routeStarted = false;
                var finishMode = false;
                var routeFinished = false;
                var routeDistance = 0;

                function startRoute() {
                    clearRoute();

                    routeStarted = true;
                    finishMode = false;
                    routeFinished = false;

                    document.getElementById("statusText").innerText =
                        "Режим: ставьте точки маршрута кликами по карте.";
                }

                function enableFinishMode() {
                    if (!routeStarted) {
                        alert("Сначала нажмите «Начать маршрут».");
                        return;
                    }

                    if (routePoints.length < 1) {
                        alert("Сначала поставьте хотя бы одну точку старта.");
                        return;
                    }

                    finishMode = true;

                    document.getElementById("statusText").innerText =
                        "Режим: кликните по карте, чтобы поставить финиш.";
                }

                function finishRoute() {
                    if (routePoints.length < 2) {
                        alert("Для маршрута нужно минимум две точки.");
                        return;
                    }

                    routeFinished = true;
                    finishMode = false;

                    var lastPoint = routePoints[routePoints.length - 1];

                    if (finishMarker !== null) {
                        map.removeLayer(finishMarker);
                    }

                    finishMarker = L.marker(lastPoint).addTo(map).bindPopup("🏁 Финиш");

                    document.getElementById("statusText").innerText =
                        "Маршрут завершён. Длина и время рассчитаны.";
                }

                map.on('click', function(event) {
                    if (!routeStarted) {
                        return;
                    }

                    if (routeFinished) {
                        alert("Маршрут уже завершён. Нажмите «Очистить», чтобы построить новый.");
                        return;
                    }

                    var point = event.latlng;

                    routePoints.push([point.lat, point.lng]);

                    if (routePoints.length === 1) {
                        startMarker = L.marker(point)
                            .addTo(map)
                            .bindPopup("📍 Старт")
                            .openPopup();
                    } else if (finishMode) {
                        finishMarker = L.marker(point)
                            .addTo(map)
                            .bindPopup("🏁 Финиш")
                            .openPopup();

                        routeFinished = true;
                        finishMode = false;

                        document.getElementById("statusText").innerText =
                            "Маршрут завершён. Длина и время рассчитаны.";
                    } else {
                        var marker = L.circleMarker(point, {
                            radius: 6,
                            color: "#dc2626",
                            fillColor: "#dc2626",
                            fillOpacity: 1
                        }).addTo(map);

                        routeMarkers.push(marker);
                    }

                    redrawRoute();
                    updateInfo();
                });

                function redrawRoute() {
                    if (routeLine !== null) {
                        map.removeLayer(routeLine);
                    }

                    if (routePoints.length >= 2) {
                        routeLine = L.polyline(routePoints, {
                            color: "#dc2626",
                            weight: 6,
                            opacity: 0.95
                        }).addTo(map);
                    }
                }

                function removeLastPoint() {
                    if (routePoints.length === 0) {
                        alert("Точек маршрута пока нет.");
                        return;
                    }

                    if (routeFinished) {
                        routeFinished = false;
                        finishMode = false;

                        if (finishMarker !== null) {
                            map.removeLayer(finishMarker);
                            finishMarker = null;
                        }
                    }

                    routePoints.pop();

                    redrawAllMarkers();
                    redrawRoute();
                    updateInfo();

                    document.getElementById("statusText").innerText =
                        "Последняя точка удалена. Можно продолжать маршрут.";
                }

                function redrawAllMarkers() {
                    if (startMarker !== null) {
                        map.removeLayer(startMarker);
                        startMarker = null;
                    }

                    if (finishMarker !== null) {
                        map.removeLayer(finishMarker);
                        finishMarker = null;
                    }

                    for (var i = 0; i < routeMarkers.length; i++) {
                        map.removeLayer(routeMarkers[i]);
                    }

                    routeMarkers = [];

                    for (var j = 0; j < routePoints.length; j++) {
                        var point = routePoints[j];

                        if (j === 0) {
                            startMarker = L.marker(point).addTo(map).bindPopup("📍 Старт");
                        } else {
                            var marker = L.circleMarker(point, {
                                radius: 6,
                                color: "#dc2626",
                                fillColor: "#dc2626",
                                fillOpacity: 1
                            }).addTo(map);

                            routeMarkers.push(marker);
                        }
                    }
                }

                function clearRoute() {
                    routePoints = [];

                    if (routeLine !== null) {
                        map.removeLayer(routeLine);
                        routeLine = null;
                    }

                    if (startMarker !== null) {
                        map.removeLayer(startMarker);
                        startMarker = null;
                    }

                    if (finishMarker !== null) {
                        map.removeLayer(finishMarker);
                        finishMarker = null;
                    }

                    for (var i = 0; i < routeMarkers.length; i++) {
                        map.removeLayer(routeMarkers[i]);
                    }

                    routeMarkers = [];

                    routeStarted = false;
                    finishMode = false;
                    routeFinished = false;
                    routeDistance = 0;

                    updateInfo();

                    document.getElementById("statusText").innerText =
                        "Режим: маршрут очищен. Нажмите «Начать маршрут».";
                }

                function calculateDistance() {
                    var distanceMeters = 0;

                    if (routePoints.length < 2) {
                        return 0;
                    }

                    for (var i = 0; i < routePoints.length - 1; i++) {
                        distanceMeters += L.latLng(routePoints[i][0], routePoints[i][1])
                            .distanceTo(L.latLng(routePoints[i + 1][0], routePoints[i + 1][1]));
                    }

                    return distanceMeters / 1000;
                }

                function formatTime(minutes) {
                    if (minutes <= 0) {
                        return "0 мин";
                    }

                    var hours = Math.floor(minutes / 60);
                    var mins = Math.round(minutes % 60);

                    if (hours > 0) {
                        return hours + " ч " + mins + " мин";
                    }

                    return mins + " мин";
                }

                function updateInfo() {
                    routeDistance = calculateDistance();

                    var pace = parseFloat(document.getElementById("pace").value);

                    if (isNaN(pace)) {
                        pace = 0;
                    }

                    var totalMinutes = routeDistance * pace;

                    document.getElementById("distance").innerText =
                        routeDistance.toFixed(2) + " км";

                    document.getElementById("timeText").innerText =
                        formatTime(totalMinutes);

                    document.getElementById("pointsCount").innerText =
                        routePoints.length;
                }

                function saveRoute() {
                    var name = document.getElementById("routeName").value;
                    var description = document.getElementById("routeDescription").value;
                    var date = document.getElementById("runDate").value;
                    var pace = document.getElementById("pace").value;
                    var time = document.getElementById("timeText").innerText;

                    if (routePoints.length < 2) {
                        alert("Сначала поставьте минимум две точки маршрута.");
                        return;
                    }

                    if (!routeFinished) {
                        alert("Сначала завершите маршрут или поставьте финиш.");
                        return;
                    }

                    var overlay = document.getElementById("successOverlay");
                    overlay.style.display = "flex";

                    setTimeout(function() {
                        overlay.classList.add("show");
                    }, 50);

                    var params = new URLSearchParams();

                    params.set("page", "Стартовое окно");
                    params.set("saved_route", "1");
                    params.set("title", name);
                    params.set("description", description);
                    params.set("date", date);
                    params.set("distance", routeDistance.toFixed(2));
                    params.set("pace", pace);
                    params.set("time", time);
                    params.set("points", JSON.stringify(routePoints));

                    setTimeout(function() {
                        window.parent.location.href =
                            window.parent.location.pathname + "?" + params.toString();
                    }, 1800);
                }

                updateInfo();
            </script>
        </body>
        </html>
        """,
        height=820
    )


# ---------------------------------------------------------
# Страница комментариев
# ---------------------------------------------------------
elif page == "Комментарии":
    st.markdown('<div class="big-title">Комментарии 💬</div>', unsafe_allow_html=True)

    activity_id = get_query_value("activity_id", "activity_0")

    if activity_id == "user_saved":
        activity = get_user_saved_activity()
    else:
        try:
            index = int(activity_id.replace("activity_", ""))
            activity = feed_activities[index]
        except Exception:
            activity = feed_activities[0]
            activity_id = "activity_0"

    if activity_id not in st.session_state.activity_comments:
        st.session_state.activity_comments[activity_id] = []

    if activity_id not in st.session_state.activity_likes:
        st.session_state.activity_likes[activity_id] = 0

    if st.button("← Вернуться в ленту"):
        st.query_params["page"] = "Стартовое окно"
        st.rerun()

    with st.container(border=True):
        st.markdown(f"## {activity['avatar']} {activity['user']}")
        st.caption(activity["date"])
        st.markdown(f"### {activity['title']}")
        st.write(activity["description"])

        show_activity_map(activity["points"], f"comments_{activity_id}")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Дистанция", activity["distance"])

        with c2:
            st.metric("Темп", activity["pace"])

        with c3:
            st.metric("Время", activity["time"])

    st.markdown("## Комментарии")

    comments = st.session_state.activity_comments[activity_id]

    if len(comments) == 0:
        st.info("Комментариев пока нет. Напишите первый комментарий.")

    for comment in comments:
        is_mine = comment["author"].strip().lower() in ["вы", "я", "me"]
        show_comment_card(comment["author"], comment["text"], is_mine=is_mine)

    st.markdown("## Добавить комментарий")

    comment_author = st.text_input("Ваше имя", "Вы")
    new_comment = st.text_area("Текст комментария")

    if st.button("Сохранить комментарий"):
        if new_comment.strip() == "":
            st.warning("Введите текст комментария.")
        else:
            st.session_state.activity_comments[activity_id].append(
                {
                    "author": comment_author,
                    "text": new_comment
                }
            )
            st.success("Комментарий сохранён!")
            st.rerun()


# ---------------------------------------------------------
# 3. Найти компанию
# ---------------------------------------------------------
elif page == "Найти компанию":
    st.markdown('<div class="big-title">Найти компанию 👥</div>', unsafe_allow_html=True)
    st.write("Выберите подходящую пробежку и присоединяйтесь к команде.")

    st.markdown("## Фильтры поиска")

    col1, col2 = st.columns(2)

    with col1:
        distance_filter = st.selectbox(
            "Дистанция",
            ["Любая", "2.9 км", "4.1 км", "5.2 км"]
        )

    with col2:
        friend_filter = st.selectbox(
            "Друзья",
            ["Все", "Только друзья", "Не в друзьях"]
        )

    st.markdown("## Доступные пробежки")

    for index, run in enumerate(company_runs):
        distance_ok = distance_filter == "Любая" or run["distance"] == distance_filter

        if friend_filter == "Только друзья":
            friend_ok = run["friend"]
        elif friend_filter == "Не в друзьях":
            friend_ok = not run["friend"]
        else:
            friend_ok = True

        if not distance_ok or not friend_ok:
            continue

        with st.container(border=True):
            st.markdown(f"## {run['title']}")
            st.write(run["description"])

            col_map, col_info = st.columns([2, 1])

            with col_map:
                show_activity_map(run["points"], f"company_route_{index}", height=260)

            with col_info:
                st.markdown("### Информация")
                st.write(f"**Создатель:** {run['creator']}")
                st.write(f"**В друзьях:** {'Да' if run['friend'] else 'Нет'}")
                st.write(f"**Дистанция:** {run['distance']}")
                st.write(f"**Примерное время:** {run['time']}")
                st.write(f"**Темп:** {run['pace']}")
                st.write(f"**Участников:** {st.session_state.company_members[run['id']]}")

                if st.button("Присоединиться", key=f"join_{run['id']}"):
                    if not st.session_state.joined_runs.get(run["id"], False):
                        st.session_state.company_members[run["id"]] += 1
                        st.session_state.joined_runs[run["id"]] = True
                        st.success("Вы присоединились к пробежке!")
                        st.rerun()
                    else:
                        st.info("Вы уже присоединились к этой пробежке.")

            st.markdown("### Кто бежит")

            participant_cols = st.columns(len(run["participants"]))

            for participant_index, participant_name in enumerate(run["participants"]):
                with participant_cols[participant_index]:
                    avatar = people[participant_name]["avatar"]
                    if st.button(
                        f"{avatar} {participant_name}",
                        key=f"participant_{run['id']}_{participant_name}"
                    ):
                        st.query_params["page"] = "Профиль"
                        st.query_params["profile_user"] = participant_name
                        st.rerun()


# ---------------------------------------------------------
# 4. Чат
# ---------------------------------------------------------
elif page == "Чат":
    st.markdown('<div class="big-title">Чат 💬</div>', unsafe_allow_html=True)
    st.write("Здесь можно общаться с другими бегунами. Это демонстрационная версия чата.")

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
                st.session_state.chat_messages[selected_user].append("Вы: " + new_message)
                st.success("Сообщение отправлено!")
                st.rerun()
            else:
                st.warning("Введите текст сообщения.")


# ---------------------------------------------------------
# 5. Профиль
# ---------------------------------------------------------
elif page == "Профиль":
    profile_user = get_query_value("profile_user", "Вы")

    st.markdown(
        """
        <div class="profile-header">
            <div class="profile-title">Профиль</div>
            <div class="profile-subtitle">Информация об участнике RUNCLUB</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if profile_user == "Вы":
        col1, col2 = st.columns([1, 2])

        with col1:
            uploaded_avatar = st.file_uploader(
                "Загрузите свою аватарку",
                type=["png", "jpg", "jpeg"]
            )

            if uploaded_avatar is not None:
                st.session_state.profile_avatar = uploaded_avatar

            if st.session_state.profile_avatar is not None:
                st.image(st.session_state.profile_avatar, width=180)
            else:
                st.markdown("# 😎")

        with col2:
            st.markdown("## Алексей")

            if st.session_state.edit_description:
                new_description = st.text_area(
                    "Описание профиля",
                    st.session_state.my_description
                )

                save_col, cancel_col = st.columns(2)

                with save_col:
                    if st.button("Сохранить описание"):
                        st.session_state.my_description = new_description
                        st.session_state.edit_description = False
                        st.success("Описание сохранено!")
                        st.rerun()

                with cancel_col:
                    if st.button("Отмена"):
                        st.session_state.edit_description = False
                        st.rerun()
            else:
                st.write(st.session_state.my_description)

                if st.button("Редактировать описание"):
                    st.session_state.edit_description = True
                    st.rerun()

            stat1, stat2, stat3 = st.columns(3)

            with stat1:
                st.metric("Километров пробежал", "128 км")

            with stat2:
                st.metric("Количество пробежек", "32")

            with stat3:
                st.metric("Средний темп", "6:10 мин/км")

        st.markdown("## Любимые тренировки")
        st.markdown("""
        <span class="badge">Лёгкий бег</span>
        <span class="badge">Пробежки в парке</span>
        <span class="badge">Интервалы</span>
        <span class="badge">Забеги 5 км</span>
        """, unsafe_allow_html=True)

        st.markdown("## Мои маршруты")

        for route in my_routes:
            st.markdown(f"<div class='small-card'>🗺️ {route}</div>", unsafe_allow_html=True)

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

    else:
        person = people.get(profile_user, people["Даня"])

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"# {person['avatar']}")

        with col2:
            st.markdown(f"## {profile_user}")
            st.write(person["description"])

            s1, s2, s3 = st.columns(3)

            with s1:
                st.metric("Километров пробежал", person["kilometers"])

            with s2:
                st.metric("Количество пробежек", person["runs_count"])

            with s3:
                st.metric("Средний темп", person["avg_pace"])

        st.markdown("## Последние тренировки")

        for item in person["last_runs"]:
            st.markdown(f"<div class='small-card'>🏃 {item}</div>", unsafe_allow_html=True)

        st.markdown("## Снаряжение")

        for item in person["gear"]:
            st.markdown(f"<div class='small-card'>🎒 {item}</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# 6. Мои пробежки
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
        "Участвовал в пробежке «Забег по городским улицам» — 10 мая",
        "Присоединился к команде «Утренний RUNCLUB» — 5 мая",
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
