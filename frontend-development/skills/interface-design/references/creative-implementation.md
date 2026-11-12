# Build an expressive web experience

Read for a premium landing page, interactive portfolio, canvas or motion editor. Use [visual craft](visual-craft.md) for composition and [Design Discovery](design-discovery.md) for feedback; this reference owns mechanism selection and runtime consequences. Expressiveness is appropriate to the product, not a reason to migrate an established stack.

## Translate a reference into a mechanism

[AlignCanvas](https://aligncanvas.com/) is a useful quality reference for image-based 3D motion, live controls and export. Its public site describes WebGL rendering and WebCodecs export; this does not establish its private React framework, scene implementation or shader source. The approach below is an original implementation strategy, not a reconstruction of its code or proprietary templates. Analyze permitted references for composition, depth, timing, pointer/scroll response, transition continuity and control feedback. Record which properties matter and deliberate differences. Do not copy brand assets, paid templates or shaders without permission.

Start with one complete, content-specific interaction: choose an image, adjust a meaningful control, preview a change and recover/reset. Keep controls, labels, navigation and primary content as semantic DOM. Put an expressive scene behind or beside that structure; a canvas does not replace accessible controls or a readable fallback. Use real user-provided or licensed demo images, with explicit local-only/upload behavior. Never imply privacy if the implementation sends images to a service.

| Desired result | Smallest suitable mechanism | Escalate when |
| --- | --- | --- |
| Editorial layout, hover feedback, simple reveal | Semantic HTML, CSS/SVG; transforms and opacity | Coordinated state/layout transitions justify Motion. |
| Shared-element or component state transitions in React | Motion, preserving focus and component identity | A long sequenced/pinned narrative justifies GSAP. |
| Art-directed scroll sequence or coordinated timeline | GSAP with scoped lifecycle and media conditions | Real depth, camera or geometry requires 3D. |
| Interactive image ring, spatial gallery or scene | Three.js, or React Three Fiber in a React app | A specific material/compositing need justifies custom GLSL. |
| Liquid distortion, refraction or procedural texture | A bounded WebGL shader/material | Multiple rendering passes only after a measured visual need. |
| Video/frame processing or deterministic export | WebCodecs with capability checks and a muxer | Only when a real export requirement exists; use ordinary video for playback. |

Choose one owner per animated property. A CSS transition, Motion animation and GSAP timeline must not race over the same transform. Explain the purpose, trigger, duration/continuity, interruption behavior and reduced-motion equivalent. Avoid taking over native scrolling for ordinary navigation. Review library versions, runtime licenses, peer compatibility and browser support at implementation time; this plugin ships guidance, not these application dependencies.

## React and Next.js boundaries

Preserve the accepted framework. In a new compatible React/Next.js project, render content and page structure normally and isolate browser APIs, scene controls and animations in small Client Components. Do not make the entire page client-rendered solely for a decorative scene. Lazy-load the heavy scene behind a stable-size poster/fallback; `ssr: false` for a browser-only scene belongs in a Client Component. Handle pending module load, texture failure and WebGL/context loss. A route should remain readable before JavaScript/GPU work completes. Keep React state for semantic control changes; update frame uniforms/transforms through refs rather than allocating objects or setting state every frame.

Use an explicit feature switch for decorative motion, including OS reduced-motion changes. Remove event listeners, animation frames, observers, GSAP contexts, object URLs and owned GPU resources on teardown. Route changes and React development remounts should not double the timeline or leak a renderer. See [Next.js lazy loading](https://nextjs.org/docs/app/guides/lazy-loading), [Motion reduced motion](https://motion.dev/docs/react-use-reduced-motion), and [GSAP React lifecycle](https://gsap.com/resources/React/).

## Original worked mechanisms

These examples explain the effect and its invariants; adapt them to the accepted stack rather than copying an untested application scaffold.

### A product image ring with a deterministic loop

For `N` image planes, assign angle `theta_i(t) = 2*pi*i/N + 2*pi*t/T`. Place each at `(R*sin(theta), 0, R*cos(theta))`, then orient toward the center or camera consistently. Separate the camera distance, plane scale, radius and period into meaningful controls with numeric labels and keyboard input. Choose depth spacing and near/far planes to prevent clipping. Use an appropriate aspect ratio per texture rather than stretching every image square.

Drive both preview and export from the same pure `sceneAt(time, settings)` function. Wrap `time` into `[0,T)`; geometry and shader inputs must all be periodic. Avoid random values per render; use a stored seed if texture noise varies. Export `M` frames at `t_k = k*T/M`, `k = 0..M-1`: duplicating the endpoint adds a pause. The conceptual endpoint at `T` should match `0`, while adjacent exported frames retain the intended motion step. Test that continuity separately from browser snapshots. A scrubber, pause/reset and static contact sheet make the same content usable without dragging or autoplay.

### A restrained shader lens

Begin with one image plane and UV coordinates, then add a local radial displacement. A simple original fragment-stage model is:

```glsl
// Inputs use UV coordinates. Texture color handling belongs to the material pipeline.
vec2 delta = vUv - uPointer;
float r = length(delta);
float weight = 1.0 - smoothstep(0.0, max(uRadius, 0.001), r);
vec2 sampleUv = clamp(vUv + delta * weight * uStrength, 0.0, 1.0);
vec4 image = texture2D(uImage, sampleUv);
```

This is UV displacement, not physically accurate glass. In a non-square viewport, correct radial distance for aspect ratio. Define edge behavior instead of sampling uninitialized pixels. Keep strength bounded, move pointer uniforms without React rerenders, and default strength to zero for reduced motion or touch-only use. Hover is enhancement; content and controls remain operable without it. For real refraction, budget render targets, resolution, sampling and transparency ordering; validate tone/color handling and alpha export. Compile shaders against the project's actual WebGL/material version. See [Three.js ShaderMaterial](https://threejs.org/docs/#api/en/materials/ShaderMaterial).

### An editorial reveal that leaves content present

Keep the heading readable in initial HTML. In a scoped React effect or GSAP `useGSAP`, attach enhancement only after mount. Use a media condition that disables translation/parallax under reduced motion; revert the context at teardown. For a component transition with Motion, derive `initial`/`animate` from `useReducedMotion()` and use a short opacity-only change or no transition when requested. Do not hide content indefinitely if a trigger fails. Test mid-animation navigation and repeated mounting. Decorative pointer attraction must not move the actual hit target away from the user's pointer or keyboard focus.

## Scene performance and resilience

In React Three Fiber, use demand rendering for resting scenes and invalidate on controls/uniform changes; continuous motion needs a running frame loop only while visible and active. Pause offscreen and in hidden tabs. Cap/adapt device pixel ratio, reuse geometry/materials, instance repeated forms, size textures for their actual screen footprint and dispose resources by ownership. Measure before adding postprocessing, shadow maps or layered refraction. [R3F scaling performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance) explains demand rendering and its invalidation contract.

Agree a target device and budget in the brief. A reasonable starting target for an interactive 60 Hz scene is a frame within 16.7 ms on that named device; measure tail latency and sustained behavior rather than claiming universal 60 fps. Record network bytes, cold load, long tasks, memory/GPU behavior where observable and idle activity. Protect meaningful content and input responsiveness before decoration. Use a poster/contact sheet when context creation fails, reduced motion is enabled, or the device cannot meet the agreed budget. Dynamic quality changes should not erase user work.

## Export only when the product needs it

WebCodecs supplies codecs, not a complete MP4/WebM container writer. Check secure-context/API availability and `VideoEncoder.isConfigSupported()` for the intended codec, dimensions, framerate and platform; availability is not proof of success. Choose a compatible muxer and inspect its license. PNG sequence/still export is a useful fallback; never rename an arbitrary byte stream `.mp4`.

Render deterministic frame times independently of display `requestAnimationFrame`. Feed `VideoFrame` timestamps in microseconds, close frames, honor encoder queue backpressure, handle output/error callbacks, flush before finalizing the muxer, and support cancellation with resource cleanup. Report progress for accepted/completed frames. Plan memory limits for large images and exports, avoid an unbounded list of raw frames, and validate decoded duration, dimensions, color/alpha support and loop continuity. Do not promise transparency for codecs that do not support the required alpha path. Image CORS/tainted-canvas restrictions apply; test owned local input and denied/corrupt assets. Upload/worker behavior should match the privacy promise. See [WebCodecs processing guidance](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs).

## Inspiration and redistribution

[Motion Primitives](https://github.com/ibelick/motion-primitives) can inform component-level patterns; [React Bits](https://github.com/DavidHDev/react-bits) can inform effect exploration. They are reference links, not vendored code or required dependencies. Inspect current licenses for the actual asset/code and intended use before adopting it, especially material with Commons Clause terms. The snippets and mechanism descriptions here are original; no AlignCanvas, React Bits or Motion Primitives implementation/assets are redistributed.
