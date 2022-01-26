import random

import pglet

from pylet import View


class VoteView(View):
    @property
    def current_voter_id(self):
        return self._current_voter_id

    @property
    def current_state(self):
        return self._current_state

    @property
    def current_county(self):
        return self._current_county

    @property
    def current_candidate(self):
        return self._current_candidate

    def __init__(self, election_name="", candidates=None, state_county=None, on_submit=None):
        super().__init__()
        self.text = "Vote"
        self.icon = "Edit"

        # View context
        self.election_name = election_name
        self.candidates = candidates
        self.state_county = state_county
        self.on_submit = on_submit

        # Current view state
        self._current_voter_id = hex(random.getrandbits(64))[2:-1]
        self._current_state = ""
        self._current_county = ""
        self._current_candidate = ""

        # Controls
        self._election_name_control = pglet.Text(self.election_name, size="xlarge")
        self._candidates_choicegroup_control = self._build_candidate_choicegroup()
        self._vote_button_control = self._build_vote_button()
        self._voter_control = self._build_voter_control()
        self._message_control = pglet.Message(visible=False)

        # View content
        self.content = pglet.Stack(
            gap=20,
            controls=[
                self._election_name_control,
                pglet.Stack(
                    border="1px solid #DDD",
                    border_radius="0",
                    padding=20,
                    bgcolor="#FDFDFD",
                    controls=[
                        self._voter_control,
                    ]
                ),
                pglet.Stack(
                    border="1px solid #DDD",
                    border_radius="0",
                    padding=20,
                    bgcolor="#FDFDFD",
                    controls=[
                        pglet.Text("Who do you want to vote for President?", size="large"),
                        self._candidates_choicegroup_control,
                    ]
                ),
                self._vote_button_control,
                self._message_control,
            ]
        )

    def _build_candidate_choicegroup(self):
        cg = pglet.ChoiceGroup()
        for c in self.candidates:
            cg.options.append(pglet.choicegroup.Option(
                key=c,
                text=self.candidates[c]["name"]
            ))

        me = self

        def on_change(e):
            me._current_candidate = e.data
            me._update_vote_control_disabled()

#        cg.on_change = self._candidate_choicegroup_change
        cg.on_change = on_change
        return cg

    def _candidate_choicegroup_change(self, e):
        self._current_candidate = e.data
        self._update_vote_control_disabled()

    def _build_vote_button(self):
        return pglet.Button(
            "Vote",
            title="Cast your vote!",
            icon="LightningBolt",
            on_click=self._submit_vote,
            primary=True,
            disabled=True,
            width=100,
        )

    def _build_voter_control(self):
        def county_changed(e):
            self._current_county = e.data
            self._update_vote_control_disabled()

        county_dropdown = pglet.Dropdown(
            width=200,
            placeholder="County",
            on_change=county_changed,
        )

        def update_counties(state):
            self._current_state = state
            county_dropdown.options = [pglet.dropdown.Option(c) for c in self.state_county[state]]
            # TODO: all of the following are necessary, should encapsulate into custom control
            e = pglet.Event(county_dropdown.uid, "change", data="")
            county_dropdown.value = ""
            county_dropdown.on_change(e)
            county_dropdown.update()
            self._update_vote_control_disabled()

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

    def _update_vote_control_disabled(self):
        self._vote_button_control.disabled = not (self._current_candidate and self._current_state and self._current_county)
        self.update()

    def _submit_vote(self, _):
        self.clear_message()
        if self.on_submit:
            self.on_submit()

    def message(self, value, kind=""):
        self._message_control.value = value
        self._message_control.type = kind
        self._message_control.visible = True
        self._message_control.update()
        self.freeze_form()

    def clear_message(self):
        self._message_control.value = ""
        self._message_control.type = ""
        self._message_control.visible = False
        self._message_control.update()

    def freeze_form(self):
        # TODO: need a way to unfreeze when reloading page
        # self.content.disabled = True
        # self.content.update()
        pass
