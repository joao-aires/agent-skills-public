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
    return metadata
