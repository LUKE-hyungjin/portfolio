import reflex as rx

def skill_bar(skill_name: str, percentage: int) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(skill_name, color="white", font_size="1.5em"),
            rx.spacer(),
            rx.text(f"{percentage}%", color="white", font_size="1.5em"),
            width="100%",
        ),
        rx.box(
            rx.box(
                width=f"{percentage}%",
                height="10px",
                background="#ffa500",
                border_radius="5px",
                transition="width 1s ease-in-out",
            ),
            width="100%",
            height="10px",
            background="rgba(255, 255, 255, 0.2)",
            border_radius="5px",
        ),
        width="100%",
        spacing="1em",
    )

def skills_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Skills", 
                size="2em", 
                margin_bottom="0.5em", 
                style={
                    "color": "#000000", 
                    "font-size": ["40px", "60px", "80px"]  # 반응형 폰트 크기
                }
            ),
            rx.heading(
                "Skills & Attributes", 
                size="xl", 
                margin_bottom="1em", 
                style={
                    "color": "#000000", 
                    "font-size": ["25px", "32px", "40px"]  # 반응형 폰트 크기
                }
            ),
            rx.text(
                "I major in mechanical engineering, but I also like coding.",
                margin_bottom="2em",
                text_align="center",  # 텍스트 중앙 정렬
                style={
                    "color": "#000000", 
                    "font-size": ["16px", "18px", "20px"]  # 반응형 폰트 크기
                }
            ),
            rx.box(
                rx.flex(  # hstack을 flex로 변경
                    # Left side - Skills
                    rx.vstack(
                        rx.heading(
                            "Skills", 
                            color="white", 
                            size="2em", 
                            margin_bottom="1.5em", 
                            style={"font-size": ["25px", "32px", "40px"]}
                        ),
                        skill_bar("Coding", 60),
                        skill_bar("Mechanical Engineering", 87),
                        width=["100%", "100%", "50%"],
                        padding="2em",
                    ),
                    # Right side - Tools
                    rx.vstack(
                        rx.heading(
                            "Tools", 
                            color="white", 
                            size="2em", 
                            margin_bottom="0.8em", 
                            align_self="center", 
                            style={"font-size": ["25px", "32px", "40px"]}
                        ),
                        rx.vstack(
                            rx.text("Inventor", color="white", font_size=["1.2em", "1.3em", "1.5em"]),
                            rx.text("Fusion 360", color="white", font_size=["1.2em", "1.3em", "1.5em"]),
                            rx.text("Ansys", color="white", font_size=["1.2em", "1.3em", "1.5em"]),
                            rx.text("Visual Studio Code", color="white", font_size=["1.2em", "1.3em", "1.5em"]),
                            spacing="1em",
                            align_items="center"
                        ),
                        rx.heading(
                            "Etc", 
                            color="white", 
                            size="2em", 
                            margin_top="2em", 
                            margin_bottom="0.8em", 
                            align_self="center", 
                            style={"font-size": ["25px", "32px", "40px"]}
                        ),
                        rx.text(
                            "Git, Docker", 
                            color="white", 
                            font_size=["1.2em", "1.3em", "1.5em"]
                        ),
                        width=["100%", "100%", "50%"],
                        padding="2em",
                        align_items="center",
                    ),
                    width="100%",
                    direction="column",  # 기본값을 column으로 설정
                    style={
                        "@media screen and (min-width: 768px)": {
                            "flex_direction": "row"  # 768px 이상에서는 row로 변경
                        }
                    },
                    background="#4a4a4a",
                    border_radius="1em",
                ),
                width=["95%", "90%", "80%"],
            ),
            align_items="center",
            width="100%",
            padding=["1em", "1.5em", "2em"],
        ),
        id="skills",
        style={
            "width": "100%",
            "background": "#FEF7D5",
            "min_height": "100vh",
            "padding": ["1em", "1.5em", "2em"],
        },
    )