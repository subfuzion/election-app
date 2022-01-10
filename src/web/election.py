import requests

_STATE_COUNTY = {"California": ["Fresno", "Alameda", "Sacramento"], "Arizona": ["La Paz", "Maricopa", "Mohave"], }

_MOCK_ELECTION_NAME = "Daffy Duck vs Mickey Mouse"

_MOCK_CANDIDATES = {
    "daffy": {
        "id": "daffy",
        "name": "Daffy Duck",
        "party": "blue",
        "color": "#1aaaf8"
    },
    "mickey": {
        "id": "mickey",
        "name": "Mickey Mouse",
        "party": "green",
        "color": "#00cbca"
    }
}


class Election:
    """
    Election is an election service api client and renders data (as needed)
    for the UI.
    """

    def __init__(self, api):
        self.api = api

    def get_election_name(self):
        # TODO: get from API
        return _MOCK_ELECTION_NAME

    def get_candidates(self):
        # TODO: get from API
        return _MOCK_CANDIDATES

    def get_state_county(self):
        """
        Returns a dictionary that maps states to counties
        """
        # TODO: get from API
        return _STATE_COUNTY

    def cast_vote(self, voter, candidate):
        return requests.post(self.api + "/vote", json={
            "voter": voter,
            "candidate": candidate
        })

    def get_vote_tally_by_candidates(self):
        return requests.get(self.api + "/tally/candidates")
