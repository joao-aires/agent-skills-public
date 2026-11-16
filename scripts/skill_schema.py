"""Single vocabulary for skill metadata and artifact routing."""

KINDS = {'system', 'activity', 'method', 'workflow', 'reference'}
PACKS = {'sdlc', 'technical', 'craft', 'product'}
PHASES = {'planning', 'requirements', 'design', 'implementation',
          'verification', 'release', 'maintenance', 'cross-phase'}
DOMAINS = {
    'development', 'delivery', 'operations', 'security', 'governance',
    'product', 'saas', 'frontend', 'backend', 'database', 'ai', 'tooling',
    'platform', 'documentation', 'visualization', 'browser-extension',
    'native', 'go', 'typescript',
}
SCOPES = {'generic', 'stack-specific'}
INVOCATIONS = {'user', 'agent', 'both'}
ROLES = {'task', 'support'}
ORIGINS = {'local', 'upstream'}
SOFTWARE_TYPES = {'frontend', 'backend', 'ai', 'library-cli'}
