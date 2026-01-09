Governance: The Conscious Protocol is stewarded by an independent non-profit foundation in formation.  
See /foundation/FOUNDATION_CHARTER.md.
---

## English Summary (Non-Normative)

This repository provides a minimal, runnable, and auditable reference implementation
of the core concepts of the Conscious Protocol (CP), including explicit consent,
revocability, and logged state transitions.

It is published as a public working reference for inspection, evaluation, and discussion.
It is not a production system, certification, or regulatory approval.

Governance of the Conscious Protocol is intended to be carried out by an independent,
non-profit foundation. WOKE GLOBAL is a commercial entity that develops implementations
compatible with the protocol, but does not control the protocol itself.

---


> English summary available in README_EN.md.
---

Conscious Kernel

A Minimal, Auditable Reference Implementation of the Conscious Protocol

Version: 0.1
Status: Public Working Reference
Maintainer: WOKE GLOBAL


---

Overview

This repository provides a minimal, runnable, and inspectable reference implementation of the core concepts of the Conscious Protocol (CP).

It is intentionally limited in scope and exists to demonstrate that the protocol’s foundational ideas—explicit consent, revocability, and auditable state transitions—can be implemented concretely in code.

This repository is not a production system, certification, or regulatory approval.


---

Purpose

The purpose of this repository is to:

Demonstrate a minimum viable implementation of Conscious Protocol concepts

Enable inspection, auditing, and falsification of core claims

Provide a shared reference for developers, researchers, and reviewers

Support discussion and evaluation of stateful consent in AI systems


The focus is correctness, clarity, and auditability — not performance or completeness.


---

Scope and Limitations (v0.1)

Version 0.1 intentionally supports only the following:

Explicit consent creation

Consent revocation

Auditable logging of state transitions

A single runnable example (examples/demo.py)


Out of scope for v0.1

Production hardening

Security guarantees

Optimization

Distributed or networked operation

Regulatory certification or compliance claims


This version exists solely to make the core ideas real, testable, and reviewable.


---

Repository Structure

conscious-kernel/
├── examples/
│   └── demo.py              # Runnable demonstration
├── consent.py               # Consent object and state handling
├── audit.py                 # Immutable audit logging
├── CONSCIOUS_PROTOCOL.md    # Protocol overview
├── MH_AI_MINIMUM_SAFETY_REQUIREMENTS.md
└── README.md


---

Minimum Safety & Compliance Context

This repository references the document:

“Minimum Safety & Compliance Requirements for State-Interactive Mental Health AI Systems”

This document defines baseline safety obligations for AI systems that interact with, infer, or influence human mental or emotional states. It is published as a Public Working Specification and is intended as a reference for developers, auditors, and institutions.

Compliance with that document does not imply regulatory approval.


---

Governance Summary (Non-Normative)

The Conscious Protocol is intended to be stewarded by an independent, non-profit foundation to ensure long-term neutrality, openness, and public trust. Governance of the protocol is designed to prevent control by any single commercial entity and to support transparent, multi-stakeholder participation. WOKE GLOBAL is a commercial organization that develops implementations and tools compatible with the Conscious Protocol, but does not control or govern the protocol itself. Conformance to the protocol does not imply endorsement, certification, or regulatory approval.


---

Status

This repository represents a minimum, inspectable reference implementation.

It is deliberately small so that:

All behavior can be understood by inspection

All claims can be tested by execution

All state changes can be audited


Future versions may expand functionality, but backward compatibility of core concepts is expected.


---

License & Use

This repository is published for research, evaluation, and discussion purposes.

Use in production systems is at your own discretion and responsibility.


---

