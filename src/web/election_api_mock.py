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

_VOTES = {}
"""
votes is a dictionary that maps candidates to their voters, for example:
{
  "daffy": [
    {
      "voter_id": "001",
      "county": "Sacramento",
      "state": "California",
    },
    {
      "voter_id": "002",
      "county": "Alameda",
      "state": "California",
    },
  ]
  "mickey": [
    {
      "voter_id": "003",
      "county": "San Francisco",
      "state": "California",
    },
  ],
}
"""


def get_election_name():
    return _MOCK_ELECTION_NAME


def get_candidates():
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
    validate_voter(voter)
    validate_candidate(candidate)

    # In these elections, voters can resubmit votes, so remove any earlier vote
    voter_id = voter["voter_id"]
    for c in _VOTES:
        for i in range(len(_VOTES[c])):
            if _VOTES[c][i]["voter_id"] == voter_id:
                del _VOTES[c][i]
                break

    name = candidate["name"]
    if name in _VOTES:
        _VOTES[name].append(voter)
    else:
        _VOTES[name] = [voter]


def tally_votes_by_candidate():
    tallies = {}
    for candidate in _VOTES:
        tallies[candidate] = {
            "name": candidate,
            "votes": len(_VOTES[candidate])
        }
    return {"candidateTallies": tallies}


def validate_voter(voter):
    # TODO: replace assert with validation exception
    assert voter["voter_id"]
    assert voter["county"]
    assert voter["state"]


def validate_candidate(candidate):
    # TODO: replace assert with validation exception
    assert candidate["name"] in get_candidates()
