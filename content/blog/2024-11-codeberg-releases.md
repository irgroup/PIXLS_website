---
id: "blog-post-4"
date: "2024-11"
display_date: "November 2024"
tag: "Open Infrastructure"
tag_color: "berry"
card_style: "tool-card"
title: "Codeberg Releases: pixls-preprints Harvester & livivo-converter Schema Tool"
excerpt: "To support open scientific infrastructure and reproducible data pipelines, ZB MED and TH Köln have released our acquisition and transformation repositories on Codeberg."
links:
  - label: "Codeberg →"
    href: "https://codeberg.org/pixls/pixls-preprints"
---

The `pixls-preprints` toolkit powers the daily harvesting of 30+ preprint archives, utilizing asynchronous REST APIs and leaky-bucket algorithms to respect rate limits while maintaining high ingestion throughput.

The companion tool, `livivo-converter`, handles schema transformation, mapping heterogeneous metadata from preprint platforms into normalized records ready for ingestion into ZB MED's [LIVIVO search portal](https://www.livivo.de/).
