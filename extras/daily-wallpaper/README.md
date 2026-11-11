# Daily wallpaper for Fluentha2 Acrylic

Acrylic needs something behind the cards to blur. This recipe gives every dashboard view the Bing image of the day,
with the photo credit available as a sensor.

## Why the custom integration

Home Assistant serves `/local/...` with `Cache-Control: max-age=2678400`, so browsers keep a file for **31 days**.
A background that is replaced every morning at the same URL therefore goes stale on every device that doesn't clear
its cache - the caption updates, the picture doesn't.

`custom_components/wallpaper` serves `/config/www/wallpaper/<file>` at **`/wallpaper/<file>`** with
`Cache-Control: no-cache`. Browsers still cache the file but revalidate it on each load, which costs a `304 Not
Modified` on days the image hasn't changed. Like `/local`, it needs no login, and it only serves files directly
inside that folder.

## Setup

1. Copy `custom_components/wallpaper` to `/config/custom_components/wallpaper` and add one line to
   `configuration.yaml`, then restart:
   ```yaml
   wallpaper:
   ```
2. Add the **Downloader** integration with `/config/www` as its download folder.
3. Add the **Scrape** integration with the resource
   `https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US` (any market code works) and two sensors:
   - `Bing wallpaper URL` with selector `url` &rarr; `sensor.bing_wallpaper_url`
   - `Bing wallpaper copyright` with selector `copyright` &rarr; `sensor.bing_wallpaper_copyright`
4. Create the automation in [`automation.yaml`](automation.yaml).
5. Point the views at it:
   ```yaml
   views:
     - title: Home
       theme: Fluentha2 Acrylic
       background:
         image: /wallpaper/bing.jpg
         size: cover
         alignment: center
         attachment: fixed
         opacity: 45
   ```

## Photo credit card (optional)

A text-only markdown card that shows the title and the copyright line under it:

```yaml
type: markdown
text_only: true
content: >-
  {%- set c = states('sensor.bing_wallpaper_copyright') -%}
  {%- if c not in ['unknown', 'unavailable', ''] -%}{%- set p = c.split(' (') -%}
  <center><small>{{ p[0] }}{% if p | count > 1 %}<br>{{ p[1] | replace(')', '') }}{% endif %}</small></center>
  {%- endif -%}
```

Bing images are for personal wallpaper use; keep the credit visible.
