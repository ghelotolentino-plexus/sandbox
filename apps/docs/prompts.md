## Copy Board

```text
ghelo.tolentino@plxs.com.au
```

```text
ghelo.ace@gmail.com
```

```text
plexus-ghelo-001@mailinator.com
```

```text
plexusAUD5432!
```

|
```
Incontinentia
```
| b | c |
|---|---|---|

## DSU Update so far

```text
timestamp + add DsuUpdate of summary my notes so far since last DSU meeting
```

## Kickstart Ticket

Paste the ticket link below this prompt:

```text
cd ~/Documents/plexlogic/

I am the assigned engineer for this, look at this ticket including all comments then describe to me what it is and the repositories we need to contribute to

And give me a copy-paste text with this format:  `<jira ticket key>: very short ticket description`
```

## Checkout with common branch name

```text
Give me a git command ticket branch name, that follows the pattern of other ticket branch names on the remote repository
```

## Create PR

```text
Create PRs that matches the style of recent PRs of their respective repositories

Assign as reviewers that have edited the files and have recently approved PRs

Add a Links sections containing the jira links and other PRs
```

## Ticket Message at Slack

```text
Give me a markdown copy paste of this ticket, omit if not applicable:

<shorter jira title> [<ticket number>](<link>) , [PR<pr number>@<repo name>](<link>) , [circleci](<link>)
```

## PR Post at Slack (single repo)

```text
Give me a markdown copy paste of this ticket, omit if not applicable:

Hello Team, [PR<pr number>@<repo name>](<pr link>) for <short jira title> [<jira ticket key>](<jira link>) , [circleci](<link>) :raised_hands:
```

## PR Post at Slack (multiple repo)

```text
Give me a markdown copy paste of this ticket, omit if not applicable:

Hello Team, PRs for <short jira title> [<jira ticket key>](<jira link>) :raised_hands:

1. [PR<pr number>@<repo name>](<pr link>) , [circleci](<link>)
2. (so on)
```

## Staging Deployment Post at Slack

Applicable to `legal-gateway` repo and other major repos

```text
Give me a markdown copy paste of this ticket, omit if not applicable:

Hello Team, I'll be triggering a staging deployment for <repo name> that includes [PR<pr number>@<repo name>](<pr link>) for <short jira title> [<jira ticket key>](<jira link>) , [circleci](<link>) :raised_hands:
```
