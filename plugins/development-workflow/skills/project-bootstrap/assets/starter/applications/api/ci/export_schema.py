import json
from pathlib import Path

from notes.main import app

path = Path(__file__).resolve().parents[3] / "documentation/architecture/schemas/openapi.json"
path.write_text(json.dumps(app.openapi(), indent=2, sort_keys=True) + "\n")
