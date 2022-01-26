import pglet

from .tab_bar import TabBar
from .view import View


class App:
    def __init__(self, page, title=""):
        self.page = page
        page.title = title
        page.horizontal_align = "stretch"

        self._title = pglet.Text(title, size="xxlarge", align="center")
        self.tab_bar = TabBar()

        self.page.add(pglet.Stack(controls=[
            self._title,
            pglet.Stack(
                padding=40,
                horizontal_align="stretch",
                vertical_fill=True,
                controls=[
                    self.tab_bar.tabs,
                ])
        ]))

        self.tab_views = {}

        page.update()

    @property
    def title(self) -> str:
        return self._title.value

    @title.setter
    def title(self, value):
        self._title.value = value
        self._title.update()

    def update(self):
        self.page.update()

    def add_view(self, tab_view: View):
        self.tab_views[tab_view.text] = tab_view
        self.tab_bar.add_view(tab_view)
        self.page.update()

    @staticmethod
    def run(name, target, **kwargs):
        kwargs["target"] = target
        if "server" not in kwargs:
            kwargs["server"] = "http://localhost:8888"
        if "no_window" not in kwargs:
            kwargs["no_window"] = True

        # TODO: add logging (following should be log.info)
        print(f"Connecting to server: {kwargs['server']}")
        pglet.app(name, **kwargs)
