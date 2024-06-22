gitea-webhook-commander
=======================

Runs a given command in the given CWD based on the route called by Gitea

## Commands

You configure things in the `commands.json` file which looks
something like this:

```json
{
	"homepage" : {
		"dir": "/home/builder/src/homepage",
		"pre-command": ["git", "pull"],
		"command": ["hugo", "-d", "/home/builder/dump/"]
	},
	"crxn" : {
		"dir": "/home/builder/src/crxn",
		"pre-command": ["git", "pull"],
		"command": ["python3", "-m", "mkdocs", "build", "-d", "/home/builder/dump/projects/crxn"]
	}
}
```


## Authentication

_Optionally_ you can set the environment variable `GITEA_WEBHOOK_AUTH` to
a string containing the password that is expected to be present in the
HTTP request that Gitea will make to us. It implies therefore that,
when this environment variable is set, that there should be an HTTP
header named `Authorization` present.