
import re
from collections import Counter

def analyze_log(filename="sample.log"):
    counts = Counter()
    issues = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(
                r"\b(INFO|WARNING|ERROR|CRITICAL)\b",
                line
            )

            if match:
                level = match.group(1)
                counts[level] += 1

                if level in ("ERROR", "CRITICAL"):
                    issues.append(line.strip())

    print("\nSERVER LOG ANALYSIS REPORT")
    print("--------------------------")
    print("INFO:", counts["INFO"])
    print("WARNING:", counts["WARNING"])
    print("ERROR:", counts["ERROR"])
    print("CRITICAL:", counts["CRITICAL"])

    print("\nDetected Issues:")
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("No critical issues found.")

    return counts, issues


if __name__ == "__main__":
    analyze_log()
