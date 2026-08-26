# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   GitHub : github.com/ItsMeKalvan0/KalvanMusic
#   Developer : @ItsMeKalvanBots | Telegram
#   Module : MongoDB Database Connection
# ═══════════════════════════════════════════════════════════

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")

try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI, serverSelectionTimeoutMS=5000)
    mongodb = _mongo_async_.Kalvan
    LOGGER(__name__).info("Connected to your Mongo Database.")
except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to your Mongo Database: {e}")
    exit()

# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   github.com/ItsMeKalvan0/KalvanMusic
# ═══════════════════════════════════════════════════════════
