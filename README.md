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

## tinytext API

- `word_count(text)`: number of whitespace-separated words.
- `sentence_count(text)`: number of sentences, split on runs of `.`, `!` or
  `?`. Trailing text without a terminator counts as a sentence; blank text
  returns 0.

```python
from tinytext import sentence_count

sentence_count("One. Two! Three?")  # 3
```

Run the tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## What is committed, and why

Recorded sessions usually stay local; agent-strace writes a `.gitignore` that
ignores them. This repository commits them on purpose so the Action can read
them and so you can replay them. From the repository root:

```bash
uvx agent-strace list
uvx agent-strace replay <session-id>
uvx agent-strace verify <session-id>
```

Secret redaction was on when they were recorded. They contain the prompts,
tool calls, and tool output of each session.

One edit was made before committing: the OS username and hostname in each
session's attribution, and the username in a local transcript path, were
replaced with `USER` and `HOST`. That changed one event line, so the
`prev_hash` of the event after it was recomputed. `agent-strace verify` passes
on the committed files, but the hash chain is not the one written at record
time.
