import reflex as rx
from ...styles.styles import previous_font_style

def circle_icon(icon_name: str) -> rx.Component:
    return rx.box(
        rx.icon(
            icon_name,
            color="#FF9494",
            width = "100%",
            height = "100%",
        ),
        padding="2em",
        border="2px solid #FF9494",
        border_radius="50%",
        margin_bottom="1em",
        width="120px",
        height="120px",
        display="flex",
        align_items="center",
        justify_content="center",
    )

def skill_category(title: str, icon_name: str, skills: list[str]) -> rx.Component:
    return rx.vstack(
        circle_icon(icon_name),
        rx.heading(
            title,
            size="3",
            margin_bottom="1em",
            white_space="pre-wrap",
            text_align="center",
            height="2.5em",
            display="flex",
            align_items="center",
            justify_content="center",
            style={"color": "#000000", 
                   "font-size": ["24px", "27px", "30px"]},
        ),
        rx.vstack(
            *[
                rx.text(
                    skill, 
                    color="gray", 
                    margin_bottom="0.5em",
                    text_align="center",
                    height="1.5em",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    style={"font-size": ["16px", "17px", "18px"]},
                ) 
                for skill in skills
            ],
            spacing="2",
            min_height="200px",
            justify_content="flex-start",
        ),
        align_items="center",
        width="300px",
        margin="1em",
        height="100%",
    )

def about_section() -> rx.Component:
    coding_skills = ["Python", "C++", "Godot"]
    ai_skills = ["Numpy", "Tensorflow", "Pytorch", "Reinforcement Learning"]
    mech_skills = ["Mechanics of Materials", "Dynamics", "Thermodynamics", "Fluid Mechanics"]

    # 경력/학력 정보를 딕셔너리로 구조화
    experiences = {
        "BS : Kyonggi University(Mechanical Engineering)": "2018 - 2022",
        "SD solution Intern": "2021.01 - 2021.02",
        "Computer Aided Engineering Lab Undergraduate Researcher": "2020.08 - 2022.02",
        "Air Force Officer(Software Engineer)": "2022.08 - Present",
    }

    return rx.box(
        rx.vstack(
            rx.heading(
                "About me",
                size="1",
                margin_bottom="0.5em",
                text_align="center",
                style={"color": "#000000", "font-size": ["50px", "60px", "80px"]},
            ),
            rx.text(
                "I'm an Air Force officer developing software.",
                margin_bottom="1em",
                text_align="center",
                style={"color": "#000000", "font-size": ["16px", "18px", "20px"]},
            ),
            rx.flex(
                skill_category("Coding", "code", coding_skills),
                skill_category("AI", "cpu", ai_skills),
                skill_category("Mechanical\nEngineering", "settings", mech_skills),
                width="100%",
                justify="center",
                align_items="center",
                gap="4",
                wrap="wrap",
                padding=["1em", "2em", "2em"],
            ),
            # 경력/학력 정보 출력
            *[
                rx.vstack(
                    rx.text(
                        title,
                        color="black" if i == 0 or i == len(experiences) - 1 else "gray",  # 첫/마지막 항목은 검정, 나머지는 회색
                        font_weight="bold" if i == 0 or i == len(experiences) - 1 else "normal",  # 첫/마지막 항목은 볼드체
                    ),
                    rx.text(
                        period,
                        color="black" if i == 0 or i == len(experiences) - 1 else "gray",  # 첫/마지막 항목은 검정, 나머지는 회색
                    ),
                    spacing="2",
                    margin_bottom="1em",
                    align_items="center",
                )
                for i, (title, period) in enumerate(experiences.items())  # enumerate로 인덱스 추가
            ],
            align_items="center",
            padding=["2em", "2em", "4em"],
            width="100%",
        ),
        id="about",
        style={
            "width": "100%",
            "background": "#FFFFFF",
            "min_height": "100vh",
        },
    )