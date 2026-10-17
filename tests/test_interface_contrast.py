import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/web-frontend/skills/interface-quality/scripts/contrast.py'
SPEC = importlib.util.spec_from_file_location('interface_contrast', SCRIPT)
contrast = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contrast)


class InterfaceContrastTests(unittest.TestCase):
    def test_black_white_and_identical_colors(self):
        self.assertAlmostEqual(contrast.evaluate('#000000', '#FFFFFF')['ratio'], 21)
        self.assertEqual(contrast.evaluate('#123456', '#123456')['ratio'], 1)
        self.assertAlmostEqual(contrast.evaluate('#FFFFFF', '#000000')['ratio'], 21)

    def test_observed_bad_recommendation_fails_three_to_one(self):
        result = contrast.evaluate('#9da599', '#f8f6ef')
        self.assertAlmostEqual(result['ratio'], 2.3466418593321454)
        self.assertFalse(result['threshold_checks']['required_non_text_information']['meets_threshold'])

    def test_aa_and_aaa_normal_text_are_different(self):
        checks = contrast.evaluate('#767676', '#ffffff')['threshold_checks']
        self.assertTrue(checks['normal_text_aa']['meets_threshold'])
        self.assertFalse(checks['normal_text_aaa']['meets_threshold'])
        self.assertTrue(checks['large_text_aaa']['meets_threshold'])

    def test_threshold_is_not_rounded_up(self):
        result = contrast.evaluate('#959595', '#ffffff')
        self.assertEqual(round(result['ratio'], 1), 3.0)
        self.assertFalse(result['threshold_checks']['required_non_text_information']['meets_threshold'])

    def test_invalid_and_alpha_colors_are_rejected(self):
        for color in ('#fff', '#ffffff80', 'transparent', '#12xz99', '', None):
            with self.subTest(color=color), self.assertRaises(ValueError):
                contrast.evaluate(color, '#ffffff')

    def test_cli_rejects_unsupported_input(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--foreground', 'rgba(0,0,0,.5)',
                                 '--background', '#ffffff'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('composite transparency first', result.stderr)


if __name__ == '__main__':
    unittest.main()
