# 99lb
Business Process Workflow Automation

## Entities
* People/Individuals
* Roles/Tags, which can be assigned to People/Individuals
  * Natural roles, like an Author/Initiator 
  * Manually assigned roles
* Groups to which Pople/Individuals can be grouped
  * Nested groups
  * Organisation hierarchy or hierarchies

## Example configuration YAML
```yaml
name: Document Approval Process
steps:
  - id: 1
    name: Initiation
  - id: 2
    name: First threshold
    responsible:
      roles: 
        - id: Role1
        - id: Role2
      individuals:
        - id: Individual1
        - id: Individual2
    escalation:
      timeout: 10m
      responsible:
        individuals:
          - id: Individual3
  - id: 3
    name: Distribution
    responsible:
      roles: 
        - id: Role3
      groups:
        - id: Group1
    escalation:
      timeout: 2h
      responsible:
        individuals:
          -id: Individual3
```

On the initiation the initiator chooses the BP Workflow to initiate and fills at least one field with free text.
After creation the process starts automatically.
Process can be sent to the previous step or returned to the initiator.
Process can time out or be escalated automatically.
