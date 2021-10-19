# obsidian-community-repos-downloader

<!-- toc -->
## Contents

  * [What?](#what)
  * [Why?](#why)
  * [Requirements](#requirements)
  * [Setup](#setup)
  * [Run](#run)
  * [Alternatives](#alternatives)
  * [Maintenance notes](#maintenance-notes)
    * [Automated updating the table of contents](#automated-updating-the-table-of-contents)
    * [Almost-automated updating of usage](#almost-automated-updating-of-usage)<!-- endToc -->

[![on-push-do-doco](https://github.com/claremacrae/obsidian-community-repos-downloader/actions/workflows/updateMarkdown.yml/badge.svg)](https://github.com/claremacrae/obsidian-community-repos-downloader/actions/workflows/updateMarkdown.yml)

## What?

Clone every approved Obsidian.md community Plugin and Theme - to read and search the source code and learn from the community.

This is a Python script to download a local copy of all the [published community Obsidian plugins and themes](https://github.com/obsidianmd/obsidian-releases), to be used as a large body of example code.

## Why?

I cannot put it better than the author of the similar project [luckman212/**obsidian-plugin-downloader**](https://github.com/luckman212/obsidian-plugin-downloader):

> As an absolute beginner to TypeScript, and a lover of [Obsidian](https://obsidian.md/) I often want to take a look at how someone has achieved a certain feature, called on an API, etc. A quick way to do that is by searching through the existing codebase of the ever growing library of plugins out there.

## Requirements

- Python 3.6 or above

## Setup

1. Clone or download this repo
2. Run the script `obsidian-community-repos-downloader.py`

## Run

<!-- snippet: usage.txt -->
<a id='snippet-usage.txt'></a>
```txt
usage: obsidian-community-repos-downloader.py [-h] [-o OUTPUT_DIRECTORY]
                                              [-l LIMIT]
                                              [--type [{plugins,themes,all}]]
                                              [--group-by-user]
                                              [--no-group-by-user]

Clone repos included in the obsidian-releases repo, to provide a body of
example plugins and CSS themes.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        The directory where repos will be downloaded. Must
                        already exist. (default: . which means "current
                        working directory")
  -l LIMIT, --limit LIMIT
                        Limit the number of plugin and theme repos that will
                        be downloaded. This is useful when testing the script.
                        0 (zero) means "no limit". Note: the count currently
                        includes any repos already downloaded.(default: 0)
  --type [{plugins,themes,all}]
                        The type of repositories to download: plugins, themes
                        or both. (default: all)
  --group-by-user       Put each repository in a sub-folder named for the
                        GitHub user. For example, the plugin
                        "https://github.com/phibr0/obsidian-tabout" would be
                        placed in "plugins/phibr0/obsidian-tabout"
  --no-group-by-user    Put each repository in the same folder, prefixed by
                        the user name. This is the default behaviour. For
                        example, the plugin
                        "https://github.com/phibr0/obsidian-tabout" would be
                        placed in "plugins/phibr0-obsidian-tabout"
```
<sup><a href='/tests/usage.txt#L1-L32' title='Snippet source file'>snippet source</a> | <a href='#snippet-usage.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Alternatives

- [konhi/**obsidian-repositories-downloader**](https://github.com/konhi/obsidian-repositories-downloader):
    - Requires Node
    - Downloads plugins only
- [luckman212/**obsidian-plugin-downloader**](https://github.com/luckman212/obsidian-plugin-downloader)
    - Written in bash, and a number of other freely-downloadable tools
    - You use a console GUI each run, to search and control which repos to download  
    - Downloads plugins only

---

## Maintenance notes

### Automated updating the table of contents

The table of contents is updated automatically by a GitHub Action, on every push to GitHub.

### Almost-automated updating of usage 

The above usage is updated automatically, on push, whenever `tests/usage.txt` is changed.

To update `tests/usage.txt:

```bash
# 1. Update tests/usage.txt
cd tests
./update_usage.sh
# 2. Commit update usage.txt
# 3. Push to github - a GitHub Action will then update the usage text in this README
```
