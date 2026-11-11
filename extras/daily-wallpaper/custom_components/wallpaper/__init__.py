"""Serves /config/www/wallpaper at /wallpaper/<file> with Cache-Control: no-cache.

/local is cached by browsers for 31 days, so a daily-replaced background image goes stale.
no-cache makes browsers revalidate (cheap 304 via ETag/Last-Modified) on every load.
"""
from pathlib import Path

from aiohttp import web

from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "wallpaper"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    root = await hass.async_add_executor_job(Path(hass.config.path("www", "wallpaper")).resolve)
    hass.http.register_view(WallpaperView(hass, root))
    return True


def _resolve(root: Path, filename: str) -> Path | None:
    path = (root / filename).resolve()
    return path if path.parent == root and path.is_file() else None


class WallpaperView(HomeAssistantView):
    url = "/wallpaper/{filename}"
    name = "wallpaper"
    requires_auth = False

    def __init__(self, hass: HomeAssistant, root: Path) -> None:
        self._hass = hass
        self._root = root

    async def get(self, request: web.Request, filename: str) -> web.StreamResponse:
        path = await self._hass.async_add_executor_job(_resolve, self._root, filename)
        if path is None:
            raise web.HTTPNotFound()
        return web.FileResponse(path, headers={"Cache-Control": "no-cache"})
