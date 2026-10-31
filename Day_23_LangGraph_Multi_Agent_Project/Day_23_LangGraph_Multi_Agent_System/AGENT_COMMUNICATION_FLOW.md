# Agent Communication Flow

Example request: “Prepare a short research response about how a multi-agent assistant can support our company project.”

| Step | Sender → Receiver | Information | Result |
|---|---|---|---|
| 1 | User → Coordinator | Company project request | Request stored in shared state |
| 2 | Coordinator → Research Agent | Request and plan | Research begins |
| 3 | Research Agent → Writer | Selected local research notes | Writer receives evidence |
| 4 | Writer → Coordinator | Structured draft | Draft stored in shared state |
| 5 | Coordinator → User | Validated final response | Answer displayed and saved |

Shared state: `user_request`, `plan`, `research_notes`, `draft`, `final_answer`, `communication_log`, `errors`, `status`.

Error path: empty request, missing knowledge base, or failed writing/research node is routed to Error Handler. It creates a failure summary and stops safely. The actual timestamped interaction is saved in `outputs/communication_log_<request>.json`.
