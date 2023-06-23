
# Mail_to_Github_account
An OSINT tool that permit to obtain the username of an Github account by simply specifying a mail adress, even is the mail is set in private.

Account is obtained by committing with the email of the person you want to obtain the account.
Beware of OPSEC Tho

## Remediation

Under your github settings just go to 'email' and check the to boxes "make my email private" and "Block command line pushes that expose my email"

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your machine.
- The 'requests' library installed. You can install it by running `pip install requests`.

## Getting Started

1. Clone or download the project files to your local machine.

2. Obtain a GitHub API Token:
   - Visit the [GitHub Developer Settings](https://github.com/settings/tokens) page.
   - Generate a new personal access token with the required scopes (e.g., `repo`).
   - Copy the generated token.
3. run the script
