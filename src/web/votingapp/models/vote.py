from pylet import Model

from votingapp import Config


class Vote(Model):
    def __init__(self, config: Config):
        super().__init__()
        self.election = config.election

    @property
    def election_name(self) -> str:
        return self.election.get_election_name()

    @property
    def candidates(self) -> dict:
        return self.election.get_candidates()

    @property
    def state_county(self) -> dict:
        return self.election.get_state_county()

    def post_vote(self, data):
        print(f"post vote: {data}")
        r = self.election.cast_vote(data["voter"], data["candidate"])
        print(f"vote api (post vote): status code: {r.status_code}")
        return None if r.status_code == 200 else r.reason

    def get_results(self):
        print(f"get results")
        r = self.election.get_vote_tally_by_candidates()
        print(f"vote api (get results): status code: {r.status_code}")
        if r.status_code != 200:
            return False, r.reason
        else:
            winner, results = self._process_results(r.json()["results"])
            return True, (winner, results)

    def _process_results(self, tallies):
        """
        For candidateTallies, return a winner and the results.
        """
        # Expect this shape:
        # {
        #     "candidateTallies": {
        #         "panther": {
        #             "name": "panther",
        #             "votes": 4
        #         },
        #         "tiger": {
        #             "name": "tiger",
        #             "votes": 5
        #         }
        #     }
        # }
        tally = {}

        # Flatten results of tallies for candidates.
        for key in tallies["candidateTallies"]:
            tally[key] = tallies["candidateTallies"][key]["votes"]

        if len(tally) == 0:
            return "No winner yet", {}

        # Sort results in order of votes, desc.
        ordered_tally = {
            k: v
            for k, v in sorted(
                tally.items(), key=lambda item: item[1], reverse=True)
        }

        # Get highest voted.
        winner = max(tally, key=tally.get)
        winner_name = self.candidates[winner]["name"]
        return winner_name, ordered_tally
