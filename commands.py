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
        file: path to the file.
        sorted: how the results should be sorted. If True (default), it will
            show the rules with the bigger hits first.
    Returns:
        A string containing a table with the rules and their number of hits.
    """
    # get the results
    results = utils.get_results(file)
    stats = utils.get_rule_stats(results, descending=sorted)

    return utils.stats_to_table(stats, STATS_HEADERS)