from pylet import Adapter

from votingapp.models import Vote
from votingapp.views import VoteView


class VoteAdapter(Adapter[Vote, VoteView]):
    def __init__(self, vote: Vote):
        super().__init__(vote)

    def build_view(self):
        return VoteView(
            election_name=self.model.election_name,
            candidates=self.model.candidates,
            state_county=self.model.state_county,
            on_submit=self.on_submit
        )

    def on_submit(self, data):
        err = self.model.post_vote(data)
        if err:
            self.view.message(f"There was an error submitting the vote: {err}", kind="Error")
        else:
            self.view.message("Vote successfully submitted.", kind="success")
