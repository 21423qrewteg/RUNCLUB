import json
import math
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
# Общие стили приложения
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

    .red-text {
        color: #dc2626;
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

    .info-card {
        background-color: white;
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Демонстрационные данные
# ---------------------------------------------------------

# Лента тренировок других участников
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
        "points": [
            [56.0211, 92.8702],
            [56.0174, 92.8790],
            [56.0125, 92.8867],
            [56.0081, 92.8952],
            [56.0045, 92.9040]
        ]
    },
    {
        "user": "Аня",
        "avatar": "🎧",
        "date": "Вчера, 19:10",
        "title": "Вечерний бег в парке",
        "description": "Спокойная тренировка после школы. В следующий раз хочет собрать компанию.",
        "distance": "3.8 км",
        "pace": "6:20 мин/км",
        "time": "24 мин",
        "likes": 18,
        "comments": 5,
        "status": "Завершено",
        "points": [
            [56.0120, 92.8244],
            [56.0151, 92.8290],
            [56.0175, 92.8355],
            [56.0142, 92.8420],
            [56.0100, 92.8360]
        ]
    },
    {
        "user": "Маша",
        "avatar": "🏃‍♀️",
        "date": "Вчера, 17:45",
        "title": "Быстрая тренировка на стадионе",
        "description": "Интервалы и работа над скоростью. Было сложно, но результат отличный.",
        "distance": "4.0 км",
        "pace": "5:10 мин/км",
        "time": "21 мин",
        "likes": 21,
        "comments": 4,
        "status": "Завершено",
        "points": [
            [56.0152, 92.8930],
            [56.0170, 92.8975],
            [56.0144, 92.9022],
            [56.0117, 92.8981],
            [56.0152, 92.8930]
        ]
    },
    {
        "user": "Игорь",
        "avatar": "⌚",
        "date": "2 дня назад",
        "title": "Длинный маршрут по Красноярску",
        "description": "Пробежал новый маршрут через несколько районов города.",
        "distance": "8.5 км",
        "pace": "6:05 мин/км",
        "time": "52 мин",
        "likes": 15,
        "comments": 2,
        "status": "Завершено",
        "points": [
            [56.0465, 92.9342],
            [56.0410, 92.9201],
            [56.0350, 92.9062],
            [56.0272, 92.8910],
            [56.0200, 92.8765],
            [56.0140, 92.8650]
        ]
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
def get_query_value(name, default=""):
    """Получает значение из адресной строки браузера."""
    value = st.query_params.get(name, default)

    if isinstance(value, list):
        return value[0] if len(value) > 0 else default

    return value


def get_status_class(status):
    """Возвращает CSS-класс для статуса события."""
    if status == "запланировано":
        return "status-planned"
    if status == "завершено":
        return "status-done"
    return "status-cancelled"


def show_activity_map(points, map_key):
    """
    Показывает карту с треком.
    Карта строится через Leaflet внутри HTML, поэтому дополнительные Python-библиотеки не нужны.
    """
    points_json = json.dumps(points)

    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">

            <link
                rel="stylesheet"
                href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
            />

            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

            <style>
                body {{
                    margin: 0;
                }}

                #map_{map_key} {{
                    height: 280px;
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
                        weight: 6
                    }}).addTo(map);

                    L.marker(points[0]).addTo(map).bindPopup("📍 Старт");

                    if (points.length > 1) {{
                        L.marker(points[points.length - 1]).addTo(map).bindPopup("🏁 Финиш");
                    }}

                    map.fitBounds(line.getBounds(), {{
                        padding: [25, 25]
                    }});
                }} else {{
                    map.setView([56.010563, 92.852572], 12);
                }}
            </script>
        </body>
        </html>
        """,
        height=300
    )


def show_activity_card(activity, index, is_user=False):
    """Показывает карточку тренировки в стартовой ленте."""
    with st.container(border=True):
        col_avatar, col_info = st.columns([1, 8])

        with col_avatar:
            st.markdown(f"## {activity['avatar']}")

        with col_info:
            if is_user:
                st.markdown(f"### {activity['user']} <span class='red-text'>— ваш маршрут</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"### {activity['user']}")

            st.caption(activity["date"])

        st.markdown(f"## {activity['title']}")
        st.write(activity["description"])

        show_activity_map(activity["points"], f"activity_{index}")

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

        st.markdown("---")

        react1, react2, react3 = st.columns([1, 1, 4])

        with react1:
            st.write(f"❤️ {activity['likes']} лайков")

        with react2:
            st.write(f"💬 {activity['comments']} комментариев")

        with react3:
            if st.button("Поставить лайк", key=f"like_{index}"):
                st.success("Вы поставили лайк!")


# ---------------------------------------------------------
# Боковое меню
# ---------------------------------------------------------
pages = [
    "Стартовое окно",
    "Создать маршрут",
    "Найти компанию",
    "Чат",
    "Профиль",
    "Мои пробежки"
]

# Если пользователь пришёл после сохранения маршрута, открываем стартовое окно
page_from_url = get_query_value("page", "Стартовое окно")

if page_from_url in pages:
    default_page_index = pages.index(page_from_url)
else:
    default_page_index = 0

st.sidebar.title("🏃 RunMate")
st.sidebar.write("Меню приложения")

page = st.sidebar.radio(
    "Выберите раздел:",
    pages,
    index=default_page_index
)

st.sidebar.markdown("---")
st.sidebar.info("Школьный проект по информатике: поиск компании для бега.")


# ---------------------------------------------------------
# 1. Стартовое окно — лента тренировок
# ---------------------------------------------------------
if page == "Стартовое окно":
    st.markdown('<div class="big-title">RunMate 🏃‍♂️</div>', unsafe_allow_html=True)
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

    # Проверяем, был ли сохранён маршрут из окна «Создать маршрут»
    saved_route = get_query_value("saved_route", "0")

    if saved_route == "1":
        title = get_query_value("title", "Мой маршрут")
        description = get_query_value("description", "Маршрут создан в приложении RunMate.")
        date = get_query_value("date", "Дата не выбрана")
        distance = get_query_value("distance", "0.00")
        pace = get_query_value("pace", "6.0")
        time = get_query_value("time", "0 мин")
        points_text = get_query_value("points", "[]")

        try:
            user_points = json.loads(points_text)
        except Exception:
            user_points = []

        user_activity = {
            "user": "Вы",
            "avatar": "🙂",
            "date": date,
            "title": title,
            "description": description,
            "distance": f"{distance} км",
            "pace": f"{pace} мин/км",
            "time": time,
            "likes": 0,
            "comments": 0,
            "status": "Запланировано",
            "points": user_points
        }

        show_activity_card(user_activity, "user_saved", is_user=True)
        st.write("")

    for index, activity in enumerate(feed_activities):
        show_activity_card(activity, index)
        st.write("")


# ---------------------------------------------------------
# 2. Создать маршрут
# ---------------------------------------------------------
elif page == "Создать маршрут":
    st.markdown('<div class="big-title">Создать маршрут 🗺️</div>', unsafe_allow_html=True)
    st.write(
        "Поставьте точки маршрута на карте. Приложение само посчитает длину "
        "и примерное время пробежки по выбранному темпу."
    )

    components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">

            <link
                rel="stylesheet"
                href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
            />

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

                .main-button:hover {
                    background: #b91c1c;
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

                .red-button:hover {
                    background: #b91c1c;
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

                .save-button:hover {
                    background: #b91c1c;
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
                    transform: translateY(20px);
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
                    1. Нажмите «Начать маршрут». 
                    2. Кликайте по карте, чтобы ставить точки.
                    3. Нажмите «Поставить финиш», затем кликните по карте.
                    4. Длина и время считаются автоматически.
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
                        <input id="routeDescription" type="text" value="Мой новый маршрут для пробежки.">
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
                    <p>
                        Сейчас вы будете перенаправлены на стартовое окно.
                        Там появится ваша тренировка с картой, дистанцией, темпом и временем.
                    </p>
                </div>
            </div>

            <script>
                // ---------------------------------------------------------
                // Настройка ограничения даты: сегодня + максимум 5 дней
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Создание карты
                // ---------------------------------------------------------
                var map = L.map('map').setView([56.010563, 92.852572], 12);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }).addTo(map);

                // ---------------------------------------------------------
                // Переменные маршрута
                // ---------------------------------------------------------
                var routePoints = [];
                var routeMarkers = [];
                var routeLine = null;
                var startMarker = null;
                var finishMarker = null;

                var routeStarted = false;
                var finishMode = false;
                var routeFinished = false;
                var routeDistance = 0;

                // ---------------------------------------------------------
                // Начать маршрут
                // ---------------------------------------------------------
                function startRoute() {
                    clearRoute();

                    routeStarted = true;
                    finishMode = false;
                    routeFinished = false;

                    document.getElementById("statusText").innerText =
                        "Режим: ставьте точки маршрута кликами по карте.";
                }

                // ---------------------------------------------------------
                // Включить режим финиша
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Завершить маршрут по последней точке
                // ---------------------------------------------------------
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

                    finishMarker = L.marker(lastPoint, {
                        title: "Финиш"
                    }).addTo(map).bindPopup("🏁 Финиш");

                    document.getElementById("statusText").innerText =
                        "Маршрут завершён. Длина и время рассчитаны.";
                }

                // ---------------------------------------------------------
                // Клик по карте
                // ---------------------------------------------------------
                map.on('click', function(event) {
                    if (!routeStarted) {
                        return;
                    }

                    if (routeFinished) {
                        alert("Маршрут уже завершён. Нажмите «Очистить», чтобы построить новый.");
                        return;
                    }

                    var point = event.latlng;

                    routePoints.push(point);

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

                // ---------------------------------------------------------
                // Перерисовка линии маршрута
                // ---------------------------------------------------------
                function redrawRoute() {
                    if (routeLine !== null) {
                        map.removeLayer(routeLine);
                    }

                    if (routePoints.length >= 2) {
                        routeLine = L.polyline(routePoints, {
                            color: "#dc2626",
                            weight: 6
                        }).addTo(map);
                    }
                }

                // ---------------------------------------------------------
                // Удалить последнюю точку
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Полностью перерисовать маркеры
                // ---------------------------------------------------------
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
                            startMarker = L.marker(point)
                                .addTo(map)
                                .bindPopup("📍 Старт");
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

                // ---------------------------------------------------------
                // Очистить маршрут
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Расчёт длины маршрута
                // ---------------------------------------------------------
                function calculateDistance() {
                    var distanceMeters = 0;

                    if (routePoints.length < 2) {
                        return 0;
                    }

                    for (var i = 0; i < routePoints.length - 1; i++) {
                        distanceMeters += routePoints[i].distanceTo(routePoints[i + 1]);
                    }

                    return distanceMeters / 1000;
                }

                // ---------------------------------------------------------
                // Форматирование времени
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Обновление длины, темпа и времени
                // ---------------------------------------------------------
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

                // ---------------------------------------------------------
                // Сохранить маршрут и перейти на стартовое окно
                // ---------------------------------------------------------
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

                    var simplePoints = [];

                    for (var i = 0; i < routePoints.length; i++) {
                        simplePoints.push([
                            routePoints[i].lat,
                            routePoints[i].lng
                        ]);
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
                    params.set("points", JSON.stringify(simplePoints));

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
