# Contributing

Thank you. Contributions are welcome, via
[Issues](https://github.com/claremacrae/obsidian-community-repos-downloader/issues) or
[Pull-Requests](https://github.com/claremacrae/obsidian-community-repos-downloader/pulls).

Please check if someone else has made the same suggestion first. Thank you.

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

