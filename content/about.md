---
heading: "The PIXLS Project & Scope"
lead: "Preprint servers have transformed scientific communication in the life sciences, enabling immediate dissemination of groundbreaking results. However, traditional digital library systems struggle to index the rich multimodality of preprints."
challenge_title: "The Challenge: Extracting Multimodal Structures from Scientific Literature"
solution_title: "The PIXLS Solution: Multimodal AI & Open Science"
solution_intro: "Funded by the Deutsche Forschungsgemeinschaft (DFG) in the LIS program (*Wissenschaftliche Literaturversorgungs- und Informationssysteme*), PIXLS tackles both dimensions:"
solution_points:
  - color: "teal"
    text: "**Automated Ingestion Pipeline:** Continuous harvesting of 530,000+ preprints from [bioRxiv](https://www.biorxiv.org/), [medRxiv](https://www.medrxiv.org/), and 30+ [OSF](https://osf.io/preprints/) archives using [`pixls-preprints`](https://codeberg.org/pixls/pixls-preprints)."
  - color: "berry"
    text: "**Vision-Language Parsing:** Moving beyond brittle legacy rule-based tools to [Docling](https://github.com/DS4SD/docling) and modern Vision-Language Models (dots.mocr) with [`reanimator-vlm`](https://pypi.org/project/reanimator-vlm/)."
  - color: "gold"
    text: "**Synthetic Relevance Benchmarks:** Generating validated multimodal relevance labels using LLMs (UMBRELA framework) to revive legacy test collections (TREC-COVID+)."
  - color: "teal"
    text: "**Preprint RAG Demonstrator & LIVIVO:** The ZB MED team has engineered a usable RAG demonstrator connecting preprint intelligence with **[LIVIVO](https://www.livivo.de/)**, while the CIR team at TH Köln focused on advancing deep multimodal information extraction."
diagram:
  heading: "Modular Research Architecture"
  image: "assets/img/pipeline-diagram.svg"
  alt: "PIXLS System Architecture: Acquisition, Multimodal Extraction, Synthetic IR, and Knowledge Integration"
  caption: "Figure 1: Modular data flow from multi-source preprint harvesting through VLM parsing and synthetic test collection revitalization to ZB MED Knowledge Environment and [LIVIVO](https://www.livivo.de/) integration."
---

Scientific literature in biomedicine is inherently multimodal: the most essential experimental data, dosage tables, statistical results, and molecular observations are embedded within tables, figures, and visual layouts. Standard full-text search engines treat PDFs as flat strings of text, completely losing structural context and rendering tables and figures invisible to retrieval algorithms.

Furthermore, evaluating retrieval systems on new tasks requires costly human relevance judgments. Test collections age quickly, failing to reflect modern user requirements such as complex question-answering and Retrieval-Augmented Generation (RAG).
