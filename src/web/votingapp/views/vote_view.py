import random

import pglet

from pylet import View


class VoteView(View):
    def __init__(self, election_name="", candidates=None, state_county=None, on_submit=None):
        super().__init__()
        self.text = "Vote"
        self.icon = "Edit"

        self.on_submit = on_submit

        self.election_name = election_name
        self.candidates = candidates
        self.state_county = state_county

        # current voter state
        self.voter_id = hex(random.getrandbits(64))[2:-1]
        self.current_state = ""
        self.current_county = ""

        # current candidate state
        self.current_candidate = ""

        # controls
        self.election_name_control = pglet.Text(self.election_name, size="xlarge")
        self.candidates_control = self._candidate_choicegroup()
        self.vote_control = self._vote_button()
        self.voter_control = self._voter_control()
        self.message_control = pglet.Message(visible=False)

        self.content = pglet.Stack(
            gap=20,
            controls=[
                self.election_name_control,
                pglet.Stack(
                    border="1px solid #DDD",
                    border_radius="0",
                    padding=20,
                    bgcolor="#FDFDFD",
                    controls=[
                        self.voter_control,
                    ]
                ),
                pglet.Stack(
                    border="1px solid #DDD",
                    border_radius="0",
                    padding=20,
                    bgcolor="#FDFDFD",
                    controls=[
                        pglet.Text("Who do you want to vote for President?", size="large"),
                        self.candidates_control,
                    ]
                ),
                self.vote_control,
                self.message_control,
            ]
        )

    def _candidate_choicegroup(self):
        cg = pglet.ChoiceGroup()
        for c in self.candidates:
            cg.options.append(pglet.choicegroup.Option(
                key=c,
                text=self.candidates[c]["name"]
            ))
        cg.on_change = self._candidate_choicegroup_changed
        return cg

    def _candidate_choicegroup_changed(self, e):
        self.current_candidate = e.data
        self.validate()

    def validate(self):
        self.vote_control.disabled = not (self.current_candidate and self.current_state and self.current_county)
        self.update()

    def _vote_button(self):
        return pglet.Button(
            "Vote",
            title="Cast your vote!",
            icon="LightningBolt",
            on_click=self._submit_vote,
            primary=True,
            disabled=True,
            width=100,
        )

    def _voter_control(self):
        def county_changed(e):
            self.current_county = e.data
            self.validate()

        county_dropdown = pglet.Dropdown(
            width=200,
            placeholder="County",
            on_change=county_changed,
        )

        def update_counties(state):
            self.current_state = state
            county_dropdown.options = [pglet.dropdown.Option(c) for c in self.state_county[state]]
            # TODO: all of the following are necessary, so encapsulate into custom control
            e = pglet.Event(county_dropdown.uid, "change", data="")
            county_dropdown.value = ""
            county_dropdown.on_change(e)
            county_dropdown.update()
            self.validate()

        state_dropdown = pglet.Dropdown(
            width=200,
            placeholder="State",
            on_change=lambda e: update_counties(e.data),
            options=[pglet.dropdown.Option(s) for s in self.state_county],
        )
        return pglet.Stack(
            controls=[
                pglet.Text("Where are you voting from?", size="large"),
                pglet.Stack(
                    horizontal=True,
                    controls=[
                        state_dropdown,
                        county_dropdown,
                    ],
                ),
            ]
        )

    def _submit_vote(self, _):
        self.clear_message()
        # TODO: refactor to properties, have adapter query values
        voter = {
            "voter_id": self.voter_id,
            "county": self.current_county,
            "state": self.current_state,
        }
        candidate = {
            "name": self.current_candidate,
            "party": self.current_candidate,
        }
        data = {
            "voter": voter,
            "candidate": candidate,
        }
        if self.on_submit:
            self.on_submit(data)

    def message(self, value, kind=""):
        self.message_control.value = value
        self.message_control.type = kind
        self.message_control.visible = True
        self.message_control.update()
        self.freeze_form()

    def clear_message(self):
        self.message_control.value = ""
        self.message_control.type = ""
        self.message_control.visible = False
        self.message_control.update()

    def freeze_form(self):
        # TODO: need a way to unfreeze when reloading page
        # self.content.disabled = True
        # self.content.update()
        pass
