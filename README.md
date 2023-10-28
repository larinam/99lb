# 99lb
Business Process Workflow Automation

## Example configuration YAML
```yaml
name: Document Approval Process
steps:
  - id: 1
    name: initiation
  - id: 2
    name: First threshold
    responsible-roles: 
      - name: Department1
      - name: Department2
    responsible-individuals:
      - id: 1
      - id: 2
  - id: 3
    name: Distribution
    responsible-roles: 
      - name: Department3
```

On the initiation initiator chooses the BP Workflow to initiate and fills at least one field with free text.
After creation the process starts automatically.
Process can be sent to the previous step or returned to the initiator.
Process can time out or be escalated automatically.
