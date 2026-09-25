---
name: emperor-queue
description: >-
  Pick or record work. Use when the user says find work, next, backlog,
  issues, Linear, what should I do, or hands a repo with no task. Not
  Claude-specific. Writes .emperor/queue.md. Wraps Dowsing, does not replace it.
license: MIT
metadata:
  version: 0.4.0
  part-of: emperor-time
---

# Emperor Queue — pick the next piece of software

1. If the client already named a task, do not hunt. Quote it into the ledger.
2. Else run `scripts/emperor queue next` and quote the tail.
3. Source order (first hit wins): `EMPEROR_QUEUE_SOURCE` → `gh issue list` →
   Linear (`LINEAR_API_KEY` set by client) → `.emperor/queue.md`.
4. One item. Write G0/G1. Out of scope: the rest of the backlog.
5. After G5 + forge, run `scripts/emperor queue next` again unless the client
   said rest.
6. If no tracker exists and the client wants one, propose the thinnest adapter
   (usually `gh`). Build it only with consent. Do not invent Linear when a
   markdown queue works.

Never open a public issue or mutate the tracker without consent.
