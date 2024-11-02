import reflex as rx
from typing import List, Optional

class WorkState(rx.State):
    selected_filter: str = "*"
    
    def set_filter(self, category: str):
        self.selected_filter = category

def project_card(href: str, img_src: str, title: str, description: str, data_type: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.box(
                rx.image(
                    src=img_src,
                    width="100%",
                    height="100%",
                    object_fit="contain",
                    position="absolute",
                    top="50%",
                    left="50%",
                    style={
                        "transform": "translate(-50%, -50%)",
                    },
                ),
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background="#EEEEEE",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.box(
                rx.heading(title, size="sm"),
                rx.text(description, font_size="sm"),
                padding="0.75em",
                background="rgba(0, 0, 0, 0.75)",
                color="white",
                position="absolute",
                bottom="0",
                width="100%",
                opacity="0",
                _hover={"opacity": 1},
                transition="opacity 0.3s",
            ),
            position="relative",
            overflow="hidden",
            border_radius="lg",
            width="100%",
            min_width="280px",
            min_height="250px",
            align_items="center",
            justify_content="center",
            background="#EEEEEE",
        ),
        href=href,
        is_external=True,
        data_type=data_type,
    )

def category_button(text: str, count: int, filter_value: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            text,
            rx.box(
                str(count),
                background="rgba(255, 255, 255, 0.3)",
                padding="0.2em 0.6em",
                border_radius="20px",
                margin_left="0.8em",
                font_weight="bold",
            ),
            spacing="2",
        ),
        on_click=WorkState.set_filter(filter_value),
        bg=rx.cond(WorkState.selected_filter == filter_value, "blue.500", "blue.400"),
        color="white",
        _hover={"bg": "blue.600"},
        padding="0.8em 1.5em",
        font_size="1.1em",
        border_radius="lg",
        min_width="150px",
    )

def work_section() -> rx.Component:
    projects = [
        {"title": "Python", "img": "/pythonLv1.png", "description": "Lv1", "type": "coding", "href": "https://www.inflearn.com/certificate/624434-326414-7886802"},
        {"title": "Python", "img": "/pythonLv2.png", "description": "Lv2", "type": "coding", "href": "https://www.inflearn.com/certificate/624434-326461-10288918"},
        {"title": "TensorFlow", "img": "/tensorflow.png", "description": "TensorFlow Developer Certificate", "type": "AI", "href": "https://api.accredible.com/v1/frontend/credential_website_embed_image/certificate/30539390"},
        {"title": "Reinforcement Learning", "img": "/mq9-reaper.jpeg", "description": "Reinforcement Learning Applied to Airplanes", "type": "AI", "href": "https://www.facebook.com/groups/ReinforcementLearningKR/permalink/2981005235472030/"},
        {"title": "Reinforcement Learning", "img": "/drone.png", "description": "Reinforcement Learning Applied to Drones", "type": "AI", "href": "https://unitysquare.co.kr/madewith/industry/view?bidx=2&idx=425"},
        {"title": "Modelling", "img": "/escalade.png", "description": "Escalade modeling", "type": "ME", "href": "https://informluke.tistory.com/entry/%EC%97%90%EC%8A%A4%EC%BB%AC%EB%A0%88%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81"},
        {"title": "Modelling", "img": "/defenserobot.jpg", "description": "Defense robot modelling", "type": "ME", "href": "https://www.youtube.com/watch?v=NY-tPyoulmk"},
    ]

    return rx.box(
        rx.vstack(
            rx.heading("My Work", size="2xl", margin_bottom="0.5em", style={"color": "#000000","font-size": "80px"}),
            rx.heading("Projects", size="xl", margin_bottom="1em", style={"color": "#000000","font-size": "40px"}),
            rx.flex(
                category_button("All", len(projects), "*"),
                category_button("Coding", len([p for p in projects if p["type"] == "coding"]), "coding"),
                category_button("AI", len([p for p in projects if p["type"] == "AI"]), "AI"),
                category_button("Mechanical Engineering", len([p for p in projects if p["type"] == "ME"]), "ME"),
                gap="6",
                margin_bottom="2em",
                justify="center",
                wrap="wrap",
                width="100%",
                padding="1em",
                spacing="6",
            ),
            rx.flex(
                rx.foreach(
                    projects,
                    lambda project: rx.cond(
                        (WorkState.selected_filter == "*") | (WorkState.selected_filter == project["type"]),
                        project_card(
                            project["href"],
                            project["img"],
                            project["title"],
                            project["description"],
                            project["type"]
                        ),
                        None
                    )
                ),
                wrap="wrap",
                gap="4",
                width="100%",
                justify_content="center",
                align_items="center",
            ),
            align_items="center",
            padding=["2em", "2em", "4em", "4em"],
            width="100%",
        ),
        id="work",
        style={
            "width": "100%",
            "min_height": "100vh",
            "background": "#FFFFFF",
        },
    )
