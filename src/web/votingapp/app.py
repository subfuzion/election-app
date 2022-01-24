from pylet import App

from adapters import ResultsAdapter, VoteAdapter
from config import Config
from models import Vote


class ElectionApp(App):
    def __init__(self, page):
        super().__init__(page)
        self.title = "Voting App Demo"
        self._config = Config()

        # App model
        vote = Vote(self.config)

        # Adapters use models, create views, and coordinate between them.
        vote_adapter = VoteAdapter(vote)
        results_adapter = ResultsAdapter(vote)

        # Adapters' views are added to the App's page, so they can be displayed.
        self.add_view(vote_adapter.view)
        self.add_view(results_adapter.view)

    @property
    def config(self) -> Config:
        return self._config


# App page will be mounted at /p/vote.
App.run("vote", ElectionApp)
