from datetime import datetime
class AuditLog:
    """
    Append-only audit log for Conscious Protocol.
    Records all meaningful events with timestamps.
    """
    def __init__(self):
        self.events = []
    def record(self, event_type: str, payload: dict):
        self.events.append({
            "event_type": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat()
        })
