import json
import pprint
import sys
try:
    with open("good.json", "r",  encoding="utf-8") as fd:
        ltm = []
        for el in json.load(fd)["detail"]["diagrams"][0]["diagramJson"]["cells"]:
            tmp = {}
            for key in ["type", "hasOpenThreats", "isWebApplication", "isEncrypted",
                        "description", "privilegeLevel", "isPublicNetwork", "outOfScope"]:
                if key in el.keys():
                    tmp[key] = el[key]
            if "text" in el["attrs"] and "text" in el["attrs"]["text"]:
                tmp["text"] = el["attrs"]["text"]["text"]
            if "threats" in el.keys():
                tmp["threats"] = {}
                for threat in el["threats"]:
                    for t in threat.keys():
                        if t in ["description", "mitigation", "modelType",
                                 "severity", "status", "title", "type"]:
                            tmp["threats"][t] = threat[t]
            ltm.append(tmp)
        pprint.pprint(ltm)
except IOError as e:
    print(f"Bad Human: {e}")
