# CleanMail — A CLI Gmail Email Cleaner

`cleanmail` is a command-line tool to help you clean up your Gmail inbox quickly and safely.  
It uses the official Gmail API and OAuth2 authentication to support actions like:
- Trashing or permanently deleting emails
- Filtering by sender
- Filtering by time (before/after dates)
- Note: --after tag deletes the mail on the given date too.

---

## Features

- **Filter by sender**
- **Filter by date range**
- **Safe by default** (moves to Trash unless `--permanent` is used)
- **OAuth2-based authentication**
- **Multi-account support** (tokens are stored per email for ease of access)

---

## Installation

Clone the repo and install the tool locally and add your `credentials.json` file to the same directory.(OAuth Credentials)


```bash
git clone https://github.com/Suhasjoshuaj/CLI-Email-Cleaner.git
cd cleanmail
pip install -e .
```

## Working 

- You login through a browser via OAuth
- Token gets saved in a file named token_something@gmail.com.json
- All API actions are done through gmail's official endpoints. 

## CLI 

```CLI
cleanmail --sender spammer@ads.com spammery@ads --after 2024/01/01 --verbose --permanent
```