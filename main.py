from src.scraper import get_sample_leads
from src.enricher import enrich_batch
from src.exporter import export_to_csv

def run_pipeline():
    print("=== Starting B2B Lead Generation & AI Enrichment Pipeline ===")
    
    # Step 1: Ingest raw lead data
    raw_leads = get_sample_leads()
    print(f"[Pipeline] Loaded {len(raw_leads)} raw leads.")

    # Step 2: Enrich via Gemini + Pydantic Schema
    enriched_leads = enrich_batch(raw_leads)

    # Step 3: Sort by Lead Score and Export
    output_file = export_to_csv(enriched_leads)
    print(f"=== Pipeline Complete! Open '{output_file}' in VS Code to view results. ===")

if __name__ == "__main__":
    run_pipeline()