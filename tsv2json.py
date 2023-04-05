#! /usr/bin/env python3
import os
import csv
import json

tsv_dir = "./tsv"  # set the folder name
json_dir = "./json"  # set the folder name

# loop over all subfolders in the tsv folder
for folder_name in os.listdir(tsv_dir):
    folder_path = os.path.join(tsv_dir, folder_name)
    json_path = os.path.join(json_dir, folder_name + ".json")
    print ("Processing: " + folder_name)
    # check if the subfolder is a directory
    if os.path.isdir(folder_path):
                
        note = ""
        note_marker = "> **Note**"
        
        # read the README.md file if it exists
        readme_path = os.path.join(folder_path, "README.md")
        if os.path.isfile(readme_path):
            with open(readme_path, "r") as readme_file:
                #readme_content = readme_file.read()
                for line in readme_file:
                  #print (line)
                  if line.startswith(note_marker):
                    break
                  note += line
        
        tsv_data = {
          "id": folder_name,
          "description": note,
          "terms": {}
          }  # initialize the dictionary for this tsv file
        
        # loop over all tsv files in the subfolder
        for filename in os.listdir(folder_path):            
            if filename.endswith(".tsv"):                
                filepath = os.path.join(folder_path, filename)
                filename_parts = os.path.splitext(filename)[0].split("_")
                #print (filename_parts)                
                
                # read the tsv file and extract the data
                with open(filepath, "r") as tsv_file:
                    tsv_reader = csv.reader(tsv_file, delimiter="\t")
                    next(tsv_reader)  # skip the first row if it starts with DB_Term
                    for row in tsv_reader:
                        
                        # Check the length of the list
                        list_len = len(row)
                        
                        # If the list has less than 5 values, add empty values to the end
                        if list_len < 5:
                          row += [None] * (5 - list_len)

                        # If the list has more than 5 values, remove the extra values
                        elif list_len > 5:
                          row = row[:5]
                        
                        if len(row) == 5:
                            term, label, description, sameAs, source = row
                            
                            if term not in tsv_data["terms"]:
                              tsv_data["terms"][term] = {
                                "term": term,
                                "label": {filename_parts[-1]: label},
                                "description": {filename_parts[-1]: description},
                                "sameAs": sameAs,
                                "source": source
                                }
                            else:
                              tsv_data["terms"][term]["label"][filename_parts[-1]] = label
                              tsv_data["terms"][term]["description"][filename_parts[-1]] = description
        
        # Convert dictionary to JSON
        json_str = json.dumps(tsv_data, indent=2)
        
        if os.path.isfile(json_path):
          with open(json_path, 'w') as file:
            file.write(json_str)
        else:
          with open(json_path, 'x') as file:
            file.write(json_str)
