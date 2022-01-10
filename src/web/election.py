import election_api as api


class Election:
    """
    Election is a thin wrapper over the election service api that renders data
    in a format to be used for rendering the UI.
    """

    def __init__(self, api_url):
        self.api = api
        self.api_url = api_url

    def get_election_name(self):
        return self.api.get_election_name()

    def get_candidates(self):
        return self.api.get_candidates()

    def cast_vote(self, voter, candidate):
        return self.api.cast_vote(voter, candidate)

    def get_vote_tally_by_candidates(self):
        return self.api.tally_votes_by_candidate()

    def get_state_county(self):
        """
        Returns a dictionary that maps states to counties
        """
        return self.api.get_state_county()
