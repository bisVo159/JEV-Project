from questions import  TOPICS

def aggregate(ratings):
    """
    ratings: list of dicts, each dict is a set of ratings for a single review e.g. [{"Camera": 4.0}, {"Display": 3.5}, ...]

    Returns : {Camera:{"average": 3.5, "count": 2}, Display: {"average": 4.0, "count": 1}, ...}
    """

    aggregated_results = {}

    for topic in TOPICS.keys():
        scores=[rating[topic] for rating in ratings if topic in rating]
        if scores:
            aggregated_results[topic] = {
                "average": round(sum(scores) / len(scores),1),
                "count": len(scores)
            }
        else:
            aggregated_results[topic] = {
                "average": None,
                "count": 0
            }

    return aggregated_results