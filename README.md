
## Projects aspired to be supported

- [InstaPy](https://github.com/socialbotspy/InstaPy)
- [FacebookPy](https://github.com/socialbotspy/FacebookPy)
- [TwitterPy](https://github.com/socialbotspy/TwitterPy)
- [GooglePy](https://github.com/socialbotspy/GooglePy)
- [GPlusPy](https://github.com/socialbotspy/GPlusPy)
- [PinterestPy](https://github.com/socialbotspy/PinterestPy)
- [LinkedinPy](https://github.com/socialbotspy/LinkedinPy)
- [MediumPy](https://github.com/socialbotspy/MediumPy)
- [YoutubePy](https://github.com/socialbotspy/YoutubePy)
- [TumblrPy](https://github.com/socialbotspy/TumblrPy)
- [RedditPy](https://github.com/socialbotspy/RedditPy)
- [QuoraPy](https://github.com/socialbotspy/QuoraPy)
- SnapPy
- [WhatsappPy](https://github.com/socialbotspy/WhatsappPy)
- WeChatPy
- [HangoutPy](https://github.com/socialbotspy/HangoutPy)
- [MessengerPy](https://github.com/socialbotspy/MessengerPy)
- DiscordPy
- SlackPy
- [GithubPy](https://github.com/socialbotspy/GithubPy)
- TelegramPy
- TwitchPy
- TikTokPy
- PeriscopePy
- [GiveawayPy](https://github.com/socialbotspy/GiveawayPy)
- [PTWPy](https://github.com/socialbotspy/PTWPy)

[![MIT license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/socialbotspy/FacebookPy/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/socialbotspy/FacebookPy)

<br />

---
### Building and Packaging

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

### Publishing package to Test Pypi
```bash
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
- Visit https://test.pypi.org/manage/project/socialcommons/releases/ and verify if it has uploaded the latest changes.

### Publishing package to Production Pypi
```bash
python3 -m twine upload dist/*
```
- Visit https://pypi.org/manage/project/socialcommons/releases/ and verify if it has uploaded the latest changes.

### Installation
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
