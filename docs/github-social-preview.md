# GitHub social preview

GitHub shows a social preview (Open Graph) image when the repo is shared. That
image is **not** set by merging files. It is uploaded in the repo UI.

## Click path (maintainer)

1. Open https://github.com/arbi-elezi/emperor-time/settings
2. Scroll to **Social preview** under General
3. Upload `assets/shovel.png` from this repo
4. Ideal size is **1280×640**. The checked-in shovel is **512×448**, so crop or
   resize if GitHub complains or the preview looks soft
5. Save and spot-check a share card (Slack, X, LinkedIn, or similar)

## What this PR does not claim

We did not set the OG image via API. GitHub's REST/GraphQL upload for social
preview is limited / settings-only for normal tokens. Leaving this note so the
click path stays honest.

Sponsors button and shovel already live in the README first screen.
