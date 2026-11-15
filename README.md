# agent-trace-demo

A public demo of [agent-trace](https://github.com/Siddhant-K-code/agent-trace)
on a real pull request.

The library is deliberately small. The point is the pull requests: each one
was written by a coding agent with agent-strace hooks on, and the recorded
session is committed under `.agent-traces/`. The
[reviewability workflow](.github/workflows/reviewability.yml) runs
`agent-strace review` on every pull request. It posts one comment with five
findings (rationale, scope, validation, stewardship, evidence health), sets a
check result, and uploads a metadata-only evidence packet.

Run the tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

`tinytext.char_count(text, include_spaces=True)` counts the characters in
`text`. Set `include_spaces=False` to exclude whitespace characters:

```python
from tinytext import char_count

char_count("a b")  # 3
char_count("a b", include_spaces=False)  # 2
```

## What is committed, and why

Recorded sessions usually stay local; agent-strace writes a `.gitignore` that
ignores them. This repository commits them on purpose so the Action can read
them and so you can replay them:

```bash
uvx agent-strace replay --trace-dir .agent-traces
```

Secret redaction was on when they were recorded. They contain the prompts,
tool calls, and tool output of each session.
