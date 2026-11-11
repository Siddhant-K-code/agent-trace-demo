import re

_SENTENCE_RE = re.compile(r"[^.!?]*[^\s.!?][^.!?]*(?:[.!?]+|$)")


def sentence_count(text):
    """Count sentences in text, split on runs of '.', '!' or '?'."""
    return len(_SENTENCE_RE.findall(text))
