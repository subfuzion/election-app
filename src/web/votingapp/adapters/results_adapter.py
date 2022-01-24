from pylet import Adapter

from votingapp.models import Vote
from votingapp.views import ResultsView


class ResultsAdapter(Adapter[Vote, ResultsView]):
    def __init__(self, vote: Vote):
        super().__init__(vote)

    def build_view(self) -> ResultsView:
        return ResultsView(
            election_name=self.model.election_name,
            candidates=self.model.candidates,
            state_county=self.model.state_county,
            on_submit=self.on_submit,
        )

    def on_submit(self):
        ok, data = self.model.get_results()
        if not ok:
            # TODO
            pass
        else:
            winner, results = data
            self.view.set_results(winner, results)
