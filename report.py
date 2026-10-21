from events import EVENTS
from stats import count_by_type, average_score


def main():
    print("Event counts:", count_by_type(EVENTS))
    print("Average score:", average_score(EVENTS))


if __name__ == "__main__":
    main()
