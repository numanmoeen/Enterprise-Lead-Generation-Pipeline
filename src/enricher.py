import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()

class EnrichedLead(BaseModel):
    company_name: str = Field(description="Official name of the business.")
    estimated_headcount: Optional[str] = Field(description="Estimated team size or number of specialists.")
    core_service: str = Field(description="Primary product or service offered.")
    automation_bottleneck: str = Field(description="Likely operational or lead-handling bottleneck based on the text.")
    lead_score: int = Field(description="Score from 1 to 10 indicating how badly they need AI/workflow automation.")
    cold_email_icebreaker: str = Field(description="A personalized 1-sentence opening line pitching AI automation for their specific bottleneck.")

client = genai.Client()

def enrich_single_lead(raw_text: str, source_url: str) -> dict:
    prompt = (
        "Analyze the following raw website text from a prospective B2B client. "
        "Extract their company details, identify their manual workflow bottleneck, "
        "score them as an AI automation prospect, and write a hyper-personalized cold email icebreaker.\n\n"
        f"Website Text:\n{raw_text}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a senior B2B RevOps analyst. Rely strictly on provided facts; do not invent company metrics.",
                response_mime_type="application/json",
                response_schema=EnrichedLead,
                temperature=0.1,
            ),
        )
        lead_data = response.parsed.model_dump()
        lead_data["source_url"] = source_url
        return lead_data

    except Exception as e:
        print(f"[Enricher Error] Failed on {source_url}: {e}")
        return {
            "company_name": "PARSE_ERROR",
            "estimated_headcount": None,
            "core_service": None,
            "automation_bottleneck": None,
            "lead_score": 0,
            "cold_email_icebreaker": None,
            "source_url": source_url,
        }

def enrich_batch(leads: list[dict]) -> list[dict]:
    enriched_results = []
    for idx, item in enumerate(leads, start=1):
        print(f"[Enricher] Processing lead {idx}/{len(leads)}: {item['source_url']}...")
        result = enrich_single_lead(item["raw_text"], item["source_url"])
        enriched_results.append(result)
    return enriched_results