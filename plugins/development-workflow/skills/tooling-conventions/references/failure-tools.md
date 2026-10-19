# Selected failure injection tools

Use project-native deterministic controls for routine fixtures. Add an optional proxy only when its real fault mechanism answers the accepted claim, with a pinned compatible version, explicit routes, bounded lifetime and cleanup independent of success.

- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) supports scoped deterministic substitutions for Python tests; prefer project-native fixtures and ensure patches are undone.
- [Toxiproxy](https://github.com/Shopify/toxiproxy) is an optional TCP fault proxy for isolated connection/delay tests. Use a reviewed compatible version and explicit affected routes; it does not simulate every protocol, provider or regional failure.


A thrown exception cannot establish a remote commit whose acknowledgment was lost. Use a controlled service that can commit and withhold the response when that boundary matters, and inspect persistent effects independently. Keep simulated, locally injected and actual provider evidence distinct.
