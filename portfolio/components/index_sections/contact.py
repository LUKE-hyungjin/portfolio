import reflex as rx

def contact_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Let's talk",
                size="2xl",
                margin_bottom="1em",
                style={
                    "color": "white",
                    "font-size": ["40px", "60px", "80px"]  # 반응형 폰트 크기
                }
            ),
            rx.heading(
                "e93052080@gmail.com",
                size="lg",
                margin_bottom="2em",
                style={
                    "color": "white",
                    "font-size": ["20px", "25px", "30px"]  # 반응형 폰트 크기
                }
            ),
            rx.flex(  # 아이콘 링크를 위한 flex 컨테이너
                rx.link(
                    rx.vstack(  # 아이콘과 텍스트를 세로로 배치
                        rx.icon(
                            "github",
                            color="#ffffff",
                            width=["30px", "40px", "50px"],  # 반응형 크기
                            height=["30px", "40px", "50px"],
                        ),
                        rx.text( 
                            "GitHub",
                            color="white",  # 텍스트 색상을 흰색으로 설정
                            margin_top="-0.8em",  # 텍스트를 위로 올리기 위해 음수 마진 설정
                        ),
                        align_items="center",
                    ),
                    href="https://github.com/LUKE-hyungjin",
                    is_external=True,
                ),
                rx.link(
                    rx.vstack(  # 아이콘과 텍스트를 세로로 배치
                        rx.icon(
                            "panel-top",
                            color="#ffffff",
                            width=["30px", "40px", "50px"],  # 반응형 크기
                            height=["30px", "40px", "50px"],
                        ),
                        rx.text(  # Blog를 rx.text로 감싸서 스타일 적용
                            "Blog",
                            color="white",  # 텍스트 색상을 흰색으로 설정
                            margin_top="-0.8em",  # 텍스트를 위로 올리기 위해 음수 마진 설정
                        ),
                        align_items="center",
                    ),
                    href="https://informluke.tistory.com/",
                    is_external=True,
                    style={
                        "text_decoration": "none",  # 링크 밑줄 제거
                        "display": "flex",  # 아이콘과 텍스트를 가로로 정렬
                        "align_items": "center",  # 세로 중앙 정렬
                    }
                ),
                gap="4",
                spacing="4",
                margin_bottom="2em",
            ),
            rx.text(
                "2024 Luke - All rights reserved",
                color="white",
                font_size=["12px", "14px", "16px"],  # 반응형 폰트 크기
            ),
            align_items="center",  # 모든 요소 중앙 정렬
            padding=["2em", "2em", "4em"],  # 반응형 패딩
            width="100%",
        ),
        id="contact",
        style={
            "width": "100%",
            "min_height": "50vh",  # 최소 높이 설정
            "background": "#2C3E50",  # 배경색 설정
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
        },
    )
