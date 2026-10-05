#!/usr/bin/env python3
"""Repository entrypoint for the self-contained bootstrap inventory helper."""
from pathlib import Path
import runpy
_script = Path(__file__).resolve().parents[1] / "plugins/development-workflow/skills/project-bootstrap/scripts/inventory_skills.py"
if __name__ == "__main__":
    runpy.run_path(str(_script), run_name="__main__")
else:
    inventory = runpy.run_path(str(_script))["inventory"]
