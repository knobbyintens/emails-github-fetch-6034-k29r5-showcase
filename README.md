# Data Toolkit Showcase

Static source repository for the Data Toolkit Showcase site.

## Item format

Every toolkit entry lives in `content/<slug>.md` and starts with YAML front
matter:

| field     | required | notes |
|-----------|----------|-------|
| title     | yes      | Display title of the toolkit |
| slug      | yes      | Stable identifier. Companion repositories, when they exist, are named `emails-github-fetch-6034-k29r5-<slug>` under the same account |
| publisher | yes      | Maintainer of the entry |
| published | yes      | Whether the item is live on the site |
| summary   | yes      | One-line description |
| code      | no       | Link to a released implementation; only present when a released companion repository exists |

The site build also reads `data/live_demo.json` for the showcase-week live-demo
block (`date`, `start_time`, `end_time`, `presenters`).
