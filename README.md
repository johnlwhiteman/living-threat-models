# Living Threat Model (LTM)

### When Apps Evolve, So Does the Risk And So Should the Threat Model

![](images/tms-are-ramen-not-milk.png)

### All Threat Models Should Be Machine Readable

![](images/machine-readable.png)

### Threat Model Tools Are Dangerously Shiny Objects

![](images/etcha-a-sketch.png)

### Put the TM in the CI/CD

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

### THREATS.md Is the New README.md

````
```threats
---
 name: "A Threat Model"
 date: 2022-06-11
assets:
   - database
   - ...
trust_boundaries:
   - public: https
   - ...
```
````

### Scan Threat Models Like You Scan Code

![](demo/demo.gif)

### Must Feed the TM to Keep It Alive

![](images/dffml.png)
