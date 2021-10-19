# Original code copied with permission:
#   Location: https://github.com/obsidian-community/obsidian-hub/blob/main/.github/scripts/utils.py
#   Author: argentum (she/her)

import json

from urllib.request import urlopen

PLUGIN_MANIFEST = "https://raw.githubusercontent.com/{}/{}/manifest.json"
PLUGINS_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
THEMES_JSON_FILE = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-css-themes.json"


def get_json_from_github(url):
    with urlopen(url) as response:
        json_file = json.loads(response.read())

    return json_file


def get_plugin_manifest(repository, branch):
    manifest = get_json_from_github(PLUGIN_MANIFEST.format(repository, branch))
    return manifest
