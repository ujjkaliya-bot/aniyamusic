# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from os import path

from yt_dlp import YoutubeDL

from ANIYAXMUSIC.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        if "soundcloud" in link:
            return True
        else:
            return False

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz


    async def search_download(self, query: str):
        """Find and download one matching public SoundCloud audio track."""
        import os

        if not query or not query.strip():
            raise ValueError("Track title is empty")

        os.makedirs("downloads", exist_ok=True)
        options = {
            **self.opts,
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
        }
        with YoutubeDL(options) as downloader:
            info = downloader.extract_info(
                f"scsearch1:{query.strip()}",
                download=True,
            )

        entries = info.get("entries") if isinstance(info, dict) else None
        track = next((item for item in (entries or []) if item), info)
        if not isinstance(track, dict):
            raise RuntimeError("No matching SoundCloud track was found")

        requested = track.get("requested_downloads") or []
        filepath = requested[0].get("filepath") if requested else None
        if not filepath:
            filepath = track.get("_filename") or downloader.prepare_filename(track)
        if not filepath or not os.path.isfile(filepath):
            raise FileNotFoundError("SoundCloud audio file was not created")

        duration = int(track.get("duration") or 0)
        details = {
            "title": track.get("title") or query.strip(),
            "duration_sec": duration,
            "duration_min": seconds_to_min(duration) if duration else "00:00",
            "uploader": track.get("uploader") or "SoundCloud",
            "filepath": filepath,
        }
        return details, filepath
