import datetime
import copy
import json
import os

import utils

try:
    from typing import List, Dict
except:
    pass

STATS_HEADERS = ["rule ID", "count"]

def stats(file: str, sorted=True) -> str:
    """
    Return the rules in the file along with their number of hits.
    The results are always sorted by number of hits.
    Arguments:
        file: path to the file or a directory with one or more files.
        sorted: how the results should be sorted. If True (default), it will
            show the rules with the bigger hits first.
    Returns:
        A string containing a list of files and a table with the rules and 
        number of hits.
    """

    # get the results
    results, names = utils.get_results(file)
    # list of analyzed files
    output = "List of analyzed files:\n"
    output += "\n".join(names)
    # table
    stats = utils.get_rule_stats(results, descending=sorted)
    output += "\n" + utils.stats_to_table(stats, STATS_HEADERS)

    return output



def split(file: str):
    """
    Splits the results in the file by rule ID. Then creates on file for each
    rule ID.
    Arguments:
        file: path to the SARIF file.        
    """

    from sarif import loader
    data = loader.load_sarif_file(file)

    # get the results.
    results = data.get_results()
    # get results by rule ID.
    results_by_ruleid = utils.get_results_by_ruleid_fast(results)

    # get input file name (w/o extension) and path
    input_file_name = data.get_file_name_without_extension()

    # get input file path, filename is not needed because we already have it
    input_file_path, filename = os.path.split(data.get_abs_file_path())

    # now we have to create one SARIF file per rule ID and store all the files
    # there.

    for rule in results_by_ruleid.keys():
            
        # help from:
        # https://github.com/microsoft/sarif-tools/blob/c76ebfed17565d7197011430b14fba13232d6108/sarif/operations/copy_op.py#L14

        sarif_data_out = {
            "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
            "version": "2.1.0",
            "runs": [],
        }

        # now = datetime.datetime.utcnow()
        # conversion_timestamp_iso8601 = now.isoformat()
        
        # I am just gonna copy the first run to the final file.
        run0 = data.runs[0]

        input_run_json_copy = copy.copy(run0.run_data)

        # I don't care about "conversions". Maybe later?
        # We can show how the modified files are created with it.

        # add the results for this rule.
        input_run_json_copy["results"] = results_by_ruleid[rule]

        # without append, then "runs" will not be a JSON array in the output.
        sarif_data_out["runs"].append(input_run_json_copy)

        # create the new file based on the old one.
        # oldfile-ruleid.sarif
        output_file_name = input_file_name + "-" + rule + ".sarif"

        # store the output files in the same path as the input.
        output_file_path = os.path.join(input_file_path, output_file_name)

        with open(output_file_path, "w", encoding="utf-8") as file_out:
            json.dump(sarif_data_out, file_out, indent=4)
    
    return

