import pglet


class Markdown(pglet.Text):
    def __init__(self, *args, **kwargs):
        kwargs["markdown"] = True
        super(Markdown, self).__init__(*args, **kwargs)
