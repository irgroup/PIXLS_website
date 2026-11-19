---
id: "blog-post-2"
date: "2026-01"
display_date: "January 2026"
tag: "Software Release"
tag_color: "berry"
card_style: "tool-card"
title: "Introducing REANIMATOR-VLM: Rebuilding Document Extraction with Vision-Language Models"
excerpt: "We announced the release of `reanimator-vlm` (v0.1.2) on PyPI. This clean rebuild transitions the REANIMATOR extraction core from traditional OCR heuristics to state-of-the-art Vision-Language Models (dots.mocr) and Docling."
links:
  - label: "PyPI Package →"
    href: "https://pypi.org/project/reanimator-vlm/"
---

Extracting information from scientific PDFs has historically been hindered by brittle layout parsers and closed LLM dependencies. `reanimator-vlm` solves this by providing:

- **VLM Layout & Table Recognition:** High-accuracy parsing of complex biomedical tables, sub-tables, formulas, and visual elements.
- **In-Text Contextualization:** Automatic linking of table and figure mentions in the narrative text to their corresponding visual containers.
- **Synthetic Relevance Engine:** Domain-independent relevance assessment based on the UMBRELA framework for evaluating RAG and retrieval benchmarks.

Install today via `pip install reanimator-vlm` or inspect the open-source code on GitHub.
