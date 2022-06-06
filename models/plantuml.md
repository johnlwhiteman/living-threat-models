# PlantUML Threat Model

```plantuml
@startuml
rectangle "in scope and trust boundary" {
  [Customer\nDatabase] <- (Web Server):HTTPS
}
(Web Server) <- (Client\nApplication):HTTPS
@enduml
```