import pprint
import sys
from parser import parse

def audit(ltm):
    issues = []
    for tm in ltm:
        if tm["type"] == "tm.Flow":
            if tm["protocol"] == "HTTP":
                issues.append({
                    "CIA": "",
                    "Issue": "No Encryption",
                    "Protocol": "HTTP",
                    "Type": "Flow",
                    "Category": "Vulnerability",
                    "Severity": "Critical",
                    "Description": tm["description"]
                })
            if tm["label"] == "":
                issues.append({
                    "CIA": "",
                    "Issue": "Missing Label",
                    "Type": "Flow",
                    "Category": "Quality",
                    "Severity": "Low",
                    "Description": tm["description"]
                })

        if tm["type"] == "tm.Store":
            if tm["storesCredentials"]:
                if not tm["isEncrypted"]:
                    issues.append({
                        "CIA": "C",
                        "Issue": "No Encryption",
                        "Type": "Store",
                        "Category": "Vulnerability",
                        "Severity": "Critical",
                        "Description": tm["description"]
                    })
    return issues

if __name__ == "__main__":
    pprint.pprint(audit(parse(sys.argv[1])))
