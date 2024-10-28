# Common styles
navbar_style = {
            "position": "fixed",  # 스크롤해도 고정되도록 설정
            "top": "0",  # 페이지 최상단에 위치
            "width": "100%",
            "zIndex": "3",
            "background": "rgba(38, 67, 86, 0.8)",  # 초기에는 투명한 배경
            "padding": "20px",
            "transition": "background 0.3s ease",  # 배경색 변경 애니메이션 추가
        }

background_image_style = {
                    "position": "absolute",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "filter": "blur(3px)",
                    "zIndex": "1",
                }

profile_image_style = {
    "position": "relative",
    "top": "60px",
    "width": "100%",
    "height": "100%",
    "objectFit": "cover",
    "borderRadius": "100px",
    "border": "5px solid white",
}

section_container = {
    "position": "relative",
    "width": "100%",
    "height": "90vh",
    "overflow": "hidden",
}

about_title_style = {
    "position": "relative",
    "font-size": "80px",
    "color": "#000000",
    "top": "40px"
}
