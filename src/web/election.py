import election_api_mock as mock

_STATE_COUNTY = {
    "California": ["Fresno", "Alameda", "Sacramento"],
    "Arizona": ["La Paz", "Maricopa", "Mohave"],
}


def get_state_county():
    """
    Returns a dictionary that maps states to counties
    """
    return _STATE_COUNTY


class Election:
    """
    Election provides data in a format to be used for rendering the UI
    """

    def __init__(self):
        """
        Instance uses mock values
        """
        self.name = mock.get_election_name()
        self.candidates = mock.get_candidates()
        self.api = mock

    def get_election_name(self):
        return self.name

    def get_candidates(self):
        return self.candidates

    def cast_vote(self, voter, candidate):
        self.api.cast_vote(voter, candidate)

    def get_vote_tally_by_candidates(self):
        return self.api.tally_votes_by_candidate()
