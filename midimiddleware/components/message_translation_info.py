from dataclasses import dataclass, field


@dataclass
class MessageTranslationInfo:
    source_channel: int
    source_type: str
    source_index: int

    target_channel: int
    target_type: str
    target_index: int

    on_color: str = ""
    off_color: str = ""

    is_toggle: bool = False


    def update(self, property_name, value):
        setattr(self, property_name, value)

        if property_name == "target_type" and value in ("note_on", "control_change"):
            if not isinstance(self.target_index, int):
                self.target_index = 60
            else:
                self.target_index = min(max(0, self.target_index), 127)

        if property_name == "target_type" and value == "pitchwheel":
            self.target_index = None

        if property_name == "target_index" and self.target_type in ("note_on", "control_change"):
            self.target_index = min(max(0, self.target_index), 127)

        if property_name == "target_index" and self.target_type == "pitchwheel":
            self.target_index = None

        # TODO: check if CC aren't used in buttons in some controller
        if self.source_type != "note_on" and self.is_toggle:
            self.is_toggle = False
