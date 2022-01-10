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


def get_state_county():
    # TODO: get from API
    return _STATE_COUNTY


def get_election_name():
    # TODO: get from API
    return _MOCK_ELECTION_NAME


def get_candidates():
    # TODO: get from API
    return _MOCK_CANDIDATES


def cast_vote(voter, candidate):
    """
    voter is a dictionary that contains keys for
      - voter_id
      - county
      - state
    candidate is a dictionary that contains keys for
      - name
      - party
    """
    pass


def tally_votes_by_candidate():
    pass
