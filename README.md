# XScraper
Bluff AI's XScraper is a scraper built for social networking services (SNS). It analyzes user profiles, posts, followers, and engagement, determining the legitimacy of a user's X (formerly Twitter) account. XScraper also tracks deleted posts, identifies potentially harmful or malicious content, and assesses the overall authenticity of the account's activity.


The following services are currently supported:

* Facebook: user profiles, groups, and communities (aka visitor posts)
* Instagram: user profiles, hashtags, and locations
* Mastodon: user profiles and toots (single or thread)
* Reddit: users, subreddits, and searches (via Pushshift)
* Telegram: channels
* Twitter: users, user profiles, hashtags, searches (live tweets, top tweets, and users), tweets (single or surrounding thread), list posts, communities, and trends
* VKontakte: user profiles
* Weibo (Sina Weibo): user profiles

## Requirements
XScraper requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install XScraper.

Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.

## Installation
    pip3 install XScraper

If you want to use the development version:

    pip3 install git+ https://github.com/BluffAiAgent/XAnalyzier.git

## Usage
### CLI
The generic syntax of XScraper's CLI is:

    XScraper [GLOBAL-OPTIONS] SCRAPER-NAME [SCRAPER-OPTIONS] [SCRAPER-ARGUMENTS...]

`XScraper --help` and `XScraper SCRAPER-NAME --help` provide details on the options and arguments. `XScraper --help` also lists all available scrapers.

The default output of the CLI is the URL of each result.

Some noteworthy global options are:

* `--jsonl` to get output as JSONL. This includes all information extracted by XScraper (e.g. message content, datetime, images; details vary by scraper).
* `--max-results NUMBER` to only return the first `NUMBER` results.
* `--with-entity` to get an item on the entity being scraped, e.g. the user or channel. This is not supported on all scrapers. (You can use this together with `--max-results 0` to only fetch the entity info.)

#### Examples
Collect all tweets by Jason Scott (@textfiles):

    XScraper twitter-user textfiles

It's usually useful to redirect the output to a file for further processing, e.g. in bash using the filename `twitter-@textfiles`:

```bash
XScraper twitter-user textfiles >twitter-@textfiles
```

To get the latest 100 tweets with the hashtag #archiveteam:

    XScraper --max-results 100 twitter-hashtag archiveteam

### Library
It is also possible to use XScraper as a library in Python, but this is currently undocumented.

## Issue reporting
If you discover an issue with XScraper, please report it at <https://github.com/BluffAiAgent/XScraper/issues>. If you use the CLI, please run XScraper with `-vv` and include the log output in the issue. If you use XScraper as a module, please enable debug-level logging using `import logging; logging.basicConfig(level = logging.DEBUG)` (before using XScraper at all) and include the log output in the issue.

### Dump files
In some cases, debugging may require more information than is available in the log. The CLI has a `--dump-locals` option that enables dumping all local variables within XScraper based on important log messages (rather than, by default, only on crashes). Note that the dump files may contain sensitive information in some cases and could potentially be used to identify you (e.g. if the service includes your IP address in its response). If you prefer to arrange a file transfer privately, just mention that in the issue.

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
