#!/usr/bin/env python3
"""Check opaque sRGB color pairs; thresholds alone do not establish conformance."""
import argparse
import json
import re


def luminance(color):
    if not isinstance(color, str) or not re.fullmatch(r'#?[0-9a-fA-F]{6}', color):
        raise ValueError('Use an opaque six-digit sRGB hex color; composite transparency first.')
    color = color[1:] if color.startswith('#') else color
    channels = [int(color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def evaluate(foreground, background):
    lower, upper = sorted((luminance(foreground), luminance(background)))
    ratio = (upper + 0.05) / (lower + 0.05)
    thresholds = {'normal_text_aa': 4.5, 'normal_text_aaa': 7,
                  'large_text_aa': 3, 'large_text_aaa': 4.5,
                  'required_non_text_information': 3}
    return {'foreground': foreground, 'background': background, 'ratio': ratio,
            'threshold_checks': {name: {'minimum': minimum, 'meets_threshold': ratio >= minimum}
                                 for name, minimum in thresholds.items()},
            'limits': 'Opaque sRGB pair only. Determine text size, state and whether a boundary is required separately; this is not an accessibility-conformance result.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--foreground', required=True)
    parser.add_argument('--background', required=True)
    args = parser.parse_args()
    try:
        result = evaluate(args.foreground, args.background)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
