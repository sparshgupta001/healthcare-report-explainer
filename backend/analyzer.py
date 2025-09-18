import json
import re

# Load normal ranges from a JSON file (optional)
try:
    with open("normal_ranges.json", "r") as f:
        NORMAL_RANGES = json.load(f)
except FileNotFoundError:
    NORMAL_RANGES = {
        "Hemoglobin": {"min": 13.0, "max": 17.0, "unit": "g/dL", "meaning": "Protein that carries oxygen in blood"},
        "Cholesterol": {"max": 200, "unit": "mg/dL", "meaning": "Fat-like substance; high levels may cause heart disease"},
    }

def analyze_text(text):
    """
    Extract key health metrics from raw text and generate simple explanations.
    """
    results = []
    lines = text.split("\n")

    for line in lines:
        # Extract numeric values
        match = re.match(r"([A-Za-z ]+):?\s*([\d.]+)", line)
        if match:
            test_name = match.group(1).strip()
            value = float(match.group(2))

            explanation = f"{test_name}: {value}"

            if test_name in NORMAL_RANGES:
                range_info = NORMAL_RANGES[test_name]
                if "min" in range_info and value < range_info["min"]:
                    explanation += f" ⬇ (Low) – may indicate {range_info['meaning']}"
                elif "max" in range_info and value > range_info["max"]:
                    explanation += f" ⬆ (High) – may indicate risk for {range_info['meaning']}"
                else:
                    explanation += " ✅ (Normal)"

            results.append({"test": test_name, "value": value, "explanation": explanation})

    return results
