import pglet


class Textbox(pglet.Textbox):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        # hack to suppress default label
        if "label" not in kwargs:
            self.label = ""

    @pglet.Textbox.value.setter
    def value(self, value):
        super()._set_attr("value", value)
        if self.on_change:
            e = pglet.Event(self.uid, "change", data=value)
            self.on_change(e)
            self.update()
