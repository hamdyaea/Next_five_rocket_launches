#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Read upcoming rocket launches from a configurable JSON API."""
from __future__ import annotations
import argparse
import json
from urllib.request import Request, urlopen

DEFAULT_URL = "https://astrometry.ch/rockets.json"

def fetch_launches(url: str = DEFAULT_URL, timeout: int = 10) -> dict:
    if not url.startswith("https://"):
        raise ValueError("Only HTTPS endpoints are supported")
    request = Request(url, headers={"User-Agent": "RocketLaunch/2.0"})
    with urlopen(request, timeout=timeout) as response:
        payload = response.read(2_000_001)
    if len(payload) > 2_000_000:
        raise ValueError("Response exceeds 2 MB")
    data = json.loads(payload)
    if not isinstance(data, dict) or not isinstance(data.get("results"), list):
        raise ValueError("Expected API JSON object containing results list")
    return data

def summarize(item: dict) -> dict[str, str]:
    def nested(*keys):
        value = item
        for key in keys:
            if not isinstance(value, dict):
                return ""
            value = value.get(key)
        return str(value) if value is not None else ""
    return {
        "Rocket": nested("rocket", "configuration", "full_name"),
        "Launch time": nested("net"),
        "Provider": nested("launch_service_provider", "name"),
        "Mission": nested("mission", "name"),
        "Mission type": nested("mission", "type"),
        "Orbit": nested("mission", "orbit", "name"),
        "Description": nested("mission", "description"),
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    try:
        data = fetch_launches(args.url)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    for index, item in enumerate(data["results"][:args.limit], start=1):
        if not isinstance(item, dict):
            continue
        print(f"\nLaunch {index}")
        for label, value in summarize(item).items():
            print(f"{label}: {value}")
    print(f"API total: {data.get('count', 'unknown')}")

if __name__ == "__main__":
    main()
