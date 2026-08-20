# AI Engineering Homelab Roadmap

## Purpose

This repository documents the development of a personal AI engineering
homelab focused on learning how to design, build, secure, evaluate, and
operate AI agents and AI-powered applications.

The goal is not simply to run an LLM locally. The goal is to develop
practical AI engineering skills through real projects.

---

## Guiding Principles

1. Learn the underlying engineering concepts rather than blindly following tutorials.
2. Build useful systems that solve real problems.
3. Keep projects version-controlled and professionally documented.
4. Apply security principles throughout development rather than adding security at the end.
5. Use least privilege and explicit authorization for AI agents.
6. Keep human approval for consequential actions until an appropriate level of trust has been established.
7. Maintain a clear backlog so new ideas do not derail active work.
8. Prefer incremental complexity: build simple systems first, then add capabilities as they become necessary.
9. Produce portfolio-quality artifacts that demonstrate engineering judgment, not just AI experimentation.

---

# Roadmap

## Phase 1 — Engineering Foundation

Establish the development environment and learn the core tools.

- WSL2
- Ubuntu 24.04 LTS
- Linux fundamentals
- Git
- GitHub
- SSH authentication
- Python
- Basic software development workflow
- Repository structure
- Documentation and version control

### Status

In progress.

---

## Phase 2 — Project Management Foundation

Establish a structured software-development workflow before building multiple
agents.

### Priority

HIGH

The project-management system is intentionally being introduced early because
the lab will eventually contain many small applications, agents, experiments,
and ideas.

### Goals

- Select a free Jira-style project/ticket management system.
- Create a central backlog.
- Define projects, tickets, priorities, and statuses.
- Establish a lightweight software development lifecycle.
- Capture new application ideas without immediately interrupting active work.
- Track technical decisions and project milestones.
- Connect project-management records to GitHub where practical.

### Future AI integration

The Project Steward agent will eventually be able to:

- Create tickets from natural-language ideas.
- Read and summarize the backlog.
- Update ticket status.
- Prioritize or recommend work.
- Link tickets to code and documentation.
- Track project progress.
- Help prevent scope drift.

---

## Phase 3 — AI Fundamentals

Learn the concepts required to build useful AI systems.

Topics will include:

- Large Language Models (LLMs)
- Model inference
- Prompts and system instructions
- Context
- Structured outputs
- Tool calling
- APIs
- Agent architecture
- Memory
- Retrieval-Augmented Generation (RAG)
- Model selection
- Evaluation
- Observability

The objective is understanding why these components exist and when they
should be used.

---

## Phase 4 — Project Steward Agent

Build the first meaningful agent for the lab.

The Project Steward will initially focus on organization rather than
autonomous software development.

Initial responsibilities may include:

- Reading project documentation.
- Maintaining project state.
- Maintaining documentation.
- Managing the project backlog.
- Recording technical decisions.
- Helping break ideas into actionable work.
- Identifying scope drift.
- Recommending the next task.

Capabilities will be introduced incrementally.

The agent will not initially receive unrestricted access to the system.

---

## Phase 5 — Software Developer Agent

Build the software-development agent that was originally planned as the first
agent.

Its purpose is to help turn small application ideas into functioning software.

Potential capabilities include:

- Requirements clarification
- Project scaffolding
- Code generation
- File creation and modification
- Test generation
- Running tests
- Debugging
- Git operations
- Branch creation
- Pull-request creation
- Documentation generation

Human approval will remain part of the workflow for consequential actions.

---

## Phase 6 — QA and Security Agents

Expand the system with specialized quality and security capabilities.

Potential responsibilities include:

- Automated testing
- Code review
- Dependency analysis
- SBOM generation
- Vulnerability scanning
- Security testing
- AI-specific security testing
- Threat modeling
- Configuration review
- Release readiness checks

Security will be treated as a continuous engineering concern.

---

## Phase 7 — Specialized Agents

Develop agents that solve specific real-world problems.

Potential examples include:

- Real-estate market research agent
- Product research agent
- Quality-assurance agent
- Other domain-specific research or analysis agents

Agents should be specialized when specialization provides meaningful
advantages in context, tools, knowledge, or permissions.

---

## Phase 8 — Multi-Agent System

Connect specialized agents into a controlled system.

Potential architecture:

User
  |
  v
Project Steward
  |
  +---- Research Agent
  |
  +---- Developer Agent
  |
  +---- QA Agent
  |
  +---- Security Agent
  |
  +---- Specialized Agents

The Project Steward may eventually coordinate work between agents while
maintaining explicit permissions and human approval boundaries.

---

# Security Engineering Goals

Security is a first-class concern of this lab.

Areas to incorporate throughout development include:

- Identity and Access Management (IAM)
- Least privilege
- Secrets management
- Authentication
- Authorization
- Agent identity
- Credential isolation
- Filesystem isolation
- Network controls
- Dependency management
- Software Bill of Materials (SBOM)
- Vulnerability management
- Threat modeling
- Logging and auditability
- Secure software development lifecycle practices
- AI-specific security risks
- Prompt injection
- Excessive agent permissions
- Data exposure
- Tool abuse
- Human-in-the-loop controls

Security controls should be introduced when they become technically relevant
rather than artificially adding complexity before it is needed.

---

# Portfolio Goals

The lab should eventually demonstrate the ability to:

- Build AI-powered applications.
- Design and implement AI agents.
- Integrate agents with software tools.
- Design multi-agent workflows.
- Apply software engineering practices.
- Apply product-security principles to AI systems.
- Document architecture and technical decisions.
- Test and evaluate AI systems.
- Manage secrets and identities.
- Produce SBOMs and security artifacts.
- Use Git and GitHub professionally.
- Operate AI systems rather than simply experimenting with models.

The repository should provide an employer with evidence of engineering
judgment, security awareness, documentation discipline, and practical AI
engineering ability.

---

# Explicitly Tabled Ideas

These ideas are intentionally preserved but are not part of the immediate
workstream.

## App Launcher

Eventually create an application launcher/dashboard for the collection of
small applications built in the lab. It should allow executable files or
applications to be registered and presented through a simple dashboard.

## Product Research System

Eventually build an AI product-research system that identifies potentially
profitable products to source, brand, and sell. This is intended as a real
business research system rather than a "get rich quick" scheme.

## Paid AI Coding Tools

Evaluate tools such as Claude Code when the lab and its workflows are mature
enough to determine whether the productivity gain justifies the cost.

A personal rule is that paid AI coding tools should demonstrate sufficient
financial or productivity value to justify their recurring cost.

## Additional Homelab Infrastructure

Additional infrastructure such as databases, containers, orchestration,
monitoring, or self-hosted services should be introduced when a project
requires them rather than installing infrastructure for its own sake.

---

# Scope Control

New ideas should be captured rather than immediately acted upon.

When a new idea appears during an active project:

1. Capture it.
2. Determine whether it is required for the current objective.
3. If it is not required, place it in the backlog or table it.
4. Continue the current workstream.
5. Revisit the idea when its appropriate phase is reached.

The goal is to preserve creativity without allowing new ideas to constantly
redirect the project.
