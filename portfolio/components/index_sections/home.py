import reflex as rx
from ...styles.styles import background_image_style, profile_image_style
from ..navbar import navbar

def scroll_to(section_id):
    return rx.scroll_to(section_id)

def home_section() -> rx.Component:
    return rx.box(
            navbar(),
            rx.image(
                src="/home_background.png",
                width="100%",
                height="100%",
                alt="Background",
                style=background_image_style
            ),
            rx.box(
                rx.vstack(
                    rx.image(
                        src="/profile.jpeg",
                        width="300px",
                        height="300px",
                        style=profile_image_style
                    ),
                    rx.text(
                        "Hi! I'm Hyungjin Lee.",
                        size="9",
                        weight="bold",
                        text_align="center",
                        style={
                            "position": "relative",
                            "top": "70px",
                        }
                    ),
                    rx.text(
                        "I am a student studying the fusion of machines and computers.",
                        size="7",
                        text_align="center",
                        style={
                            "position": "relative",
                            "top": "80px",
                        }
                    ),
                    rx.flex(
                        rx.button("Contact", on_click=scroll_to("section1")),
                        rx.link(  # button을 link로 감싸기
                            rx.button("Download CV"),
                            href="/CV.pdf",  # assets 폴더의 파일 경로
                            is_external=True,  # 새 탭에서 열기
                            download=True,  # 다운로드 속성 추가
                        ),
                        gap="6",
                        wrap="wrap",
                        spacing="6",
                        justify="center",
                        width="100%",
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
            id="home",
            style={
                "position": "relative",
                "width": "100%",
                "height": "90vh",
                "overflow": "hidden",
            }
        )