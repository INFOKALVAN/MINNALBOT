from KALVANMUSIC import app
from KALVANMUSIC.utils.colored_buttons import styled_button


MUSIC_HELP_SECTIONS = [2, 3, 6, 15, 20, 23, 24, 25, 26]
TOTAL_SECTIONS = len(MUSIC_HELP_SECTIONS)

# Alternate button colors: green → blue → green → blue ...
_STYLE_CYCLE = ["success", "primary"]


def generate_help_buttons(_, sections, current_page: int):
    """Return only music-related category buttons with alternating colors."""
    buttons, per_row = [], 3
    for idx, section in enumerate(sections):
        if idx % per_row == 0:
            buttons.append([])
        style = _STYLE_CYCLE[idx % len(_STYLE_CYCLE)]
        buttons[-1].append(
            styled_button(
                text=_[f"H_B_{section}"],
                callback_data=f"help_callback hb{section}_p{current_page}",
                style=style,
            )
        )
    return buttons


def first_page(_):
    buttons = generate_help_buttons(_, MUSIC_HELP_SECTIONS[:5], current_page=1)
    # Menu = blue, Next = green (positive)
    buttons.append(
        [
            styled_button(text="๏ ᴍᴇɴᴜ ๏", callback_data="back_to_main", style="primary"),
            styled_button(text="๏ ɴᴇxᴛ ๏", callback_data="help_next_2", style="success"),
        ]
    )
    return buttons


def second_page(_):
    buttons = generate_help_buttons(_, MUSIC_HELP_SECTIONS[5:], current_page=2)
    # Back = blue, Menu = green
    buttons.append(
        [
            styled_button(text="๏ ʙᴀᴄᴋ ๏", callback_data="help_prev_1", style="primary"),
            styled_button(text="๏ ᴍᴇɴᴜ ๏", callback_data="back_to_main", style="success"),
        ]
    )
    return buttons


def action_sub_menu(_, current_page: int):
    return [
        [
            styled_button(text=_["H_B_S_1"], callback_data="action_prom_1", style="success"),
            styled_button(text=_["H_B_S_2"], callback_data="action_pun_1", style="danger"),
        ],
        [
            styled_button(text=_["BACK_BUTTON"], callback_data=f"help_back_{current_page}", style="primary"),
        ],
    ]


def help_back_markup(_, current_page: int):
    return [
        [
            styled_button(text=_["BACK_BUTTON"], callback_data=f"help_back_{current_page}", style="primary"),
            styled_button(text=_["CLOSE_BUTTON"], callback_data="close", style="danger"),
        ],
    ]


def private_help_panel(_):
    return [
        [
            styled_button(text=_["S_B_3"], url=f"https://t.me/{app.username}?start=help", style="success"),
        ],
    ]
