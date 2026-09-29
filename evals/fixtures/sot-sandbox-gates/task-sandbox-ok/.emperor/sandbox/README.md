# Sandbox — ports, mocks, sims, isolation

Powers: sandboxing, mocking, simulating, isolating,
parallel testing. Ports allocated per artifact; stacks
raised per artifact. Simulator emits docker-compose (or
equivalent) wiring SOT plugins together.

Files (v1 stubs):
- `ports.json` — allocated host ports per artifact
- `manifest.json` — mock/sim declarations

CLI: `emperor sandbox plan|up|down|ports`
Profiles: `profiles/{isolate,mock,simulate}.json` (loadable).
Runtimes: compose | podman | k8s via `emperor runtime use`.
