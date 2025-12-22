from datetime import datetime
import uuid
class Consent:
    """
    Minimal consent object for Conscious Protocol.
    Represents explicit, revocable permission from a human subject.
    """
    def __init__(self, subject_id: str, scope: str):
        self.consent_id = str(uuid.uuid4())
        self.subject_id = subject_id
        self.scope = scope
        self.timestamp = datetime.utcnow().isoformat()
        self.active = True
    def revoke(self):
        self.active = False
