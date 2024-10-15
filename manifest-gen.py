import os
import json

def generate_json_structure(base_directory):
    json_data = []
    categories = ['filament', 'printer', 'print']

    # Iterate over the categories
    for category in categories:
        folder_path = os.path.join(base_directory, category)
        
        # Ensure the folder exists
        if not os.path.exists(folder_path):
            print(f"Warning: {folder_path} does not exist")
            continue

        # Iterate over all .ini files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".ini"):
                    file_path = os.path.join(root, file)
                    file_path = os.path.relpath(file_path, base_directory)
                    file_id = os.path.splitext(file)[0]  # filename without extension
                    
                    json_entry = {
                        "type": category,
                        "path": file_path,
                        "label": file_id
                    }
                    
                    json_data.append(json_entry)

    return json_data

# Set the base directory to the same location as the script
base_directory = os.path.dirname(os.path.abspath(__file__))

# Generate the JSON structure
json_structure = generate_json_structure(base_directory)

# Convert to JSON and print it out
json_output = json.dumps(json_structure, indent=4)
print(json_output)

# Optionally, write to a file
with open("manifest.json", "w") as outfile:
    outfile.write(json_output)
