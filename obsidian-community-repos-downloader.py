#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess

# TODO Control which of these:
#       https://github.com/username/projectname.git
#  vs
#           git@github.com:username/projectname.git

from utils import (
    get_json_from_github
)
from utils import PLUGINS_JSON_FILE, THEMES_JSON_FILE
from dirutils import use_directory, readable_dir


def clone_repo(plugin):
    repo = plugin.get("repo")
    branch = plugin.get("branch", "master")
    user, repo_name = repo.split("/")
    with use_directory(user, create_if_missing=True):
        if not os.path.isdir(repo_name):
            print(f"cloning {repo}")
            command = f"git clone https://github.com/{repo}.git"
            subprocess.run(command, shell=True, check=True)
        else:
            print(f"{repo} already exists")


def clone_repos(repo_list):
    for plugin in repo_list:
        clone_repo(plugin)


def process_released_plugins(overwrite=False):
    with use_directory("plugins", create_if_missing=True):
        plugin_list = get_json_from_github(PLUGINS_JSON_FILE)
        clone_repos(plugin_list)


def process_released_themes(overwrite=False):
    print("-----\nProcessing themes....\n")
    with use_directory("css-themes", create_if_missing=True):
        theme_list = get_json_from_github(THEMES_JSON_FILE)
        clone_repos(theme_list)


class DownloaderOptions:
    def __init__(self):
        self.parser = make_arg_parser()
        self.args = None

    def parse_args(self, argv):
        self.args = self.parser.parse_args(argv)

    def root_output_directory(self):
        return self.args.output_directory


class Downloader:
    def __init__(self, options):
        self.options = options

    def download(self):
        with use_directory(self.options.root_output_directory(), create_if_missing=False):
            print(f"Working directory: {os.getcwd()}")
            process_released_plugins()
            process_released_themes()


def make_arg_parser():
    parser = argparse.ArgumentParser(
        description="Clone repos included in the obsidian-releases repo, "
                    "to provide a body of example plugins and CSS themes."
    )
    parser.add_argument('-o', '--output_directory', default='.', type=readable_dir,
                        help='The directory where repos will be downloaded. Must already exist. '
                             'Defaults to the current working directory.'
                        )
    return parser


def main(argv=sys.argv[1:]):
    options = DownloaderOptions()
    options.parse_args(argv)

    downloader = Downloader(options)
    downloader.download()


if __name__ == "__main__":
    main()
