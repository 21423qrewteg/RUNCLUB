import math
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# Дополнительные библиотеки для интерактивной карты
# ---------------------------------------------------------
# Если их нет, установите:
# pip install folium streamlit-folium

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
    }
]

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
    "Набережная Енисея — Центральный парк, 5 км",
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
    """Показывает интерактивную карту Яндекса."""
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
    """Показывает карточку тренировки в ленте."""
    with st.container(border=True):
        col_avatar, col_info = st.columns([1, 8])

        with col_avatar:
            st.markdown(f"## {activity['avatar']}")

        with col_info:
            st.markdown(f"### {activity['user']}")
            st.caption(activity["date"])

        st.markdown(f"## {activity['title']}")
        st.write(activity["description"])

        show_yandex_map(activity["map_url"], height=280)

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
            st.write(f"🔥 {activity['likes']} лайков")

        with react2:
            st.write(f"💬 {activity['comments']} комментариев")

        with react3:
            if st.button("Поставить лайк", key=f"like_{index}"):
                st.success("Вы поставили лайк!")


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Считает расстояние между двумя точками на Земле.
    Результат возвращается в километрах.
    """
    earth_radius = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    difference_lat = lat2 - lat1
    difference_lon = lon2 - lon1

    a = (
        math.sin(difference_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(difference_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c


def calculate_route_length(points):
    """
    Считает длину маршрута по списку точек.
    Каждая точка хранится как [широта, долгота].
    """
    if len(points) < 2:
        return 0

    total_distance = 0

    for index in range(len(points) - 1):
        lat1, lon1 = points[index]
        lat2, lon2 = points[index + 1]

        total_distance += haversine_distance(lat1, lon1, lat2, lon2)

    return total_distance


def format_minutes(minutes):
    """Красиво показывает время пробежки."""
    if minutes <= 0:
        return "0 мин"

    hours = int(minutes // 60)
    mins = int(minutes % 60)

    if hours > 0:
        return f"{hours} ч {mins} мин"

    return f"{mins} мин"


def extract_route_points(map_data):
    """
    Достаёт точки нарисованного маршрута из карты.
    Пользователь рисует линию на карте, а программа берёт координаты этой линии.
    """
    if not map_data:
        return []

    drawings = map_data.get("all_drawings")

    if not drawings:
        return []

    # Берём последний нарисованный объект
    last_drawing = drawings[-1]

    geometry = last_drawing.get("geometry", {})
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates", [])

    # Если нарисована линия, координаты идут в формате [долгота, широта]
    if geometry_type == "LineString":
        points = []

        for point in coordinates:
            lon = point[0]
            lat = point[1]
            points.append([lat, lon])

        return points

    return []


def create_route_map():
    """Создаёт карту Красноярска, на которой можно рисовать маршрут."""
    krasnoyarsk_center = [56.010563, 92.852572]

    route_map = folium.Map(
        location=krasnoyarsk_center,
        zoom_start=12,
        tiles="OpenStreetMap"
    )

    # Подсказка на карте
    folium.Marker(
        krasnoyarsk_center,
        tooltip="Красноярск",
        popup="Нарисуйте маршрут линией на карте"
    ).add_to(route_map)

    # Инструмент рисования маршрута
    draw = Draw(
        export=False,
        draw_options={
            "polyline": True,
            "polygon": False,
            "circle": False,
            "rectangle": False,
            "marker": False,
            "circlemarker": False
        },
        edit_options={
            "edit": True,
            "remove": True
        }
    )

    draw.add_to(route_map)

    return route_map


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
                    padding: 18px;
                    border: 1px solid #e5e7eb;
                }

                .hint {
                    background: #fff7ed;
                    border: 1px solid #fed7aa;
                    color: #9a3412;
                    padding: 12px;
                    border-radius: 12px;
                    margin-bottom: 14px;
                    font-size: 15px;
                }

                .buttons {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    margin-bottom: 14px;
                }

                button {
                    border: none;
                    border-radius: 12px;
                    padding: 12px 16px;
                    font-size: 15px;
                    font-weight: 700;
                    cursor: pointer;
                }

                .main-button {
                    background: #fc4c02;
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
                    height: 520px;
                    width: 100%;
                    border-radius: 18px;
                    border: 1px solid #d1d5db;
                    margin-bottom: 18px;
                }

                .controls {
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 14px;
                    margin-top: 12px;
                }

                .control-card {
                    background: #f9fafb;
                    border: 1px solid #e5e7eb;
                    border-radius: 14px;
                    padding: 14px;
                }

                .control-card label {
                    font-size: 14px;
                    color: #4b5563;
                    display: block;
                    margin-bottom: 8px;
                }

                .control-card input {
                    width: 100%;
                    box-sizing: border-box;
                    padding: 9px;
                    border-radius: 8px;
                    border: 1px solid #d1d5db;
                    font-size: 15px;
                }

                .metric {
                    font-size: 26px;
                    font-weight: 800;
                    color: #111827;
                    margin-top: 6px;
                }

                .success {
                    background: #dcfce7;
                    color: #166534;
                    padding: 12px;
                    border-radius: 12px;
                    border: 1px solid #86efac;
                    margin-top: 14px;
                    display: none;
                }

                .status {
                    background: #eef2ff;
                    color: #3730a3;
                    padding: 10px;
                    border-radius: 12px;
                    margin-bottom: 12px;
                    font-size: 15px;
                }
            </style>
        </head>

        <body>
            <div class="app-box">

                <div class="hint">
                    1. Нажмите «Начать маршрут».<br>
                    2. Кликайте по карте, чтобы ставить точки маршрута.<br>
                    3. Нажмите «Поставить финиш», затем кликните по карте в месте финиша.<br>
                    4. Длина и примерное время будут считаться автоматически.
                </div>

                <div class="status" id="statusText">
                    Режим: маршрут ещё не начат.
                </div>

                <div class="buttons">
                    <button class="main-button" onclick="startRoute()">▶️ Начать маршрут</button>
                    <button class="green-button" onclick="enableFinishMode()">🏁 Поставить финиш</button>
                    <button class="blue-button" onclick="finishRoute()">✅ Завершить маршрут</button>
                    <button class="gray-button" onclick="removeLastPoint()">↩️ Удалить последнюю точку</button>
                    <button class="red-button" onclick="clearRoute()">🗑️ Очистить маршрут</button>
                </div>

                <div id="map"></div>

                <div class="controls">
                    <div class="control-card">
                        <label>Название маршрута</label>
                        <input id="routeName" type="text" value="Пробежка по Красноярску">
                    </div>

                    <div class="control-card">
                        <label>Дата начала пробежки</label>
                        <input id="runDate" type="date">
                    </div>

                    <div class="control-card">
                        <label>Темп, мин/км</label>
                        <input id="pace" type="number" value="6.0" min="3" max="12" step="0.1" oninput="updateInfo()">
                    </div>

                    <div class="control-card">
                        <label>Количество точек</label>
                        <div class="metric" id="pointsCount">0</div>
                    </div>
                </div>

                <div class="controls">
                    <div class="control-card">
                        <label>Длина маршрута</label>
                        <div class="metric" id="distance">0.00 км</div>
                    </div>

                    <div class="control-card">
                        <label>Выбранный темп</label>
                        <div class="metric" id="paceText">6.0 мин/км</div>
                    </div>

                    <div class="control-card">
                        <label>Примерное время</label>
                        <div class="metric" id="timeText">0 мин</div>
                    </div>

                    <div class="control-card">
                        <label>Сохранение</label>
                        <button class="main-button" onclick="saveRoute()">Создать маршрут</button>
                    </div>
                </div>

                <div class="success" id="successBox">
                    ✅ Маршрут создан!
                </div>
            </div>

            <script>
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
                // Включить режим постановки финиша
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
                        "Режим: кликните по карте, чтобы поставить точку финиша.";
                }

                // ---------------------------------------------------------
                // Завершить маршрут по последней поставленной точке
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
                        alert("Маршрут уже завершён. Нажмите «Очистить маршрут», чтобы построить новый.");
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
                            color: "#fc4c02",
                            fillColor: "#fc4c02",
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
                            color: "#fc4c02",
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
                                color: "#fc4c02",
                                fillColor: "#fc4c02",
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

                    document.getElementById("paceText").innerText =
                        pace.toFixed(1) + " мин/км";

                    document.getElementById("timeText").innerText =
                        formatTime(totalMinutes);

                    document.getElementById("pointsCount").innerText =
                        routePoints.length;
                }

                // ---------------------------------------------------------
                // Сохранить маршрут
                // ---------------------------------------------------------
                function saveRoute() {
                    var name = document.getElementById("routeName").value;
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

                    var successBox = document.getElementById("successBox");

                    successBox.style.display = "block";
                    successBox.innerHTML =
                        "✅ Маршрут <b>" + name + "</b> создан!<br>" +
                        "Дата: <b>" + date + "</b><br>" +
                        "Длина: <b>" + routeDistance.toFixed(2) + " км</b><br>" +
                        "Темп: <b>" + pace + " мин/км</b><br>" +
                        "Примерное время: <b>" + time + "</b>";
                }

                updateInfo();
            </script>
        </body>
        </html>
        """,
        height=930
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
