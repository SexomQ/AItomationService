# generated by fastapi-codegen:
#   filename:  prompt_generation_service_v1_0_0.yaml
#   timestamp: 2024-06-13T06:12:55+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Prompt(BaseModel):
    domain: Optional[str] = Field(None, example='Travel Bloging')
    action: Optional[str] = Field(
        None, example='Select a city from the list of 20 lesser-known cities.'
    )
    process: Optional[str] = Field(
        None,
        example="I run a travel blog and want to create a series of articles about hidden gems in Europe. I have a list of 20 lesser-known cities with basic info like country, population, and a few key attractions. I want to generate engaging blog posts that include a catchy title, an introduction that piques interest, a section on the city's history, a part about local cuisine, and a conclusion that encourages readers to visit. Each post should be around 800 words.",
    )
