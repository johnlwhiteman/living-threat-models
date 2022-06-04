# Living Threat Model (LTM)

## GitFlow Scenarios

### LTM as a Branch

```mermaid
%%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'showBranches': true, 'showCommitLabel':false}} }%%
    gitGraph
        commit tag: "init {...}"
        branch ltm
        checkout ltm
        commit tag: "v1.0"
        checkout main
        merge ltm tag: "v1.0"
        branch b1
        checkout b1
        commit tag: "hotfix {∅}"
        checkout main
        merge b1 tag: "v1.1"
        branch b2
        checkout b2
        commit tag: "cloud {Δ}"
        checkout ltm
        merge b2 tag: "v2.0"
        checkout main
        merge ltm tag: "v2.0"
        checkout b1
        merge main
        commit tag: "hotfix {CVE}"
        checkout ltm
        merge b1 tag: "v3.0"
        checkout main
        merge ltm tag: "v2.1"
        checkout ltm
        commit tag: "0 Day"
```

### LTM w/o the Branch

```mermaid
%%{init: { 'themeVariables': {'git0': '#FFCB5D', 'git1': '#77A3FF', 'git2':'#FF7A5D'}, 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'showBranches': true, 'showCommitLabel':false}} }%%
    gitGraph
        commit tag: "v1.0"
        branch b1
        checkout b1
        commit tag: "hotfix {∅}"
        checkout main
        merge b1 tag: "v1.1"
        branch b2
        checkout b2
        commit tag: "cloud {Δ}"
        checkout main
        merge b2 tag: "v2.0"
        checkout b1
        merge main
        commit tag: "hotfix {CVE}"
        checkout main
        merge b1 tag: "v2.1"

```