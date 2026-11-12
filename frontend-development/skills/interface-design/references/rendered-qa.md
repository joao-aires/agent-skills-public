# Verify the rendered interface

Read during browser implementation/refinement or visual regression work. Reuse the project's browser runner, fixtures and accessibility tools. Playwright or a compatible browser driver supplies execution; this skill does not install a browser or promise access. Without runtime access, inspect available current artifacts, identify their revision and freshness, and report live checks as unverified.

## Build an evidence loop

1. Start the documented local app with owned fixtures, record route/revision and browser, and use a stable screenshot environment. Keep server lifecycle/cleanup explicit.
2. Capture a representative target with actual content at desktop and narrow widths (for example 1440×900 and 390×844), relevant themes and important states. Include long text and a failure/retry path where applicable. Wait for intended content, fonts and scene readiness; `networkidle` alone does not establish readiness.
3. Open and inspect the screenshots. Compare hierarchy, composition, spacing, clipping, contrast and identity with the brief. Record concrete findings and affected shared owners, then repair authorized changes and recapture. Never describe a capture command as visual review.
4. Exercise the primary task, keyboard/focus sequence, dialogs and recovery. A screenshot cannot establish those behaviors. Run available automated accessibility checks and targeted manual operation; use [measurement and applicability](measurement-and-applicability.md) for numeric claims.
5. Measure the agreed performance budget on a named browser/device profile. Retain precise gaps, including unavailable screen-reader/device/GPU checks. Stop when the scoped acceptance criteria are satisfied or a real blocker is recorded, rather than looping for cosmetic novelty.

For animated scenes, capture an explicit deterministic time and scene state through a test-only control, plus the reduced-motion/static fallback. Playwright's CSS animation disabling does not freeze an arbitrary WebGL clock. Separately inspect a live motion sample for continuity, interruption and jank. A static shader frame is not proof of good movement.

## Adaptable Playwright example

Use the project's installed Playwright test version/configuration and actual route/selectors. This example is a pattern, not a bundled runnable application test:

```ts
import { test, expect } from '@playwright/test';

for (const viewport of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
  test(`editor at ${viewport.width}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto('/editor'); // configured local baseURL, owned fixture
    await expect(page.getByRole('heading', { name: 'Image editor' })).toBeVisible();
    await page.evaluate(() => document.fonts.ready);
    await expect(page.getByRole('button', { name: 'Reset view' })).toBeVisible();
    await expect(page).toHaveScreenshot(`editor-${viewport.width}-reduced.png`, {
      animations: 'disabled',
    });
    await page.getByRole('button', { name: 'Reset view' }).focus();
    await page.keyboard.press('Enter');
    await expect(page.getByRole('button', { name: 'Reset view' })).toBeFocused();
  });
}
```

Add meaningful assertions for the actual state change, loading/failure/retry, denied image/codec capability and no-WebGL fallback when those features exist. For a new baseline, capture first, open the image and review it before accepting; do not blindly run update-snapshots after a failure. Screenshot baselines require a consistent browser/OS/fonts/rendering environment; GPU output can vary. Mask only genuinely nondeterministic incidental content, not the feature being verified. See [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).

## Completion evidence

Report routes/states/viewports and source revision, screenshot paths, observed findings/repairs, actual behavior/accessibility checks, performance conditions/results and unverified boundaries. Keep aesthetic judgment, user preference, automated regressions and feature correctness separate. If no user responded, the direction remains an implemented recommendation. A clean build, detector score or passing screenshot diff cannot establish aesthetic quality or full accessibility conformance.
