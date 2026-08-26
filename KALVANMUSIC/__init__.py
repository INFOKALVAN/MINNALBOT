# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   GitHub : github.com/ItsMeKalvan0/KalvanMusic
#   Developer : @ItsMeKalvanBots | Telegram
#   Module : Package Initialization & App Setup
# ═══════════════════════════════════════════════════════════

from KALVANMUSIC.core.bot import KALVAN
from KALVANMUSIC.core.dir import dirr
from KALVANMUSIC.core.git import git
from KALVANMUSIC.core.userbot import Userbot
from KALVANMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = KALVAN()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   github.com/ItsMeKalvan0/KalvanMusic
# ═══════════════════════════════════════════════════════════
