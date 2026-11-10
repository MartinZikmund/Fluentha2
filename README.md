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

## Fluentha2 Acrylic

A second theme in the same file: cards become Windows 11 **Acrylic** - a translucent tint with a 30px blur and
150 % saturation of whatever sits behind them. It uses Home Assistant's own `--ha-card-backdrop-filter` variable,
so it still needs **no card-mod**. Give the view a background image so there is something to blur:

```yaml
views:
  - title: Tablet
    theme: Fluentha2 Acrylic
    background:
      image: /local/wallpaper.jpg
      size: cover
      alignment: center
      attachment: fixed
      opacity: 60   # the theme's base colour shows through, which darkens the image
```

Backdrop blur is GPU work on every repaint. It is smooth on desktops and recent tablets; on older or low-power
devices (cheap wall tablets, old Fire tablets) stick to plain `Fluentha2`.

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
4. Optional but recommended on non-Windows devices: add the **Open Sans** font as a dashboard resource.
   Settings > Dashboards > three-dot menu > **Resources** > Add resource:
   `https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap`, type **Stylesheet**.

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

- Font stack: `"Segoe UI Variable", "Segoe UI", "Open Sans", system-ui`. Windows keeps Segoe; Android, Linux and
  Apple devices get Open Sans when the Google Fonts resource above is registered, otherwise their system font.
- There's no real Mica (wallpaper-tinted blur) in a browser; the base colour is the solid Mica fallback Windows uses.

## License

MIT - see [LICENSE](LICENSE).
