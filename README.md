# PIXLS: Preprint Information eXtraction for Life Sciences

Official website repository for the **PIXLS** research project (2023 – 2027), funded by the **Deutsche Forschungsgemeinschaft (DFG)** under grant number **492813820** (*Scientific Library Services and Information Systems* / LIS program).

**Project Lead Institutions:**
- **TH Köln** – Faculty of Information Science and Communication Studies, Cologne Information Retrieval Group (CIR)
  - PI: Prof. Dr. Philipp Schaer
  - Research Associate: Fabian Haak, M.Sc.
  - Website: [`https://ir.web.th-koeln.de/`](https://ir.web.th-koeln.de/)
- **ZB MED – Information Centre for Life Sciences**
  - PI: Prof. Dr. Konrad U. Förstner
  - Research Associate: Benjamin Wolff, M.Sc.
  - Portal & Website: [`https://www.zbmed.de/`](https://www.zbmed.de/) & [`https://www.livivo.de/`](https://www.livivo.de/)

---

## 🔬 Project Overview

Preprint servers have become vital in modern life sciences communication, offering rapid, unfiltered access to emerging research. However, because findings are locked inside PDF documents and complex visual formats (tables, formulas, figures), standard retrieval systems fail to make this knowledge machine-actionable.

**PIXLS** addresses these challenges across four collaborative research pillars:
1. **Data Ingestion & Harvesting (Continuous since 2023):** Automated ELT ingestion of 530,000+ preprints across bioRxiv, medRxiv, and 30+ OSF servers using [`pixls-preprints`](https://codeberg.org/pixls/pixls-preprints).
2. **Multimodal Information Extraction (2023–2026):** Vision-Language Models (VLMs) and Docling-powered parsing of tables, figures, captions, and contextually linked text passages via [`reanimator-vlm`](https://pypi.org/project/reanimator-vlm/).
3. **LIVIVO & Knowledge Integration (2024–2027):** Ingestion into the ZB MED Knowledge Environment (KE), enriched semantic BERT embeddings, and schema conversion for the [`LIVIVO`](https://www.livivo.de/) discovery portal using [`livivo-converter`](https://codeberg.org/pixls/livivo-converter).
4. **Synthetic IR & RAG Evaluation (2024–2027):** Revitalizing legacy test collections (TREC-COVID+) with automated, reproducible relevance assessments via LLMs (UMBRELA framework), empirical evaluation of table impact on RAG, and practical RAG demonstrators.

---

## 🛠️ Software & Resources

- **`reanimator-vlm`**: VLM-powered document parsing and synthetic relevance assessment.
  - PyPI: [`https://pypi.org/project/reanimator-vlm/`](https://pypi.org/project/reanimator-vlm/)
  - GitHub: [`https://github.com/irgroup/REANIMATOR-VLM`](https://github.com/irgroup/REANIMATOR-VLM)
  - Documentation: [`https://irgroup.github.io/reanimator-vlm/`](https://irgroup.github.io/reanimator-vlm/)
- **`pixls-preprints`**: Automated ELT acquisition pipeline for harvesting preprints across 30+ repositories.
  - Codeberg: [`https://codeberg.org/pixls/pixls-preprints`](https://codeberg.org/pixls/pixls-preprints)
- **`livivo-converter`**: Transformation and schema-mapping toolkit for LIVIVO portal integration.
  - Codeberg: [`https://codeberg.org/pixls/livivo-converter`](https://codeberg.org/pixls/livivo-converter)
- **Original REANIMATOR Framework (ACM SIGIR '25)**:
  - Repository: [`https://github.com/irgroup/Reanimator`](https://github.com/irgroup/Reanimator)
  - Paper: [`https://arxiv.org/abs/2504.07584`](https://arxiv.org/abs/2504.07584) / DOI: `10.1145/3726302.3730342`
- **SEASON 2026 Poster (REANIMATOR Sample Case)**:
  - *"Revealing the Hidden Success Factors of Scientific Papers: Structural, Linguistic, and Multimodal Dynamics"*
  - Figshare DOI: [`https://doi.org/10.6084/m9.figshare.34912698`](https://doi.org/10.6084/m9.figshare.34912698)
  - Programme: [`https://searchenginesandsociety.net/season-2026/programme/`](https://searchenginesandsociety.net/season-2026/programme/)
- **ISI 2027 Workshop**:
  - *"Information Extraction in Practice"* co-organized with ZBW & GESIS at ISI 2027 (Hamburg).

---

## 💻 Local Preview & Development

The site is built with modern vanilla HTML5, CSS3, and JavaScript with zero external build dependencies:

```bash
# Clone the repository
git clone https://github.com/irgroup/PIXLS_website.git
cd PIXLS_website

# Start a local HTTP server
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in your web browser.

---

## 🌐 GitHub Pages Deployment

The site is hosted on GitHub Pages at [`https://irgroup.github.io/PIXLS_website/`](https://irgroup.github.io/PIXLS_website/):
- Automated deployment runs via `.github/workflows/pages.yml`.
- Under repository **Settings &rarr; Pages**, ensure **Source** is set to **GitHub Actions**.

---

## 📄 License & Attribution

- Web content and documentation: [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- Source code and scripts: [MIT License](https://opensource.org/licenses/MIT)
