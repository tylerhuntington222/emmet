from typing import List, Dict, Any
from pydantic import BaseModel


class StructureVisualization(BaseModel):
    """
    Subclass of `pydantic.Basemodel` used for schema validation
    of Stores built by `VisualizationBuilder`.
    """
    
    scene: Dict[str, Any]
    legend: Dict[str, dict]
    settings: Dict[str, Any]
    source: Dict[str, Any]
