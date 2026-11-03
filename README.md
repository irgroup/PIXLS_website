# PIXLS: Preprint Information eXtraction for Life Sciences

Official website repository for the **PIXLS** research project, funded by the **Deutsche Forschungsgemeinschaft (DFG)** under grant number **492813820** (*Scientific Library Services and Information Systems* / LIS program).

**Project Lead Institutions:**
- **TH Köln** – Faculty of Information Science and Communication Studies, Information Retrieval Research Group (IRgroup)
  - PI: Prof. Dr. Philipp Schaer
  - Research Associate: Fabian Haak, M.Sc.
- **ZB MED – Information Centre for Life Sciences**
  - PI: Prof. Dr. Konrad U. Förstner
  - Research Associate: Benjamin Wolff, M.Sc.

---

## 🔬 Project Overview

Preprint servers have become vital in modern life sciences communication, offering rapid, unfiltered access to emerging research. However, because findings are locked inside PDF documents and complex visual formats (tables, formulas, figures), standard retrieval systems fail to make this knowledge machine-actionable.

**PIXLS** bridges this gap:
1. **Continuous Data Acquisition:** Automated ELT ingestion of 530,000+ preprints across bioRxiv, medRxiv, and 30+ OSF servers.
2. **Multimodal Information Extraction:** Vision-Language Models (VLMs) and Docling-powered parsing of tables, figures, captions, and contextually linked text passages.
3. **Synthetic Relevance Benchmarking:** Revitalizing legacy test collections (TREC-COVID+) with automated, reproducible relevance assessments via LLMs (UMBRELA framework).
4. **Knowledge Integration & RAG:** Integration into the ZB MED Knowledge Environment (KE), enriched semantic BERT embeddings, and a dedicated RAG demonstrator developed by ZB MED for Preprints and LIVIVO.

---

## 🛠️ Software & Resources

- **`reanimator-vlm`**: VLM-powered document parsing and synthetic relevance assessment.
  - PyPI: [`https://pypi.org/project/reanimator-vlm/`](https://pypi.org/project/reanimator-vlm/)
  - GitHub: [`https://github.com/irgroup/REANIMATOR-VLM`](https://github.com/irgroup/REANIMATOR-VLM)
  - Documentation: [`https://irgroup.github.io/reanimator-vlm/`](https://irgroup.github.io/reanimator-vlm/)
- **Original REANIMATOR Framework (ACM SIGIR '25)**:
  - Repository: [`https://github.com/irgroup/Reanimator`](https://github.com/irgroup/Reanimator)
  - Paper: [`https://arxiv.org/abs/2504.07584`](https://arxiv.org/abs/2504.07584) / DOI: `10.1145/3726302.3730342`
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

To host this repository on GitHub Pages (`https://irgroup.github.io/PIXLS_website/`):
1. Navigate to the repository settings on GitHub (`Settings` > `Pages`).
2. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
3. Choose the `main` branch and `/ (root)` folder, then click **Save**.
4. GitHub Pages will serve the website directly from `index.html`.

---

## 📄 License & Attribution

- Web content and documentation: [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- Source code and scripts: [MIT License](https://opensource.org/licenses/MIT)

