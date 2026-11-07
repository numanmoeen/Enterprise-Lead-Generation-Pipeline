import os
import pandas as pd

def export_to_csv(enriched_leads: list[dict], output_path: str = "data/enriched_leads.csv") -> str:
    """
    Sorts enriched leads by lead_score (highest first) and exports to a clean CSV.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.DataFrame(enriched_leads)

    if "lead_score" in df.columns:
        df = df.sort_values(by="lead_score", ascending=False)

    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"[Exporter] Saved {len(df)} prioritized leads to {output_path}")
    return output_path