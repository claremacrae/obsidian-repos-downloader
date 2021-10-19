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


class DownloaderOptions:
    def __init__(self):
        self.parser = self.make_parser()
        self.args = None

    def make_parser(self):
        parser = argparse.ArgumentParser(
            description="Clone repos included in the obsidian-releases repo, "
                        "to provide a body of example plugins and CSS themes."
        )
        parser.add_argument('-o', '--output_directory', default='.', type=readable_dir,
                            help='The directory where repos will be downloaded. Must already exist. '
                                 'Defaults to the current working directory.'
                            )

        parser.add_argument('-l', '--limit', type=int, default=0,
                            help='Limit the number of plugin and theme repos that will be downloaded. '
                                 'This is useful when testing the script. '
                                 'The default is 0, meaning no limit. '
                                 'Note: the count currently includes any repos already downloaded.')

        parser.add_argument('--type',
                            default='all',
                            const='all',
                            nargs='?',
                            choices=['plugins', 'themes', 'all'],
                            help='The type of repositories to download: plugins, themes or both. '
                                 '(default: %(default)s)')

        parser.add_argument('--group-by-user', dest='group_by_user', action='store_true',
                            help='Put each repository in a sub-folder named for the GitHub user. '
                                 'For example, the plugin "https://github.com/phibr0/obsidian-tabout" would be placed '
                                 'in "plugins/phibr0/obsidian-tabout"')
        parser.add_argument('--no-group-by-user', dest='group_by_user', action='store_false',
                            help='Put each repository in the same folder, prefixed by the user name. '
                                 'This is the default behaviour. '
                                 'For example, the plugin "https://github.com/phibr0/obsidian-tabout" would be placed '
                                 'in "plugins/phibr0-obsidian-tabout"')
        parser.set_defaults(group_by_user=False)

        return parser

    def parse_args(self, argv):
        self.args = self.parser.parse_args(argv)

    def limit(self):
        return self.args.limit

    def need_to_download_type(self, type):
        return self.args.type in ["all", type]

    def root_output_directory(self):
        return self.args.output_directory

    def repo_output_directory(self, user):
        if self.args.group_by_user:
            return user
        else:
            return '.'

    def repo_output_name(self, user, repo):
        if self.args.group_by_user:
            return repo
        else:
            # Prefix with username, in case there are any duplicated repo names
            return f"{user}-{repo}"

class Downloader:
    def __init__(self, options):
        self.options = options

    def download(self):
        with use_directory(self.options.root_output_directory(), create_if_missing=False):
            print(f"Working directory: {os.getcwd()}")
            self.process_released_plugins(PLUGINS_JSON_FILE)
            self.process_released_themes(THEMES_JSON_FILE)

    def process_released_plugins(self, json_file):
        self.process_released_repos("plugins", json_file)

    def process_released_themes(self, json_file):
        self.process_released_repos("themes", json_file)

    def process_released_repos(self, type, json_file):
        if not self.options.need_to_download_type(type):
            return

        print(f"-----\nProcessing {type}....\n")
        with use_directory(type, create_if_missing=True):
            plugin_list = get_json_from_github(json_file)
            self.clone_repos(plugin_list)

    def clone_repos(self, plugin_list):
        count = 0
        limit = self.options.limit()
        for plugin in plugin_list:
            self.clone_repo(plugin)
            count += 1
            if limit > 0 and count >= limit:
                print("Maximum number of new repos exceeded. Stopping.")
                return

    def clone_repo(self, plugin):
        repo = plugin.get("repo")
        branch = plugin.get("branch", "master")
        user, repo_name = repo.split("/")
        directory_for_repo = self.options.repo_output_directory(user)
        with use_directory(directory_for_repo, create_if_missing=True):
            repo_output_name = self.options.repo_output_name(user, repo_name)
            if not os.path.isdir(repo_output_name):
                print(f"cloning {repo}")
                command = self.get_download_command(repo, user, repo_name, repo_output_name)
                subprocess.run(command, shell=True, check=True)
            else:
                print(f"{repo_output_name} already exists")

    def get_download_command(self, repo, user, repo_name, repo_output_name):
        command = f"git clone https://github.com/{repo}.git {repo_output_name}"
        return command


def main(argv=sys.argv[1:]):
    options = DownloaderOptions()
    options.parse_args(argv)

    downloader = Downloader(options)
    downloader.download()


if __name__ == "__main__":
    main()
