# agent-trace-demo

A public demo of [agent-trace](https://github.com/Siddhant-K-code/agent-trace)
review on real agent-written pull requests.

The `tinytext` library is deliberately small. The point is the pull requests.
The [reviewability workflow](.github/workflows/reviewability.yml) runs
`agent-strace review` on each one and posts a single comment with five
findings: rationale, scope, validation, stewardship and evidence health. It
also sets a check result and uploads a metadata-only evidence packet.

## The two pull requests

Both stay open on purpose so the comments track the current release.

| Pull request | Written by | Session evidence | What the comment shows |
|---|---|---|---|
| [#1 Add sentence_count](https://github.com/Siddhant-K-code/agent-trace-demo/pull/1) | GitHub Copilot CLI, one prompt, agent-strace hooks on | Recorded session committed under `.agent-traces/` | Session summary and findings read from the trace: the prompt was captured, every written file was named or read, the tests passed in the session |
| [#3 Add char_count](https://github.com/Siddhant-K-code/agent-trace-demo/pull/3) | Copilot cloud agent, from [issue #2](https://github.com/Siddhant-K-code/agent-trace-demo/issues/2) | None recorded | Findings marked inconclusive, not passed. External evidence notes the Copilot cloud agent commit and the missing `Agent-Logs-Url` trailer |

#1 is what review looks like with evidence. #3 is what it looks like
without: missing capture is reported, not guessed.

Neither comment uses CI results. Validation means test runs inside the
recorded session. [How to read the comment](https://github.com/Siddhant-K-code/agent-trace/blob/main/docs/review.md).

## Replay the recorded session

Recorded sessions usually stay local; agent-strace writes a `.gitignore` that
ignores them. #1 commits its session on purpose so the Action can read it and
you can replay it:

```bash
gh pr checkout 1 -R Siddhant-K-code/agent-trace-demo
uvx agent-strace replay b13539e7-7f48-4d
uvx agent-strace verify b13539e7-7f48-4d
```

Secret redaction was on when it was recorded. It contains the prompt, tool
calls and tool output of the session.

One edit was made before committing: the OS username and hostname in the
session's attribution, and the username in a local transcript path, were
replaced with `USER` and `HOST`. That changed one event line, so the
`prev_hash` of the event after it was recomputed. `agent-strace verify` passes
on the committed files, but the hash chain is not the one written at record
time.

## Try it on your repository

1. Copy [`reviewability.yml`](.github/workflows/reviewability.yml) into
   `.github/workflows/`.
2. Record sessions with `agent-strace setup --cli copilot` (or `claude`,
   `codex`, `gemini`, `cursor`).
3. The Action reads sessions from `.agent-traces/`. Commit them, as #1 does,
   or restore them from an artifact before the step.

With no session, the comment looks like #3. Pull requests with no sign of an
agent get no comment. See the
[GitHub Action docs](https://github.com/Siddhant-K-code/agent-trace/blob/main/docs/review.md#github-action).

## tinytext API

- `word_count(text)`: number of whitespace-separated words.

## Run the tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```
