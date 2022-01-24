import pglet

from pylet import Markdown, View


class ResultsView(View):
    def __init__(self, election_name="", candidates=None, state_county=None, on_submit=None):
        super().__init__()
        self.text = "Results"
        self.icon = "Checklist"

        self.on_submit = on_submit

        self.election_name = election_name
        self.candidates = candidates
        self.state_county = state_county

        self.election_name_control = pglet.Text(
            self.election_name,
            size="xlarge"
        )

        self.get_results_control = self._create_get_results_control()
        self.results_markdown_control = Markdown()
        self.results_control = self._create_results_control(self.results_markdown_control)

        self.content = pglet.Stack(controls=[
            self.election_name_control,
            self.get_results_control,
            self.results_control,
        ])

    def _create_get_results_control(self):
        def submit(e):
            self.results_control.visible = True
            self.results_control.update()
            if self.on_submit:
                self.on_submit()

        return pglet.Button(
            "Get results",
            title="Get latest voting results",
            icon="Page",
            on_click=submit,
            primary=True,
            width=150,
        )

    def _create_results_control(self, text):
        return pglet.Stack(
            border="1px solid #DDD",
            border_radius="0",
            padding=20,
            bgcolor="#FDFDFD",
            visible=False,
            controls=[
                text,
            ]
        )

    def set_results(self, winner, results):
        # TODO: generating this probably belongs in the adapter
        tallies = ""
        for tally in results:
            tallies += f"- {self.candidates[tally]['name']}: {results[tally]}\n"

        self.results_markdown_control.value = f"""
## {winner} wins!
""" + tallies
        self.results_markdown_control.update()
