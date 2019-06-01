from typing import List, Dict, Any
from pydantic import BaseModel

class StructureVisualization(BaseModel):
    scene: Dict[str, Any]
    legend: Dict[str, dict]
    settings: Dict[str, Any]
    source: Dict[str, Any]
