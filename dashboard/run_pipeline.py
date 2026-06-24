import subprocess
import sys

scripts = [
    "ingestion/news_api.py",
    "processing/location_extractor.py",
    "processing/scoring.py",
    "processing/geocoder.py",
    "maps/map_generator.py"
]

for script in scripts:

    print(f"\nRunning {script}...\n")

    subprocess.run(
        [sys.executable, script]
    )

print("\nPipeline Completed Successfully!")