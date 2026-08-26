import config
from KALVANMUSIC import app
from KALVANMUSIC.utils.colored_buttons import styled_button


def start_panel(_):
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style="success"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style="success"),
            styled_button(text=_["S_B_3"], callback_data="open_help", style="primary"),
        ],
    ]
    return buttons
