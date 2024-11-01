import reflex as rx
def about_section() -> rx.Component:
    return rx.box(
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
        )