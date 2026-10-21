from events import EVENTS
from stats import count_by_type, average_score

assert count_by_type(EVENTS)["level_end"] == 2, "count_by_type is wrong"
assert average_score(EVENTS) == 44.0, "average_score is wrong"
print("all tests passed")
