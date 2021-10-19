# obsidian-repos-downloader

<!-- toc -->
## Contents

  * [What?](#what)
  * [Why?](#why)
  * [Setup](#setup)
    * [Requirements](#requirements)
    * [Download](#download)
  * [Run](#run)
    * [Getting Started](#getting-started)
    * [Usage - all the arguments](#usage---all-the-arguments)
  * [Output Directories](#output-directories)
    * [Flatter Structure](#flatter-structure)
    * [Grouped by User name](#grouped-by-user-name)
  * [Likely Questions](#likely-questions)
    * [How do I update repos I have already downloaded?](#how-do-i-update-repos-i-have-already-downloaded)
    * [What order are plugins and themes downloaded in?](#what-order-are-plugins-and-themes-downloaded-in)
  * [Alternatives](#alternatives)<!-- endToc -->

[![on-push-do-doco](https://github.com/claremacrae/obsidian-repos-downloader/actions/workflows/updateMarkdown.yml/badge.svg)](https://github.com/claremacrae/obsidian-repos-downloader/actions/workflows/updateMarkdown.yml)

## What?

Clone every approved Obsidian.md community Plugin and Theme - to read and search the source code and learn from the community.

This is a Python3 script to download a local copy of all the [published community Obsidian plugins and themes](https://github.com/obsidianmd/obsidian-releases), to be used as a large body of example code.

It inspects these files, and then downloads (clones) all the repos listed in them:

- [community-css-themes.json](https://github.com/obsidianmd/obsidian-releases/blob/master/community-css-themes.json)
- [community-plugins.json](https://github.com/obsidianmd/obsidian-releases/blob/master/community-plugins.json)


## Why?

I cannot put it better than the author of the similar project [luckman212/**obsidian-plugin-downloader**](https://github.com/luckman212/obsidian-plugin-downloader):

> As an absolute beginner to TypeScript, and a lover of [Obsidian](https://obsidian.md/) I often want to take a look at how someone has achieved a certain feature, called on an API, etc. A quick way to do that is by searching through the existing codebase of the ever growing library of plugins out there.

## Setup

### Requirements

- Python 3.6 or above

### Download

1. Download the [Latest Release](https://github.com/claremacrae/obsidian-repos-downloader/releases). 
   - Choose one of:
       - "Source code (zip)"
       - "Source code (tar.gz)" 
   - If you can't see them, click to expand the "Assets"
2. Expand the downloaded Source Code file
   - This will give you a folder name such as "obsidian-repos-downloader-0.1.0"

## Run

### Getting Started

The script to run is `obsidian-repos-downloader.py`

Depending on your platform, here are some example ways you might need to run it:

```bash
obsidian-repos-downloader.py
./obsidian-repos-downloader.py
python3 obsidian-repos-downloader.py
```

### Usage - all the arguments

Running `obsidian-repos-downloader.py --help` gives this output:


<!-- snippet: usage.txt -->
```txt
usage: obsidian-repos-downloader.py [-h] [-o OUTPUT_DIRECTORY] [-l LIMIT] [-n]
                                    [-t [{plugins,themes,all}]]
                                    [--group-by-user] [--no-group-by-user]

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
  -n, --dry-run         Print out the commands to be executed, but do no run
                        them. This is useful for testing. Note: it does not
                        print the directory-creation commands, just the git
                        ones
  -t [{plugins,themes,all}], --type [{plugins,themes,all}]
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
<!-- endSnippet -->

## Output Directories

The script always creates a `plugins/` and `themes/` directories for its output.

There are the command-line arguments to determine the structure inside those directories.

### Flatter Structure

By default, or when the argument `--no-group-by-user` is supplied, all the downloaded repos are placed side-by-side.
They are prefixed with the username of the developer who wrote them.

For example, running this command (limiting the output to only 4 repositories, for brevity)....

```bash
obsidian-repos-downloader.py  --limit 4
```

... gives this directory structure: 

<!-- snippet: tree-output-ungrouped.txt -->
```txt
plugins
├── agathauy-wikilinks-to-mdlinks-obsidian
├── aidenlx-alx-folder-note
├── aidenlx-better-fn
└── aidenlx-cm-chs-patch
themes
├── ArtexJay-Obsidian-CyberGlow
├── auroral-ui-aurora-obsidian-md
├── bcdavasconcelos-Obsidian-Ayu
└── bcdavasconcelos-Obsidian-Ayu_Mirage

8 directories
```
<!-- endSnippet -->



### Grouped by User name

When the argument `--group-by-user` is supplied, all the downloaded repos are placed in sub-directories
named with the username of the developer who wrote them.

For example, running this command (limiting the output to only 4 repositories, for brevity)....

```bash
obsidian-repos-downloader.py  --limit 4 --group-by-user
```

... gives this directory structure: 

<!-- snippet: tree-output-grouped.txt -->
```txt
plugins
├── agathauy
│   └── wikilinks-to-mdlinks-obsidian
└── aidenlx
    ├── alx-folder-note
    ├── better-fn
    └── cm-chs-patch
themes
├── ArtexJay
│   └── Obsidian-CyberGlow
├── auroral-ui
│   └── aurora-obsidian-md
└── bcdavasconcelos
    ├── Obsidian-Ayu
    └── Obsidian-Ayu_Mirage

13 directories
```
<!-- endSnippet -->

## Likely Questions

### How do I update repos I have already downloaded?

In this early release, there is no mechanism to update any repos that have already been downloaded.

You can do this via `git pull`, although you would need to script the running of that in every plugin and theme directory.

**Workaround**: delete the existing downloads, and run the script again.

### What order are plugins and themes downloaded in?

They are downloaded in case-insensitive alphabetical order of the repository's GitHub URL, so effectively in order
of user name and then repo name.

## Alternatives

There is a growing number of alternative mechanisms for downloading Obsidian repos:

- [konhi/**obsidian-repositories-downloader**](https://github.com/konhi/obsidian-repositories-downloader):
    - Requires Node
    - Downloads plugins only
- [luckman212/**obsidian-plugin-downloader**](https://github.com/luckman212/obsidian-plugin-downloader)
    - Written in bash, and a number of other freely-downloadable tools
    - You use a console GUI each run, to search and control which repos to download  
    - Downloads plugins only
