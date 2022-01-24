import pglet


class TabBar:
    def __init__(self):
        self.tabs = pglet.Tabs(margin=40)

    def add_view(self, tab):
        self.tabs.tabs.append(tab)

    def on_change(self, handler) -> None:
        self.tabs.on_change = handler
