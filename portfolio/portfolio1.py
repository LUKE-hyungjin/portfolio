import reflex as rx

def scroll_to(section_id):
    return rx.scroll_to(section_id)

def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            navbar(),
            rx.image(
                src="/home_background.png",
                width="100%",
                height="100%",
                alt="Background",
                style={
                    "position": "absolute",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "filter": "blur(3px)",
                    "zIndex": "1",
                }
            ),
            rx.box(
                rx.vstack(
                    rx.image(
                        src="/profile.jpeg",
                        width="300px",
                        height="300px",
                        style={
                            "position": "relative",
                            "top": "60px",
                            "width": "100%",
                            "height": "100%",
                            "objectFit": "cover",
                            "borderRadius": "100px",
                            "border": "5px solid white",
                        }
                    ),
                    rx.text(
                        "Hi! I'm Hyungjin Lee.",
                        size="9",
                        weight="bold",
                        style={
                            "position": "relative",
                            "top": "70px",
                        }
                    ),
                    rx.text(
                        "I am a student studying the fusion of machines and computers.",
                        size="7",
                        style={
                            "position": "relative",
                            "top": "80px",
                        }
                    ),
                    rx.hstack(
                        rx.button("Contact", on_click=scroll_to("section1")),
                        rx.button("Download CV"),
                        style={
                            "position": "relative",
                            "top": "80px",
                        }
                    ),
                    align_items="center",
                    style={
                        "position": "relative",
                        "top": "40px",
                        "zIndex": "2",
                    }
                ),
            ),
            "This is Section 1",
            id="section1",
            style={
                "position": "relative",
                "width": "100%",
                "height": "90vh",
                "overflow": "hidden",
            }
        ),
        rx.box(
            rx.vstack(
            rx.text(
                "About Me",
                style={
                    "position" : "relative",
                    "font-size" : "80px",
                    "color" : "#000000",
                    "top" : "40px"
                }
            ),
            rx.text("I'm a Mechanical Engineering student",
                    style={
                        "position" : "relative",
                        "color" : "#000000",
                        "top" : "40px"
                    }),
            rx.hstack(
                rx.vstack(
                    rx.text("Coding"),
                    rx.text(),
                ),
                rx.vstack(
                    rx.text("AI"),
                    rx.text(),
                ),
                rx.vstack(
                    rx.text("MechanicalEngineering"),
                    rx.text(),
                ),
                style={
                        "position" : "relative",
                        "color" : "#000000",
                        "top" : "40px"
                    }
            ),
            align_items="center",
            ),
            id="section2",
            style={"height": "100vh", "width" : "100%", "background": "#FFFFFF"},
        ),
        rx.box(
            "This is Section 3",
            id="section3",
            style={"height": "100vh", "background": "lightcoral"},
        ),
        spacing="0",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("LUKE", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    rx.link(rx.text("Home", size="4", weight="medium", on_click=scroll_to("section1"))),
                    rx.link(rx.text("About", size="4", weight="medium", on_click=scroll_to("section2"))),
                    rx.link(rx.text("Skill", size="4", weight="medium", on_click=scroll_to("section3"))),
                    rx.link(rx.text("My Work", size="4", weight="medium", on_click=scroll_to("section1"))),
                    rx.link(rx.text("Contact", size="4", weight="medium", on_click=scroll_to("section1"))),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
            rx.mobile_and_tablet(
                rx.hstack(
                    rx.image(
                        src="/favicon.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Skill"),
                        rx.menu.item("My Work"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style={
            "position": "fixed",  # 스크롤해도 고정되도록 설정
            "top": "0",  # 페이지 최상단에 위치
            "width": "100%",
            "zIndex": "3",
            "background": "rgba(38, 67, 86, 0.8)",  # 초기에는 투명한 배경
            "padding": "20px",
            "transition": "background 0.3s ease",  # 배경색 변경 애니메이션 추가
        },
        id="navbar",
        
    )

app = rx.App()
app.add_page(index)
