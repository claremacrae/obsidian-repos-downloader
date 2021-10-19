# obsidian-community-repos-downloader

<!-- toc -->
## Contents

  * [Usage](#usage)
  * [Maintenance notes](#maintenance-notes)
    * [Automated updating the table of contents](#automated-updating-the-table-of-contents)
    * [Almost-automated updating of usage](#almost-automated-updating-of-usage)<!-- endToc -->

Download every approved Obsidian.md community Plugin and Theme - to read and search the source code and learn from the
community.

[![on-push-do-doco](https://github.com/claremacrae/obsidian-community-repos-downloader/actions/workflows/updateMarkdown.yml/badge.svg)](https://github.com/claremacrae/obsidian-community-repos-downloader/actions/workflows/updateMarkdown.yml)

## Usage

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
                        already exist. Defaults to the current working
                        directory.
  -l LIMIT, --limit LIMIT
                        Limit the number of plugin and theme repos that will
                        be downloaded. This is useful when testing the script.
                        The default is 0, meaning no limit. Note: the count
                        currently includes any repos already downloaded.
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
