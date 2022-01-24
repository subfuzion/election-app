import os
from dataclasses import dataclass, field

from votingapp.lib import Election


@dataclass
class Config:
    election: Election = field(init=False)

    def __post_init__(self):
        # Create Vote API client.
        election_server = os.getenv("VOTE", "http://vote")
        print(f"INFO: Using election server at: {election_server}")
        self.election = Election(election_server)
