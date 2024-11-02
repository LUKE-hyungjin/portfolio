import reflex as rx
from ..styles.styles import navbar_style

def scroll_to(section_id):
    return rx.scroll_to(section_id)

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
                    rx.link(rx.text("Home", size="4", weight="medium", on_click=scroll_to("home"))),
                    rx.link(rx.text("About", size="4", weight="medium", on_click=scroll_to("about"))),
                    rx.link(rx.text("Skill", size="4", weight="medium", on_click=scroll_to("skills"))),
                    rx.link(rx.text("My Work", size="4", weight="medium", on_click=scroll_to("work"))),
                    rx.link(rx.text("Contact", size="4", weight="medium", on_click=scroll_to("contact"))),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
            rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "LUKE", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=scroll_to("home")),
                        rx.menu.item("About", on_click=scroll_to("about")),
                        rx.menu.item("Skill", on_click=scroll_to("skills")),
                        rx.menu.item("My Work", on_click=scroll_to("work")),
                        rx.menu.item("Contact", on_click=scroll_to("contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=navbar_style,
        id="navbar",
    )