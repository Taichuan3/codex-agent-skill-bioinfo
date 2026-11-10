# User-Supplied Assets

Read this before using paper figures, experiment result charts, screenshots, logos, or other assets that must appear in the deck.

When the user provides paper figures, experiment result charts, screenshots, logos, or other assets that must appear in the deck, treat them as source assets, not as loose visual inspiration.

Recommended project-local asset location:

```text
{base_dir}/{deck_name}/assets/
├── figures/
│   ├── result_01.png
│   └── result_02.png
└── logos/
    └── lab_logo.png
```

Do not place source assets in `origin_image/`; that directory is only for final `slide_XX.png` images.

For slides that must include a user-supplied figure:

- Record the exact asset path or attachment name in `outline.md` for that slide, preferably as a Markdown image reference inside that slide's `Required images` list, then ask the user to confirm the mapping before generation.
- Stay on the already selected image backend. Do not switch between built-in image generation and CLI/API fallback only because a slide includes source images.
- Use the selected backend's reference-image or edit capability when available, with the supplied figure visible as an input image.
- In built-in `image_gen` mode, every source image must be visible in the conversation context before generating any slide that depends on it. User attachments and images generated earlier in the thread already qualify. For local image paths, inspect each required image with `view_image` first, then generate or edit the slide.
- In built-in mode, inspect local images before generation and pass them through the current tool's documented image-reference mechanism. Label each image's role; do not assume conversation visibility alone attaches an image or transfers it to a worker.
- Ask the model to preserve the supplied figure's data, labels, axes, colors, and visual content, and only compose the surrounding slide layout, title, captions, callouts, and background.
- Do not ask the model to "redraw", "recreate", "imagine", or "generate a similar chart" for result figures unless the user explicitly wants a stylized redraw.
- After generation, compare the output to the original figure: labels, axes, values, curves, bars and legends. A preservation prompt or visual resemblance is not proof of scientific fidelity. If exact preservation is required or cannot be verified, stop the slide and offer `pptx-generator` for lossless source-image embedding; do not report the generated figure as unchanged data.

Example prompt fragment for a result-figure slide:

```json
{
  "source_assets": [
    {
      "path": "{base_dir}/{deck_name}/assets/figures/result_01.png",
      "usage": "embed as the main evidence figure",
      "fidelity": "preserve the figure content; do not redraw or change data, axes, labels, colors, curves, bars, or legends"
    }
  ],
  "visual_elements": {
    "main_visual": "place the supplied result_01.png as a large figure panel, with a short caption and two callouts around it"
  },
  "constraints": [
    "Use the provided figure as an input image, not as a loose style reference.",
    "Do not synthesize a replacement chart.",
    "Keep all numerical values and labels in the supplied figure unchanged."
  ]
}
```
