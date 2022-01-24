from typing import TypeVar

import pglet

T = TypeVar('T', bound=pglet.Control)


class View(pglet.Tab):
    """
    This is the View in the Model-View-Adapter pattern.
    View content is bound to a specific type of Control as the only
    visual element.
    """

    def __init__(self, title: str = "", control: T = None, **kwargs):
        super().__init__(text=title, **kwargs)
        self.content = control

    @property
    def content(self) -> T:
        return super().controls[0]

    @content.setter
    def content(self, content: T):
        super().controls.clear()
        super().controls.insert(0, content)
