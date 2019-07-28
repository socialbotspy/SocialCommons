
## Projects aspired to be supported

- [FacebookPy](https://github.com/socialbotspy/FacebookPy)
- [TwitterPy](https://github.com/socialbotspy/TwitterPy)
- Google+
- PinterestPy
- [LinkedinPy](https://github.com/socialbotspy/LinkedinPy)
- YoutubePy
- TumblrPy
- RedditPy
- QuoraPy
- SnapPy
- WhatsappPy
- WeChatPy
- DiscordPy
- SlackPy
- [GithubPy](https://github.com/socialbotspy/GithubPy)
- TwitchPy
- TikTokPy
- PeriscopePy
- [InstaPy](https://github.com/timgrossmann/InstaPy/tree/master/instapy)

[![MIT license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/socialbotspy/FacebookPy/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/socialbotspy/FacebookPy)

<br />

---
### Setup

```bash
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine
rm -rf SocialCommons.egg-info/ build/ dist/
```

- Modify version no in `setup.py`

```bash
python3 setup.py sdist bdist_wheel
```

- Verify `SocialCommons.egg-info`, `build` and `dist` are recreated

### Uploading to Test Pypi
```bash
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
- Visit `https://test.pypi.org/manage/project/socialcommons/releases/` and verify it has uploaded the latest changes.

### Uploading to Production Pypi
```bash
python3 -m twine upload dist/*
```
- Visit `https://pypi.org/manage/project/socialcommons/releases/` and verify it has uploaded the latest changes.

### Install
```bash
pip install -U SocialCommons
```

### Contributors

This project exists thanks to all the people who contribute.

### Backers

Thank you to all our backers! 🙏

### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.


## Help build socialbotspy
Check out this short guide on [how to start contributing!](https://github.com/InstaPy/instapy-docs/blob/master/CONTRIBUTORS.md).
