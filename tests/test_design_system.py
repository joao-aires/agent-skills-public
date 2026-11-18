"""Structural checks for the software-type and design-record model."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / 'plugins/sdlc/skills/artifact-system/references'
DESIGN = ROOT / 'plugins/sdlc/skills/design'
ACTIVITY = ROOT / 'plugins/sdlc/skills/activity-system'


class DesignSystemTests(unittest.TestCase):
    def test_four_software_types_and_references_exist(self):
        index = (ARTIFACTS / 'software-types.md').read_text()
        for name in ('frontend', 'backend', 'ai', 'library-cli'):
            with self.subTest(type=name):
                self.assertIn(name, index)
                path = ARTIFACTS / 'software-types' / f'{name}.md'
                self.assertTrue(path.is_file(), path)
                text = path.read_text()
                for heading in ('## What this is', '## Design record must show',
                                '## Verification that counts', '## Not required'):
                    self.assertIn(heading, text)

    def test_type_versus_constraint_is_explicit(self):
        text = (ARTIFACTS / 'software-types.md').read_text()
        for marker in ('constraint', 'component', 'Browser extension', 'REST',
                       'SaaS', 'anti-rigidity'):
            with self.subTest(marker=marker):
                self.assertIn(marker.lower(), text.lower())
        self.assertIn('not a project', text.lower())
        self.assertNotIn('software_type:', text)

    def test_design_proposal_contract_has_required_sections(self):
        text = (ARTIFACTS / 'contracts/design-proposal.md').read_text()
        for heading in ('## Affected software types', '## Options',
                        '## Linked design artifacts', '## Tradeoffs and failure behavior',
                        '## Seam decisions', '## Recommendation and decision'):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)
        self.assertIn('at least three', text.lower())
        self.assertIn('materially different', text.lower())

    def test_one_contract_per_artifact_type(self):
        text = (ARTIFACTS / 'contracts/README.md').read_text()
        self.assertIn('one contract per artifact', text.lower())
        self.assertIn('not one per software type', text.lower())
        self.assertIn('design-proposal.md', text)

    def test_design_methods_cover_options_validation_and_review(self):
        option = (DESIGN / 'references/option-set.md').read_text()
        self.assertIn('at least three', option.lower())
        self.assertIn('materially different', option.lower())
        for lens in ('Frontend', 'Backend', 'AI', 'Library/CLI'):
            self.assertIn(lens, option)

        validation = (DESIGN / 'references/design-validation.md').read_text()
        self.assertIn('## Modes', validation)
        self.assertIn('validated', validation.lower())
        self.assertIn('test', validation.lower())

        review = (DESIGN / 'references/design-review.md').read_text()
        for marker in ('Software types', 'Options', 'Linked artifacts', 'Reopen'):
            self.assertIn(marker, review)

    def test_design_skill_links_the_new_references(self):
        text = (DESIGN / 'SKILL.md').read_text()
        for target in ('software-types.md', 'design-proposal.md', 'option-set.md',
                       'design-validation.md', 'design-review.md', 'engagement-state.md'):
            with self.subTest(target=target):
                self.assertIn(target, text)
        self.assertIn('not implement', text.lower())

    def test_engagement_state_supports_parallel_threads_and_reopen(self):
        text = (ACTIVITY / 'references/engagement-state.md').read_text()
        for marker in ('## State block', 'Threads', 'Reopen protocol',
                       'Side topics', 'One focus, many threads'):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)
        self.assertIn('parallel', text.lower())

    def test_transitions_include_reentry(self):
        text = (ACTIVITY / 'references/transitions.md').read_text()
        self.assertIn('reopen', text.lower())
        self.assertIn('parallel', text.lower())
        self.assertIn('Design validation', text)

    def test_documentation_states_software_type_is_not_metadata(self):
        text = (ROOT / 'docs/metadata.md').read_text()
        self.assertIn('software type is not skill metadata', text.lower())
        self.assertIn('software_type', text)

    def test_readme_and_sdlc_docs_link_the_design_system(self):
        readme = (ROOT / 'plugins/sdlc/README.md').read_text()
        self.assertIn('software-types.md', readme)
        self.assertIn('design-proposal.md', readme)
        self.assertIn('engagement-state.md', readme)
        guide = (ROOT / 'docs/sdlc.md').read_text()
        self.assertIn('software-types.md', guide)
        self.assertIn('design-proposal.md', guide)

    def test_artifact_guides_are_explicit_guides(self):
        guides = sorted((ROOT / 'plugins/sdlc/skills').glob('guide-*/SKILL.md'))
        self.assertEqual(len(guides), 22)
        for path in guides:
            with self.subTest(guide=path.parent.name):
                self.assertTrue(path.parent.name.startswith('guide-'))
                front = path.read_text().split('---', 2)[1]
                metadata = yaml.safe_load(front)
                labels = metadata['metadata']
                self.assertEqual(labels['kind'], 'guide')
                self.assertEqual(labels['pack'], 'sdlc')
                self.assertEqual(labels['role'], 'support')
                self.assertEqual(labels['invocation'], 'both')
                text = path.read_text()
                for heading in ('## Minimum content', '## Common failures', '## Handoff'):
                    self.assertIn(heading, text)

    def test_metadata_defines_the_guide_kind(self):
        text = (ROOT / 'docs/metadata.md').read_text()
        for kind in ('system', 'activity', 'method', 'workflow', 'guide', 'reference'):
            with self.subTest(kind=kind):
                self.assertIn(f'`{kind}`', text)
        self.assertIn('`kind: guide`', text)
        self.assertIn('`guide-adr`', text)
        self.assertIn('artifact guide registry', text.lower())

    def test_skill_map_includes_guides_and_counts(self):
        text = (ROOT / 'docs/skills-map.md').read_text()
        self.assertIn('158 skills', text)
        for name in ('guide-design-spec', 'guide-architecture-views',
                     'guide-state-machine', 'guide-compatibility-matrix',
                     'guide-runbook', 'guide-prd', 'guide-rfc', 'guide-adr',
                     'guide-ecr', 'guide-design-proposal', 'guide-system-documentation',
                     'guide-incident-record', 'guide-postmortem',
                     'guide-assurance-assessment', 'guide-issue', 'guide-pr',
                     'guide-research-report', 'guide-release-note', 'guide-readme',
                     'guide-product-feedback-analysis', 'guide-roadmap', 'guide-data-model'):
            self.assertIn(name, text)


if __name__ == '__main__':
    unittest.main()
