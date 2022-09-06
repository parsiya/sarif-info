import array
from sarif import loader
from prettytable import PrettyTable

try:
    from typing import List, Dict
except:
    pass

def get_results(file: str) -> List[Dict]:
    """
    Return the results from the SARIF file.
    Arguments:
        file: path to the file.
    Returns:
        A list of results. One result represents one hit.
    """
    data = loader.load_sarif_file(file)
    return data.get_results()


def get_ruleids(results: List[Dict]) -> List[str]:
    """
    Get a list of ruleIDs.
    """
    rules = {}
    for res in results:
        rules[res["ruleId"]] = True
    return rules

def get_results_by_ruleid(results: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Get the results, grouped by ruleid. This is O(2n) but the code looks good
    and more importantly WORKS!
    """
    # get a dictionary of ruleIDs.
    ruleids = get_ruleids(results)

    # I dunno how this works, but it works!
    return {
        ruleid: [result for result in results if result["ruleId"] == ruleid]
        for ruleid in ruleids
    }

def get_rule_stats(results: List[Dict], descending=True) -> Dict[str, int]:
    """
    Get a dictionary where the key is the ruleID and the value is the number of
    results for that rule. By default they are sorted by number of findings from
    highest to lowest.
    """
    stats = {}

    # based on this code
    # https://github.com/microsoft/sarif-tools/blob/c76ebfed17565d7197011430b14fba13232d6108/sarif/sarif_file.py#L78
    for res in results:
        ruleid = res["ruleId"]
        stats[ruleid] = stats.get(ruleid, 0) + 1
    
    # return them sorted by count descending (which is default)
    return dict(sorted(stats.items(), key=lambda item: item[1], reverse=descending))


def get_results_by_ruleid2(results: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Get a dictionary where the key is the ruleID and the value a list of all
    results for that rule. This is O(n) because why not!
    """
    stats = {}

    # based on
    # https://github.com/microsoft/sarif-tools/blob/c76ebfed17565d7197011430b14fba13232d6108/sarif/sarif_file.py#L78
    # no clue how it works!
    for res in results:
        # get the rule ID
        ruleid = res["ruleId"]

        # this returns the current value of stats[ruleid] or an empty list if
        # it does not exist.
        current_list = stats.get(ruleid, [])
        # append the new result to it.
        # Note: append always returns None so we cannot use the return value.
        current_list.append(res)
        # store the current_list in the dictionary
        stats[ruleid] = current_list
    
    # does this work?
    return stats


def stats_to_table(data: Dict[str, int], header: array) -> str:
    """
    Convert rule stats (Dict[str, int]) to a table.
    Arguments:
        data: Dict[str, int] that will be converted to a table.
        header: array of strings which contain the headers.
    Returns:
        A string which contains the data in a table.
    """
    table = PrettyTable()
    table.field_names = header
    table.align["rule ID"] = "l"

    for row in data:
        table.add_row([row, data[row]])

    return table.get_string()