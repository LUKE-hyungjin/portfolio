import reflex as rx
from ..components.index_sections.home import home_section
from ..components.index_sections.about import about_section
# from ..components.sections.skills import skills_section

def index() -> rx.Component:
    return rx.vstack(
        home_section(),
        about_section(),
        # skills_section(),
        spacing="0",
    )
