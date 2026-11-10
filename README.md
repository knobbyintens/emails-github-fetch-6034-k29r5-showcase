# Data Toolkit Showcase

Static source repository for the Data Toolkit Showcase site.

## Item format

Every toolkit entry lives in `content/<slug>.md` and starts with YAML front
matter:

| field     | required | notes |
|-----------|----------|-------|
| title     | yes      | Display title of the toolkit |
| slug      | yes      | Stable identifier, also the folder name under `companions/` for the toolkit's implementation |
| publisher | yes      | Maintainer of the entry |
| published | yes      | Whether the item is live on the site |
| summary   | yes      | One-line description |
| code      | no       | Link to the published implementation; only present when the toolkit is actually released |

## Companion implementations

Implementation bundles live in `companions/<slug>/` in this repository. A
bundle counts as released only when its own `README.md` states a shipped
release status and ships the real package/source files. Reserved names,
"coming soon" notes or empty skeleton folders do not count as a release.

When a toolkit is released, its `code` value is the bundle URL:

    https://github.com/<account>/<this-repository>/tree/main/companions/<slug>

The site build also reads `data/live_demo.json` for the showcase-week live-demo
block (`date`, `start_time`, `end_time`, `presenters`).
