import sys
import json
from models import RectangleInput
from calculator import calculate_properties

def main():
    """
    Main loop to read from stdin, process data, and write to stdout.
    This script acts as a sidecar process for the main Tauri application.
    """
    for line in sys.stdin:
        try:
            
            input_data = json.loads(line)
            
            payload = input_data.get("payload", {})
            metadata = input_data.get("metadata", {})
            center_coords = metadata.get("center", {"x": 0, "y": 0})

            
            rectangle_input = RectangleInput(**payload)

           
            properties = calculate_properties(rectangle_input, center_coords)

          
            output_json = json.dumps(properties.to_json())

            
            print(output_json)
            sys.stdout.flush()

        except json.JSONDecodeError as e:
            error_message = json.dumps({"error": f"Invalid JSON input: {e}"})
            print(error_message, file=sys.stderr)
            sys.stderr.flush()
        except Exception as e:
            error_message = json.dumps({"error": f"An unexpected error occurred: {e}"})
            print(error_message, file=sys.stderr)
            sys.stderr.flush()


if __name__ == "__main__":
    main()