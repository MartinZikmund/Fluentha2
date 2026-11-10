# Fluentha2

A Windows 11 / WinUI 3 **Fluent Design** theme for Home Assistant: Mica-style background, layered 8px cards with a
1px hairline stroke instead of shadows, Segoe UI Variable typography on the Fluent type ramp, and the Windows default
accent blue. One theme, light and dark built in.

![Screenshot placeholder](docs/screenshot.png)

The theme is called `Fluentha2` so it can sit next to the original
[Fluentha](https://github.com/MartinZikmund/Fluentha) without a name clash.

## Why another one

- **Small and plain.** One theme entry, roughly 300 lines of CSS variables. No card-mod, no generated files, nothing
  that reaches into the frontend's shadow DOM - so a frontend update can't break it in weird ways.
- **Real WinUI tokens.** Colours come straight from the WinUI 3 theme resources (`SolidBackgroundFillColorBase`,
  `CardBackgroundFillColorDefault`, `CardStrokeColorDefault`, `TextFillColor*`, `AccentFillColorDefault`,
  `SystemFillColor*`). The YAML is commented with the mapping.
- **Readable state colours.** Off is neutral, on is accent, lights glow warm amber, and locks/alarms/doors use the
  Fluent success/caution/critical colours.

| | Dark | Light |
|---|---|---|
| Background (Mica) | `#202020` | `#f3f3f3` |
| Card layer | `#2b2b2b` | `#fbfbfb` |
| Card stroke | white 7 % | black 6 % |
| Accent | `#60cdff` | `#005fb8` |
| Lights on | `#ffc463` | `#d38300` |

## Install

### HACS (custom repository)

1. Make sure your `configuration.yaml` loads themes from a folder:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
2. HACS (or the Marketplace on 2026.11+) > three-dot menu > **Custom repositories** > add
   `https://github.com/MartinZikmund/Fluentha2`, category **Theme**.
3. Download **Fluentha2**, then run the `frontend.reload_themes` action (or restart).

### Manual

Copy `themes/fluentha2.yaml` into `/config/themes/` and reload themes.

## Use

- **Everywhere:** Profile > Theme > **Fluentha2**. Light/dark follows the profile's mode switch.
- **One view only** (great for a wall tablet):
  ```yaml
  views:
    - title: Tablet
      theme: Fluentha2
  ```
- **As the default:** `frontend.set_theme` with `name: Fluentha2` (and `mode: dark` for the dark default).

## Notes

- Segoe UI Variable is only on Windows 11. Elsewhere it falls back to the system UI font (Roboto on Android,
  SF on Apple devices), which still looks clean.
- There's no real Mica (wallpaper-tinted blur) in a browser; the base colour is the solid Mica fallback Windows uses.

## License

MIT - see [LICENSE](LICENSE).
