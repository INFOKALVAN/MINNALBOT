# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   GitHub : github.com/ItsMeKalvan0/KalvanMusic
#   Developer : @ItsMeKalvanBots | Telegram 
#   Module : Git Update & Repository Manager
# ═══════════════════════════════════════════════════════════

import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    """
    Best-effort auto-sync with the upstream repo.
    This must NEVER crash the bot on startup — if git isn't available,
    the repo isn't a git repo, or the fetch fails (e.g. no credentials,
    no network access to GitHub, private repo without GIT_TOKEN), we
    just log it and move on so the bot still starts.
    """
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        try:
            repo = Repo()
            LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
            # Ensure origin remote points to correct URL
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
                if list(origin.urls)[0] != UPSTREAM_REPO:
                    origin.set_url(UPSTREAM_REPO)
            else:
                repo.create_remote("origin", UPSTREAM_REPO)
        except GitCommandError as e:
            LOGGER(__name__).warning(f"Invalid Git Command: {e}")
        except InvalidGitRepositoryError:
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)

            origin.fetch()
            repo.create_head(
                config.UPSTREAM_BRANCH,
                origin.refs[config.UPSTREAM_BRANCH],
            )
            repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[config.UPSTREAM_BRANCH]
            )
            repo.heads[config.UPSTREAM_BRANCH].checkout(True)

            nrs = repo.remote("origin")
            nrs.fetch(config.UPSTREAM_BRANCH)
            try:
                nrs.pull(config.UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")

            install_req("pip3 install --no-cache-dir -r requirements.txt")
            LOGGER(__name__).info("Fetched updates from upstream repository.")
    except Exception as e:
        # Covers GitCommandError raised by origin.fetch()/pull() above
        # (e.g. "could not read Username for 'https://github.com'" on
        # hosts like Render/Heroku with no git credentials/TTY), plus
        # any other unexpected git-related failure.
        LOGGER(__name__).warning(
            f"Git auto-sync skipped, continuing startup without it: {e}"
        )

# ═══════════════════════════════════════════════════════════
#        😎  KALVAN MUSIC BOT  😎
#   github.com/ItsMeKalvan0/KalvanMusic
# ═══════════════════════════════════════════════════════════
