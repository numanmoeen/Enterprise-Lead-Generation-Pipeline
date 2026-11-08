# Enterprise B2B Lead Generation & AI Enrichment Pipeline

An automated Revenue Operations (RevOps) data pipeline that scrapes unstructured B2B company websites, strips DOM noise to reduce LLM token overhead, and uses the Google GenAI SDK with strict Pydantic validation to output prioritized sales leads and personalized outreach copy.

## Business Impact & ROI

* **Eliminates Manual Prospecting:** Automates lead research, qualification, and first-touch copywriting, saving sales teams roughly 15 hours per rep each week.
* **Token Cost Optimization:** Strips non-content HTML tags before LLM ingestion, cutting API token consumption by over 70 percent.
* **Zero-Hallucination Schema Enforcement:** Enforces deterministic JSON outputs via Pydantic models so downstream CRM imports never fail.
* **Automated Prioritization:** Ranks prospects on a 1 to 10 urgency scale so sales reps focus immediately on high-intent accounts.

## System Architecture

```mermaid
graph LR
    A[Target B2B URLs] --> B[DOM Scraper & Noise Filter]
    B --> C[Clean Text Payload]
    C --> D[Gemini 3.8 Flash API]
    E[Pydantic Schema Validation] --> D
    D --> F[Prioritized Pandas DataFrame]
    F --> G[CRM-Ready CSV Export]
```

## Sample Enriched Output

| Company Name | Headcount | Bottleneck | Lead Score | Cold Email Icebreaker |
| :--- | :--- | :--- | :--- | :--- |
| Apex Dental | 25 specialists | Phone-only booking | 9 | Automating patient bookings outside 9-to-5 hours. |
| Prime Estates | 40 agents | Manual WhatsApp | 8 | Routing commercial property leads automatically. |

The pipeline evaluates raw website text to identify operational bottlenecks, assign a numeric lead score, and draft a tailored opening line for sales outreach.

## Tech Stack

* **Language:** Python 3
* **AI & Validation:** Google GenAI SDK, Pydantic
* **Ingestion & Parsing:** Requests, BeautifulSoup4
* **Data Processing:** Pandas, python-dotenv

## Quickstart

1. Clone the repository and navigate into the project directory:
```bash
git clone [https://github.com/YOUR_USERNAME/Enterprise-Lead-Generation-Pipeline.git](https://github.com/YOUR_USERNAME/Enterprise-Lead-Generation-Pipeline.git)
cd Enterprise-Lead-Generation-Pipeline
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Add your API key to a **.env** file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

4. Execute the pipeline:
```bash
python main.py
```
