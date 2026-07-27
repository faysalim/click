#!/usr/bin/env python3
"""
Add a new tracking link to links.json and print the shareable URL.

Usage:
    python gen_link.py --url https://example.com/page --contact jane --channel whatsapp \
        --pages-url https://yourusername.github.io/your-repo

Then commit + push links.json to GitHub.
"""
import argparse
import json
import random
import string
import os

LINKS_FILE = os.path.join(os.path.dirname(__file__), "links.json")


def generate_code(existing, length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = "".join(random.choices(chars, k=length))
        if code not in existing:
            return code


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True, help="Destination URL")
    p.add_argument("--contact", default="", help="Contact name/id")
    p.add_argument("--channel", default="", help="e.g. whatsapp, email, linkedin")
    p.add_argument(
        "--pages-url",
        default="https://YOURUSERNAME.github.io/YOURREPO",
        help="Your GitHub Pages base URL (no trailing slash)",
    )
    args = p.parse_args()

    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE) as f:
            links = json.load(f)
    else:
        links = {}

    code = generate_code(links)
    links[code] = {"url": args.url, "contact": args.contact, "channel": args.channel}

    with open(LINKS_FILE, "w") as f:
        json.dump(links, f, indent=2)

    tracking_url = f"{args.pages_url}/r.html?id={code}"
    print(f"Added code: {code}")
    print(f"Tracking URL: {tracking_url}")
    print("Now commit + push links.json to publish it.")


if __name__ == "__main__":
    main()
