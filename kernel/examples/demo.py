from kernel.consent import Consent
from kernel.state import KernelState
from kernel.audit import AuditLog

def run_demo():
    state = KernelState()
    audit = AuditLog()

    consent = Consent(
        subject_id="user_123",
        scope="data_processing"
    )

    state.register_consent(consent)
    audit.record("consent_registered", consent.consent_id)

    state.revoke_consent(consent.consent_id)
    audit.record("consent_revoked", consent.consent_id)

    print("Kernel started at:", state.started_at)
    print("Last event:", state.last_event)
    print("Audit log:")
    for event in audit.events:
        print(event)

if __name__ == "__main__":
    run_demo()
