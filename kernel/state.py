from datetime import datetime


class KernelState:
    """
    Minimal state container for the Conscious Kernel.

    Represents the current operational state of a system
    that is required to respect consent and produce auditability.
    """

    def __init__(self):
        self.started_at = datetime.utcnow().isoformat()
        self.active_consents = {}
        self.last_event = None

    def register_consent(self, consent):
        self.active_consents[consent.consent_id] = consent
        self.last_event = "consent_registered"

    def revoke_consent(self, consent_id: str):
        if consent_id in self.active_consents:
            self.active_consents[consent_id].revoke()
            self.last_event = "consent_revoked"
