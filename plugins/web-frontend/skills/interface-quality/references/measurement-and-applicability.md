# Measure the applicable requirement

Use this for quantitative interface recommendations and accessibility findings. Establish which requirement applies before comparing measurements to a threshold; standards include conditions and exceptions that a numeric result alone cannot resolve.

For opaque sRGB colors, run the bundled [contrast calculator](../scripts/contrast.py) with Python 3, or use an equivalent checked method:

```sh
python3 scripts/contrast.py --foreground '#000000' --background '#ffffff'
```

Run from the skill directory. Measure the proposed pair against its actual adjacent colors and relevant states, accounting for opacity/compositing when present. The helper rejects alpha colors; use a method that resolves the real rendered colors in that case. Its unrounded ratio and separate text/non-text thresholds are measurements, not a conformance verdict. Current-palette results do not verify replacement colors.

For non-text contrast, determine whether the boundary is necessary to identify the control or state. A labelled button may be identifiable without an outline; an editable input may need a visible boundary even when its text is readable. Decorative separators can have a different role. Keep these applicability controls when assessing a boundary. See [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

Focus appearance involves applicable area and other conditions as well as contrast. A high ratio alone cannot establish AAA focus appearance. State the requirement and evidence actually checked.

Apply the same evidence discipline to non-numeric claims: clipping demonstrates hidden visual content, while copying, expansion or alternate retrieval needs its own check. Static appearance cannot establish runtime focus, persistence or recovery. Verify the claimed path or mark it unverified, and check the complete recommendation before returning it.
