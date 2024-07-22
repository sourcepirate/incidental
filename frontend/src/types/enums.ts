export enum IncidentRoleKind {
  REPORTER = 'REPORTER',
  LEAD = 'LEAD'
}

export enum IncidentStatusCategory {
  TRIAGE = 'TRIAGE',
  ACTIVE = 'ACTIVE',
  POST_INCIDENT = 'POST_INCIDENT',
  CLOSED = 'CLOSED'
}

export enum FormType {
  CREATE_INCIDENT = 'CREATE_INCIDENT',
  UPDATE_INCIDENT = 'UPDATE_INCIDENT'
}

export enum OrganisationKind {
  DEFAULT = 'default',
  SLACK = 'slack'
}

export enum FieldKind {
  INCIDENT_TYPE = 'INCIDENT_TYPE',
  INCIDENT_SEVERITY = 'INCIDENT_SEVERITY',
  INCIDENT_STATUS = 'INCIDENT_STATUS',
  INCIDENT_NAME = 'INCIDENT_NAME'
}

export enum FieldInterfaceKind {
  SINGLE_SELECT = 'SINGLE_SELECT',
  MULTI_SELECT = 'MULTI_SELECT',
  TEXT = 'TEXT',
  TEXTAREA = 'TEXTAREA'
}
