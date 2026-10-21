def count_by_type(events):
    counts = {}
    for e in events:
        counts[e["type"]] = counts.get(e["type"], 0) + 1
    return counts


def average_score(events):
    if not events:
        return 0
    return sum(e["score"] for e in events) / len(events)


def max_score(events):
    return max((e["score"] for e in events), default=0)
