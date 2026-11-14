"""Shared Agent Skills frontmatter checks for source and built packages."""
import re

import yaml


def validate_skill_metadata(skill):
    parts = skill.read_text().split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'Missing frontmatter: {skill}')
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict):
        raise ValueError(f'Invalid frontmatter: {skill}')
    name = metadata.get('name', '')
    if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError(f'Invalid skill name: {skill}')
    if name != skill.parent.name:
        raise ValueError(f'Skill folder/name mismatch: {skill}')
    description = metadata.get('description')
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError(f'Invalid skill description: {skill}')
    for field in ('license', 'allowed-tools'):
        if field in metadata and not isinstance(metadata[field], str):
            raise ValueError(f'Invalid skill {field}: {skill}')
    labels = metadata.get('metadata', {})
    if isinstance(labels, dict):
        if 'scope' in labels and labels['scope'] not in {'generic', 'stack-specific'}:
            raise ValueError(f'Invalid skill scope: {skill}')
        if labels.get('scope') == 'stack-specific' and (not isinstance(labels.get('stack'), str) or not labels['stack'].strip()):
            raise ValueError(f'Missing skill stack label: {skill}')
        if 'invocation' in labels and labels['invocation'] not in {'user', 'agent', 'both'}:
            raise ValueError(f'Invalid skill invocation label: {skill}')
        if 'role' in labels and labels['role'] not in {'task', 'support'}:
            raise ValueError(f'Invalid skill role: {skill}')
        if 'kind' in labels and labels['kind'] not in {'system', 'activity', 'method', 'workflow', 'reference'}:
            raise ValueError(f'Invalid skill kind: {skill}')
        if 'origin' in labels and labels['origin'] not in {'local', 'upstream'}:
            raise ValueError(f'Invalid skill origin: {skill}')
    if 'compatibility' in metadata:
        value = metadata['compatibility']
        if not isinstance(value, str) or not value.strip() or len(value) > 500:
            raise ValueError(f'Invalid skill compatibility: {skill}')
    if 'metadata' in metadata:
        value = metadata['metadata']
        if not isinstance(value, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in value.items()):
            raise ValueError(f'Skill metadata must map strings to strings: {skill}')
    if not isinstance(metadata.get('disable-model-invocation', False), bool):
        raise ValueError(f'Invalid invocation flag: {skill}')
    if not isinstance(metadata.get('user-invocable', True), bool):
        raise ValueError(f'Invalid user-invocable flag: {skill}')
    client_metadata = skill.parent / 'agents/openai.yaml'
    if client_metadata.exists():
        settings = yaml.safe_load(client_metadata.read_text())
        if not isinstance(settings, dict) or not isinstance(settings.get('policy', {}), dict):
            raise ValueError(f'Invalid client invocation metadata: {skill}')
        implicit = settings.get('policy', {}).get('allow_implicit_invocation', True)
        if not isinstance(implicit, bool) or (metadata.get('disable-model-invocation', False) and implicit):
            raise ValueError(f'Conflicting invocation metadata: {skill}')
    return metadata


def validate_local_skill_classification(skill):
    """Require the small local classification layer without constraining acquired snapshots."""
    metadata = validate_skill_metadata(skill)
    labels = metadata.get('metadata', {})
    required = ('scope', 'invocation', 'kind', 'role', 'origin')
    missing = [field for field in required if not labels.get(field)]
    if missing:
        raise ValueError(f'Missing local skill classification {missing}: {skill}')
    if labels.get('origin') != 'local':
        raise ValueError(f'Local skill origin must be local: {skill}')
    return metadata
