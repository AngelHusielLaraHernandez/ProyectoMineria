# Carpeta: MenuVersion2/decky-ps5-dashboard

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## .gitignore

Ruta: `MenuVersion2/decky-ps5-dashboard/.gitignore` · Bytes: 83 · SHA-256: `2149caecd4c27b84223fd7183e749125be6eeb2e8564e5672cebfc3f51d81817`

````text
node_modules/
dist/
*.zip
!ps5-dashboard.zip
__pycache__/
*.pyc
.DS_Store
preview/

````

## CHANGELOG.md

Ruta: `MenuVersion2/decky-ps5-dashboard/CHANGELOG.md` · Bytes: 6849 · SHA-256: `14e425baed28e188d019fcf2619938023bb105adb7a615cdf28f76247d71c9f3`

````text
# Changelog

## 1.10.0

- **The plugin speaks your Steam language.** 1.9.0 detected Steam's language, but the plugin only had English and
  Portuguese text. It now ships 14 languages: English, Portuguese, Spanish, French, German, Italian, Polish, Russian,
  Ukrainian, Turkish, Japanese, Korean, Simplified Chinese and Traditional Chinese. Any other Steam language gets
  English, never the operating system's language.
- Plurals follow each language's rules ("2 дня" / "5 дней", "2 miesiące" / "5 miesięcy"...).
- Translations live in `src/locales/`, one file per language, all checked against the English one so no string
  can go missing.
- **Rounded corners actually work now.** Steam registers a CSS property called `--r` as an angle, and the plugin used
  that same name for its corner radius, so Steam threw the value away and every tile, card and button on the plugin's
  screens came out square. The plugin's variables now have their own names, and the **Tile corner radius** setting
  (0–24 px) rounds the game covers on the home row, the lower rows, the Game Library, the info cards and the buttons.
- **The glass aura follows the corners.** The animated edge around the focused game now curves with the tile, and its
  light shades through grey and the accent blue as well as white and translucent black.

## 1.9.0

- **New setting: Hide bottom bar (Ocultar barra inferior).** Under the Layout section, users can now toggle off the
  controller button hints footer bar (A, B, X, Y buttons, Legion Go / Xbox / Steam glyphs) at the bottom of the screen.
- **Fixed SteamOS native language detection.** Robust locale detection mapping 30+ internal Steam language codes
  (such as "brazilian", "portuguese", "latam", etc.) to proper ISO prefixes, ensuring SteamOS in Portuguese or English
  always shows the matching UI text seamlessly.
- **Improved header and game row spacing.** Adjusted spacing between the top-right option buttons (search, settings,
  power, profile avatar) and the main home game tiles to prevent overlap when tiles or avatar focus labels are selected.

## 1.8.0

- **New setting: Open Steam's library.** When it's on, the Game Library tile at the end of the home row, its shortcut
  cards, the Game Library shortcut and the Media tab's Apps card open Steam's own library instead of the PS5 Game
  Library, so your TabMaster tabs and sorting are right there. The tile then shows "Steam Library". It's off by
  default, so the PS5 Game Library stays the default. Requested by a user on Reddit.

## 1.7.0

- **New setting: Style Steam's library.** Turn it off to leave Steam's own library as Steam draws it (capsule corners,
  focus, tabs and page background), for example to use TabMaster's tabs and sorting. The PS5 home screen, menus and
  Game Library are not affected. Requested by a user on Reddit.

## 1.6.0

- **Steam menu pills fixed.** Steam scaled the focused and the current item to 110%, pushing the pill past the
  panel's edge, where it lost its right corners. Items now stay inside the panel, the focus gets a gentle 2% lift,
  and its glow is no longer cut into a hard band.
- **Long labels fit.** Items are sized so "Friends & Chat" and similar labels fit instead of turning into Steam's
  scrolling marquee, and the focused label is always black on white.
- **Quick Access tabs are real circles.** The tabs are 48 × 64 px, so rounding them gave stretched ovals; a fixed
  circle behind the icon is the highlight now, without Steam's scale-and-clip focus effect.
- **Steam's library looks like the PS5.** A navy gradient page, tabs as pills in sentence case with dimmed counts, and
  a crisp white edge with a soft lift on the focused capsule instead of a wide white bloom.

## 1.5.0

- **Steam menu (left side) in PS5 style.** Dark navy glass panel, rounded items, a white focused item with black text
  and a soft glow, and the current page in bold with a small PlayStation-blue dot. Steam's blue panel and its
  translucent focus animation are gone.
- **The theme now reaches the Steam menu and Quick Access windows.** In Game Mode they don't always appear in Steam's
  popup list, so the plugin also looks them up through Steam's controller navigation, the way Steam itself tracks them.
- **Your time** card: non-Steam games show when you last played them instead of "Not played yet".
- The plugin panel shows its version, so you can check which build Steam has loaded.

## 1.4.0

- **Home row like the PS5.** The next games now sit right after the selected one instead of leaving a wide gap, and
  the game's name moves under them. The tile before the selected one peeks in at the left edge.
- **Lift and glass aura.** The focused game lifts slightly with a drop shadow, and a glass light band keeps circling
  its edge, blending white, grey and translucent black. It only rotates (a GPU transform), so it costs nothing per
  frame, and only the focused tile has it.

## 1.3.0

- **Game options on Select.** Press Select (View) or ≡ on any game tile, on Home, in the lower rows or in the Game
  Library, to open Steam's own game menu, with whatever other plugins add to it, such as SteamGridDB's
  "Change artwork…".
- The round **⋯** button next to Play now opens the same game menu, like on the PS5.
- If Steam's game menu can't be found after a client update, these buttons open the game's page instead.

## 1.2.0

- **Info cards under Play:** Time to beat (HowLongToBeat), Your time, Reviews and Achievements. Each opens the
  matching page. The Store and Game Library tiles get shortcut cards.
- HowLongToBeat lookups run only after the selection rests on a game, and are cached on disk for a week.
- **Menus are PlayStation blue and white now.** The Power menu and every other option menu get a dark rounded panel
  and a white focused item. Steam used to paint "Switch to Desktop" and other items red or green.
- The Steam menu and Quick Access are themed reliably: Steam bundles several copies of their style modules, and every
  copy is matched now instead of only the first.
- Shortcut tiles are glass tiles with a round icon instead of flat grey boxes.
- The background dims to PlayStation navy in the lower rows, and the game row and info fade out instead of sliding
  under the tabs.

## 1.1.0

- The selected game on the home row no longer hides or gets cut off. The row now slides by whole tiles with a GPU
  transform instead of resizing tiles and scrolling mid-animation, and the browser can no longer scroll it on its own.
- The game art crossfades with a slight zoom, and the row slides in when Home opens.
- Lighter on performance: every animation is a transform or an opacity change.

## 1.0.0

- First release: PS5 home screen, Games and Media tabs, Game Library, PS5 colors everywhere, Control Center-style
  menus, accent colors and PlayStation-style font.

````

## LICENSE

Ruta: `MenuVersion2/decky-ps5-dashboard/LICENSE` · Bytes: 1067 · SHA-256: `0e7a71c62e915d523de51d987d42a597c19621b7ab713f240334004cb424e775`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## README.md

Ruta: `MenuVersion2/decky-ps5-dashboard/README.md` · Bytes: 11755 · SHA-256: `cac42ecef28ed9c66f606d9e948006afc21ad6f4c6f2cb916455b27cdcfe2b97`

````text
<div align="center">

# PS5 Dashboard

**Make SteamOS Game Mode look and feel like the PlayStation 5 home screen.**

A [Decky Loader](https://decky.xyz) plugin for the Steam Deck and other handhelds running SteamOS.

[![Latest release](https://img.shields.io/github/v/release/kromossomom-debug/decky-ps5-dashboard?label=release&color=0070D1)](https://github.com/kromossomom-debug/decky-ps5-dashboard/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/kromossomom-debug/decky-ps5-dashboard/total?color=0070D1)](https://github.com/kromossomom-debug/decky-ps5-dashboard/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-0070D1)](LICENSE)
[![Decky Loader](https://img.shields.io/badge/Decky-Loader-0070D1)](https://decky.xyz)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/kromossomoc)

<img src="docs/screenshots/home.jpg" alt="PS5 Dashboard home screen with God of War selected" width="100%">

</div>

## Features

- **PS5 home screen.** Replaces Steam's home with a row of square tiles along the top: the Steam Store first, your
  recent games, and the Game Library at the end. The selected game stays big on the left with its name beside it,
  while its key art fills the whole screen.
- **Game info, PS5 style.** The game's logo, when you last played it and for how long, a white **Play** button and a
  round **⋯** button for the game's options.
- **Info cards under Play:**
  - **Time to beat** from [HowLongToBeat](https://howlongtobeat.com): Story, + Extras and 100%, with a bar showing how
    far into the story your playtime gets you.
  - **Your time:** total playtime, when you last played and the last two weeks.
  - **Reviews:** Steam review score, Metacritic and installed size.
  - **Achievements:** unlocked count, a progress bar and the three most recent unlocks.

  Each card opens the matching page. Under the Store and Game Library tiles the cards become shortcuts (Specials,
  Wishlist, Search, Installed, Games, Apps).
- **Game options on Select.** Press **Select** (View) or **≡** on any game, or pick **⋯**, to open Steam's own game
  menu. It includes what other plugins add to it, such as **SteamGridDB's "Change artwork…"**.
- **Games and Media tabs.** Switch with **L1 / R1**, like on the PS5. Search, Settings, Power and your profile sit in
  the top-right corner.
- **Game Library.** A grid of square tiles with filter pills along the top: Playable, Your Collection, Apps,
  Favorites, Non-Steam and your own collections, sorted by Recent or A–Z.
- **Lower rows.** Scroll down for Favorites, Installed and Shortcuts. The game art dims to PlayStation navy as you go.
- **PS5 colors everywhere.** Repaints Steam's own blues, greens and slate greys with PlayStation blue and the PS5's
  deep, cool greys: menus, buttons, toggles and pages, not just the plugin's screens.
- **Control Center-style menus.** The Steam menu, Quick Access and option menus (such as Power) get a dark rounded
  panel and a white focused item, without Steam's red and green highlights.
- **PS5 effects.** White focus glow, an art crossfade with a slight zoom, a sliding game row and staggered card
  entrances.
- **Accent colors.** PlayStation blue by default, or the console and DualSense colors: Starlight Blue, Cobalt Blue,
  Cosmic Red, Nova Pink, Galactic Purple, Volcanic Red and more.
- **Speaks your language.** The plugin follows the language you picked in Steam: English, Portuguese, Spanish,
  French, German, Italian, Polish, Russian, Ukrainian, Turkish, Japanese, Korean and Simplified and Traditional
  Chinese. Any other Steam language gets English. Translations live in `src/locales/`, one file per language, and
  improvements are welcome.

## Screenshots

| | |
|:-:|:-:|
| <img src="docs/screenshots/play.jpg" alt="Play button focused on Cyberpunk 2077"><br>**Play** focused, with the info cards | <img src="docs/screenshots/store.jpg" alt="Steam Store tile selected"><br>**Steam Store** tile with shortcut cards |
| <img src="docs/screenshots/rows.jpg" alt="Favorites, Installed and Shortcuts rows"><br>**Favorites, Installed and Shortcuts** | <img src="docs/screenshots/library.jpg" alt="Game Library grid with filter pills"><br>**Game Library** |
| <img src="docs/screenshots/media.jpg" alt="Media tab cards"><br>**Media** tab | |

> These screenshots are rendered from the plugin's own stylesheet at the Steam Deck's 1280×800 resolution, with
> sample library data. The HowLongToBeat times shown are real.

### Running on a handheld

| | |
|:-:|:-:|
| <img src="docs/photos/handheld-home.jpg" alt="PS5 Dashboard on a handheld, God of War III selected"> | <img src="docs/photos/handheld-store.jpg" alt="PS5 Dashboard on a handheld, Steam Store selected"> |

*Photos of an earlier build (v1.1) on the author's handheld, with Steam in Portuguese.*

## Installation

### From the release ZIP

1. Install [Decky Loader](https://decky.xyz) if you haven't already.
2. Download **`ps5-dashboard.zip`** from the [latest release](https://github.com/kromossomom-debug/decky-ps5-dashboard/releases/latest)
   (it's also in the repository root: [`ps5-dashboard.zip`](ps5-dashboard.zip)).
3. In Game Mode, open **Quick Access (`…`) → Decky → ⚙ Settings → General** and turn on **Developer mode**.
4. Go to **Developer → Install plugin from ZIP** and pick `ps5-dashboard.zip`.
5. Open **Quick Access → Decky → PS5 Dashboard** to adjust it.

To update, install the new ZIP the same way. Your settings are kept.

> Use one dashboard theme at a time. If you also have **Xbox Dashboard** or a CSS Loader theme that restyles the home
> screen, turn it off first, or the two will fight over the home screen and Steam's colors.

## Controls

| Button | Where | Action |
|---|---|---|
| **L1 / R1** | Anywhere | Switch between the Games and Media tabs |
| **A** | Game tile or Play | Play (or resume / view the game if it isn't installed) |
| **Select (View) / ≡** | Any game tile | Steam's game menu: Favorites, Manage, Properties, SteamGridDB's *Change artwork…* |
| **⋯ button** | Game info | Same game menu |
| **Y** | Game tile | Game details page |
| **D-pad down** | Home | Play button → info cards → Favorites, Installed, Shortcuts |
| **B** | Media, Game Library | Back to Games |

## Settings

Everything lives in the plugin panel in Quick Access. Settings are saved to
`~/homebrew/settings/ps5-dashboard/settings.json`.

| Setting | What it does | Default |
|---|---|---|
| Enable PS5 look | Turns the whole theme on or off | On |
| PS5 home screen | Replaces Steam's home with the PS5 one | On |
| Open Steam's library | The Game Library tile and shortcuts open Steam's own library (handy with TabMaster) | Off |
| Info cards | Cards under the Play button | On |
| HowLongToBeat | Looks up how long each game takes to beat | On |
| PS5 colors everywhere | Repaints Steam's own colors | On |
| Accent color | PlayStation blue or a console / DualSense color | PlayStation blue |
| Home background | Game art, accent gradient or dark | Game art |
| Focus | White glow (PS5) or accent glow | White |
| Tile corner radius | 0–24 px | 12 px |
| Control Center-style menus | Restyles the Steam menu, Quick Access and option menus | On |
| Style Steam's library | PS5-style capsules, focus and tabs in Steam's own library; turn off for Steam's look or TabMaster | On |
| Clean home screen | Hides What's New, Friends and Recommended on Steam's own home | Off |
| PlayStation-style font | Uses SST if installed, otherwise Noto Sans | On |

## Performance

The plugin is built to stay out of the way of your games:

- **GPU-only animation.** Every animation is a transform or an opacity change, so the GPU runs it without the page
  being laid out again. There are no blur filters and no animation that loops forever.
- **No work while you scroll fast.** HowLongToBeat is only looked up after the selection rests on a game for half a
  second, and each answer is cached on disk for a week (misses for a day). Achievements are cached for five minutes.
- **Light DOM.** Rows are memoized, so moving the focus re-renders only the background and the game info. At most
  two background images exist at once.
- **In-place repaint.** Steam's colors are swapped inside its own stylesheets instead of adding a large override
  sheet, and only new stylesheets are scanned afterwards.

## How it works

Steam's CSS class names are hashed and change with every client update, so the plugin never hard-codes them. At
runtime it finds Steam's class modules by their stable key names (`RecentGamesContainer`, `BasicGameCarouselItem`,
`contextMenuItem`…) and builds its stylesheet from them. Steam ships several copies of some modules, like the main
menu and Quick Access, so every copy is matched. The stylesheet goes into each Game Mode window (`SP`, `QuickAccess`,
`MainMenu`) and is put back if Steam recreates one.

The home screen replaces the `/library/home` route through Decky's router patching. If it ever fails to render, Steam's
own home is shown instead. The game menu is Steam's own `LibraryContextMenu`, which is why other plugins' menu items
show up in it.

HowLongToBeat has no public API. The Python backend does what the website does (a short-lived search token, then a
search), matches the Steam name to the closest HowLongToBeat entry and caches the result. Lookups run off the loader's
event loop.

Turning the plugin off or uninstalling it removes everything and restores Steam's original colors.

## Building from source

Requirements: Node.js 18+ and npm.

```bash
git clone https://github.com/kromossomom-debug/decky-ps5-dashboard.git
cd decky-ps5-dashboard
npm install
npm run build
./scripts/package.sh   # creates ps5-dashboard.zip
```

```
src/
  index.tsx      plugin entry, Quick Access panel, route patches
  Shell.tsx      tabs, top-right icons, Media cards
  Ps5Home.tsx    home row, background, game info
  InfoCards.tsx  HowLongToBeat, playtime, reviews and achievement cards
  Library.tsx    Game Library grid
  theme.ts       stylesheet for Steam's own screens
  palette.ts     in-place repaint of Steam's colors
  classes.ts     runtime lookup of Steam's class modules
  styles.ts      stylesheet for the plugin's screens
  i18n.ts        picks Steam's language; locales/ holds one file per language
py_modules/
  hltb_client.py HowLongToBeat lookups with a disk cache
main.py          Decky backend: settings and HowLongToBeat
```

## Known limitations

- A Steam client update can rename the modules the plugin relies on. Parts of the theme then stop applying until the
  plugin is updated. Nothing breaks: the home screen falls back to Steam's own.
- HowLongToBeat matching works by name, so a few games with unusual Steam names may show no times.
- Non-Steam shortcuts have no achievements or reviews, so those cards are hidden for them.

## Support

If you enjoy the plugin, you can buy the author a coffee. It helps keep it updated. The plugin's panel in Quick Access
has a **Buy Me a Coffee** button too.

<a href="https://buymeacoffee.com/kromossomoc"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="50"></a>

Bug reports and ideas are welcome in [Issues](https://github.com/kromossomom-debug/decky-ps5-dashboard/issues).

## Disclaimer

This is an unofficial fan project. It is not affiliated with, endorsed by or sponsored by Sony Interactive
Entertainment, Valve or HowLongToBeat. PlayStation, PS5 and DualSense are trademarks of Sony Interactive
Entertainment Inc. Game artwork shown in the screenshots belongs to its respective owners.

## License

[MIT](LICENSE) © 2026 kromossomo

````

## main.py

Ruta: `MenuVersion2/decky-ps5-dashboard/main.py` · Bytes: 1693 · SHA-256: `c8f38735d766026c3260fd8bc759fbc65a837ff87e8242473b6ad2cd60742517`

````text
import asyncio
import json
import os

import decky

from hltb_client import HltbClient

SETTINGS_FILE = os.path.join(decky.DECKY_PLUGIN_SETTINGS_DIR, "settings.json")
HLTB_CACHE_FILE = os.path.join(decky.DECKY_PLUGIN_RUNTIME_DIR, "hltb_cache.json")


class Plugin:
    hltb: HltbClient | None = None

    async def hltb_times(self, appid: int, name: str) -> dict | None:
        """HowLongToBeat times (in seconds) for a game, or None if it isn't found."""
        if self.hltb is None:
            self.hltb = HltbClient(HLTB_CACHE_FILE)
        # The lookup does blocking HTTP; keep it off the loader's event loop.
        return await asyncio.get_running_loop().run_in_executor(None, self.hltb.get, int(appid), str(name))

    async def get_settings(self) -> dict:
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except Exception as e:
            decky.logger.error(f"Could not read settings: {e}")
            return {}

    async def set_settings(self, settings: dict) -> bool:
        try:
            os.makedirs(decky.DECKY_PLUGIN_SETTINGS_DIR, exist_ok=True)
            tmp = SETTINGS_FILE + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)
            os.replace(tmp, SETTINGS_FILE)
            return True
        except Exception as e:
            decky.logger.error(f"Could not save settings: {e}")
            return False

    async def _main(self):
        decky.logger.info("PS5 Dashboard loaded")

    async def _unload(self):
        decky.logger.info("PS5 Dashboard unloaded")

````

## package-lock.json

Ruta: `MenuVersion2/decky-ps5-dashboard/package-lock.json` · Bytes: 72679 · SHA-256: `2dfedf550109d7bf2d6891ea507b20775f7870fcabdc86fac1367ae260cc7471`

````text
{
  "name": "ps5-dashboard",
  "version": "1.10.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "ps5-dashboard",
      "version": "1.10.0",
      "license": "MIT",
      "dependencies": {
        "@decky/api": "^1.1.3",
        "react-icons": "^5.3.0",
        "tslib": "^2.7.0"
      },
      "devDependencies": {
        "@decky/rollup": "^1.0.2",
        "@decky/ui": "^4.16.0",
        "@types/react": "19.1.1",
        "@types/react-dom": "19.1.1",
        "react": "19.1.1",
        "rollup": "^4.53.3",
        "typescript": "^5.6.2"
      }
    },
    "node_modules/@decky/api": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/@decky/api/-/api-1.1.3.tgz",
      "integrity": "sha512-XsPCZxfxk5I1UtylIUN3qaWQI31siQbKfbLIskkI5innEatY1m4NQqBv/6hwPaO9mKMbdqYpnh5PSJDeMEOOBA==",
      "license": "LGPL-2.1"
    },
    "node_modules/@decky/rollup": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/@decky/rollup/-/rollup-1.0.2.tgz",
      "integrity": "sha512-ixuHH3msw156ACbgWZi4hgccdzDBIuqYGOVja8sLX4lHFgaWUKji1vomDi7Dk1CamgjmKt+Dqf75Pezv2FB6Bw==",
      "dev": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "@rollup/plugin-commonjs": "^26.0.1",
        "@rollup/plugin-json": "^6.1.0",
        "@rollup/plugin-node-resolve": "^15.2.3",
        "@rollup/plugin-replace": "^5.0.7",
        "@rollup/plugin-typescript": "^11.1.6",
        "merge-anything": "^6.0.2",
        "rollup": "^4.18.0",
        "rollup-plugin-delete": "^2.0.0",
        "rollup-plugin-external-globals": "^0.11.0",
        "rollup-plugin-import-assets": "^1.1.1",
        "tslib": "^2.6.3",
        "typescript": "^5.5.3"
      }
    },
    "node_modules/@decky/ui": {
      "version": "4.16.0",
      "resolved": "https://registry.npmjs.org/@decky/ui/-/ui-4.16.0.tgz",
      "integrity": "sha512-yvgwpDSr2tdPrpR1BPc8RvCDtmGbZ/pTULxm6jvwEoWhgxk8v1K0Y3ilpAd+aBYrDQa2fZbnqkKS6ZZTwsmz6A==",
      "dev": true,
      "license": "LGPL-2.1"
    },
    "node_modules/@isaacs/cliui": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
      "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "string-width": "^5.1.2",
        "string-width-cjs": "npm:string-width@^4.2.0",
        "strip-ansi": "^7.0.1",
        "strip-ansi-cjs": "npm:strip-ansi@^6.0.1",
        "wrap-ansi": "^8.1.0",
        "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.6.0.tgz",
      "integrity": "sha512-T7jf+5zgsZHwNJ4lvQ7/aezbyk0nNX+zJVWpmHA7VYsEx7a7qr5Rg5IbtJFqkgze5Y2sruq1RUY8Q837Od7iFw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@napi-rs/lzma-linux-x64-gnu": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/@napi-rs/lzma-linux-x64-gnu/-/lzma-linux-x64-gnu-1.5.1.tgz",
      "integrity": "sha512-oTXEIha4SsuXdTA4Iyskj0kpdx2yVXdhd75c2v3xGrHFfVMsbhTPZU/nMPL4sWKo4pBHm3aucLaqGlF696dTyQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^22.20 || ^24.12 || >=25"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@pkgjs/parseargs": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/@pkgjs/parseargs/-/parseargs-0.11.0.tgz",
      "integrity": "sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@rollup/plugin-commonjs": {
      "version": "26.0.3",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-commonjs/-/plugin-commonjs-26.0.3.tgz",
      "integrity": "sha512-2BJcolt43MY+y5Tz47djHkodCC3c1VKVrBDKpVqHKpQ9z9S158kCCqB8NF6/gzxLdNlYW9abB3Ibh+kOWLp8KQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.0.1",
        "commondir": "^1.0.1",
        "estree-walker": "^2.0.2",
        "glob": "^10.4.1",
        "is-reference": "1.2.1",
        "magic-string": "^0.30.3"
      },
      "engines": {
        "node": ">=16.0.0 || 14 >= 14.17"
      },
      "peerDependencies": {
        "rollup": "^2.68.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/plugin-json": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-json/-/plugin-json-6.1.0.tgz",
      "integrity": "sha512-EGI2te5ENk1coGeADSIwZ7G2Q8CJS2sF120T7jLw4xFw9n7wIOXHo+kIYRAoVpJAN+kmqZSoO3Fp4JtoNF4ReA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.1.0"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/plugin-node-resolve": {
      "version": "15.3.1",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-node-resolve/-/plugin-node-resolve-15.3.1.tgz",
      "integrity": "sha512-tgg6b91pAybXHJQMAAwW9VuWBO6Thi+q7BCNARLwSqlmsHz0XYURtGvh/AuwSADXSI4h/2uHbs7s4FzlZDGSGA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.0.1",
        "@types/resolve": "1.20.2",
        "deepmerge": "^4.2.2",
        "is-module": "^1.0.0",
        "resolve": "^1.22.1"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^2.78.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/plugin-replace": {
      "version": "5.0.7",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-replace/-/plugin-replace-5.0.7.tgz",
      "integrity": "sha512-PqxSfuorkHz/SPpyngLyg5GCEkOcee9M1bkxiVDr41Pd61mqP1PLOoDPbpl44SB2mQGKwV/In74gqQmGITOhEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.0.1",
        "magic-string": "^0.30.3"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/plugin-typescript": {
      "version": "11.1.6",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-typescript/-/plugin-typescript-11.1.6.tgz",
      "integrity": "sha512-R92yOmIACgYdJ7dJ97p4K69I8gg6IEHt8M7dUBxN3W6nrO8uUxX5ixl0yU/N3aZTi8WhPuICvOHXQvF6FaykAA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.1.0",
        "resolve": "^1.22.1"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^2.14.0||^3.0.0||^4.0.0",
        "tslib": "*",
        "typescript": ">=3.7.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        },
        "tslib": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/pluginutils": {
      "version": "5.5.1",
      "resolved": "https://registry.npmjs.org/@rollup/pluginutils/-/pluginutils-5.5.1.tgz",
      "integrity": "sha512-P9ZvnfouRu4MSC+ilERaw6FmZs8zqKhpHxEs4aGDGWQAMzQGXnhvCSvoNwokfNvdt7t3Y5Y4p6gStQgezeIqug==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "^1.0.0",
        "estree-walker": "^2.0.2",
        "picomatch": "^4.0.2"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/rollup-android-arm-eabi": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.65.0.tgz",
      "integrity": "sha512-t2AnVba25baFdq7gczzS13JyVcdubLVbFX1X04mxrggDrTQPUXNv3XM0k9H1hr5tqvg7AVvtQ720QHAj0iYqhg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-android-arm64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.65.0.tgz",
      "integrity": "sha512-dNONUaEwPGhl/nuO2KV8VABWlcjYyU6KtZGN8dQv5OS5JU7JSCxPijVNKXbRJd0iuTzTiJ4TjPt/4bbvDRNiMQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-darwin-arm64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.65.0.tgz",
      "integrity": "sha512-zWQqUH+9zavr2Bxuzfpuv2SIF3X31cr58TvSQC9o1GhpOvkqRwr60GkZdQcudyT/BEgdpdSafjgd2I13MbTL7g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-darwin-x64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.65.0.tgz",
      "integrity": "sha512-RQYreBFWtO4//hIuOaZkYUnF/lPU4lz35dveDimDshWCJvVisVtJ/shmT9bkXK8wFJY+FJF89X6F3Cq1qI3LCw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-arm64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-arm64/-/rollup-freebsd-arm64-4.65.0.tgz",
      "integrity": "sha512-A0NfMj6Cuh/9BE5k3awJKv6HoxFVXIcLAb6SZqAMoxUHPA1ZNNK4RsGuUPD/vL7nEAm9LG+ZzXWWTrnC0XtkpA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-x64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-x64/-/rollup-freebsd-x64-4.65.0.tgz",
      "integrity": "sha512-BI6/H7q3aP0I7S7GOrjyxTjgEJlSnovXE38+bdxBpuKN6z+d//uF+T+VQ3Q7ltJL/71p17ufartARX9Ja5gOGQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.65.0.tgz",
      "integrity": "sha512-W1vUprf09RWaVWnsFP1vlUkEWJzTZlpObOEAYZXt9Fq0UVAOYEkeGr7wBX7McKqqIQskXdBnpiOMgwPujordgA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-musleabihf": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-musleabihf/-/rollup-linux-arm-musleabihf-4.65.0.tgz",
      "integrity": "sha512-s8QTcZWgrl9haFzEGIqyE5BWyo89pFDGLMBFZ752WYxk8DJwNU/O1X6pZgPw829d9/sm6CCHyrMP3aurt76p1Q==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.65.0.tgz",
      "integrity": "sha512-ke1f6dLRzkqveyjjF2fkEwQYZvxHtNNwjegY8nJrwcO0Bdqr8CzFO/pKE0Bns13cx0qz2Ba2Y0Hs3dSwMdnHxA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-musl": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.65.0.tgz",
      "integrity": "sha512-926SMeUcy4y18Rz/w2aJiUKOnyAnm6czg72bXkQEaeemsll+Wr0hnsjb2BGRpHvWgwAMYy5ACJCotbvfLCfj0A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-gnu/-/rollup-linux-loong64-gnu-4.65.0.tgz",
      "integrity": "sha512-6T7JNRP1hc4hqF2dUsEoVLOt9K8tmODoCLldtQRYnrddGGQY8Gqe2pM/qMMUo7EMowpP7oa2N95k0/8sYK/ipw==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-musl": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-musl/-/rollup-linux-loong64-musl-4.65.0.tgz",
      "integrity": "sha512-SImGFl1Je5kpyAgOCPONVT7h6ASV8mAUwGRjY7eZvVjPg//PfHOXgI+P241RF/+HqsA4PP3qD527ysWFKNQyhQ==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-gnu/-/rollup-linux-ppc64-gnu-4.65.0.tgz",
      "integrity": "sha512-XeDTbmPF1Yu5asfXGPrMkWoxTDhgryQbmw5Q1+R582O51VNCk23J6f2pDrsAp5YkneBVBwtExx6ZGOb9D2aQ6A==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-musl": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-musl/-/rollup-linux-ppc64-musl-4.65.0.tgz",
      "integrity": "sha512-VS55JUI/1nsljmV/jfqNkLZXFw8uMO8nNlfoHmSevNf6fO3neuhyDvx9dv3c/Ytt8r/431SL8Qax1dpYvOMZTg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.65.0.tgz",
      "integrity": "sha512-Vblw84TbX7RS4la1Y4+yQ7aore/oSyaNtFbppuBr5Vs/4LfBeXKq9dIfoExw6zOvRERqd2rRAjnZRaMhH/0x5w==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-musl": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-musl/-/rollup-linux-riscv64-musl-4.65.0.tgz",
      "integrity": "sha512-7+gHjtONvKgwR9InTKFaLq53f6YzBJkgeMRBENdWTsQr+spahGqQm8HF5aXpq8i4JaRrOqYyv6Zn1WltDTxaZQ==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-s390x-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-s390x-gnu/-/rollup-linux-s390x-gnu-4.65.0.tgz",
      "integrity": "sha512-KvNDC0J6s4vVHhtJ6KrDXU0Er0au/hmRIBq/+1maCV8TseGupeKizq0bWcrbp2HE1T8xoknvN0Q/KZ/YF0qX3w==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.65.0.tgz",
      "integrity": "sha512-GExdD15WPvu/x/drELjVam7vX8EsPgvTMOa/iJL/p/4m/oOqzbb7JXZg8fXR4hlXtg/sF2zyTZ3bR0AEtEMlhQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-musl": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.65.0.tgz",
      "integrity": "sha512-8sT9PemIZfIMED4Vd4KGoOXVDj5CMSWNcGdbheRUx9TYS03yOWdT2Q0lXPyEyNBB9YTilwewIQKNIBk6Nxi0Kg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-openbsd-x64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openbsd-x64/-/rollup-openbsd-x64-4.65.0.tgz",
      "integrity": "sha512-pO6Ehi0jo5yE0R6PltKhJhv9mlIiyzBJk5N5NUF2OF6xtVKI+1bdXxj/rb0jGXy3hck1ELVT0QPY3tzkAm360w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ]
    },
    "node_modules/@rollup/rollup-openharmony-arm64": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openharmony-arm64/-/rollup-openharmony-arm64-4.65.0.tgz",
      "integrity": "sha512-vo7N3/+cjjPDYr8vtxC+qSNgWa9sDvJ7g8N8R5SWqFY4WiNH1ULcAU70SKVyHeiIZOYYwNP9pTipmhN5sl1NPw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ]
    },
    "node_modules/@rollup/rollup-win32-arm64-msvc": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.65.0.tgz",
      "integrity": "sha512-ArwvgFAbjKcDM7qqotZ4OVYf+UMT9xH2YzkCzK4+AuZSDihMlz1Ekoe4INwBVXzn2mnJzuIYOcSx07iTBijGRQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-ia32-msvc": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.65.0.tgz",
      "integrity": "sha512-QGMmK4/cxKE/36FoLMSHQBCyymv/eFTnsCvvsBF0rgmOvVbvX78VWZRerL3dHa77f4pM6Xcc2iGDhJ10w/svKQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-gnu": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-gnu/-/rollup-win32-x64-gnu-4.65.0.tgz",
      "integrity": "sha512-XfKYFWHIPs4HPODIMsGF1IKlS3H1e3WokUZIgpmn4+uNnZBlnRDDHEylNyazbQXwhMKZre68OjtRYbKqb5+j8w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-msvc": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.65.0.tgz",
      "integrity": "sha512-wPWi++K4Bs1VR4XihOhfGi4IGX6Cub7FlerTf8X2v+2BtDHddgSqWCXwGD+h2yAe4/niIhNDwAltioOC+wEogQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@types/estree": {
      "version": "1.0.9",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz",
      "integrity": "sha512-GhdPgy1el4/ImP05X05Uw4cw2/M93BCUmnEvWZNStlCzEKME4Fkk+YpoA5OiHNQmoS7Cafb8Xa3Pya8m1Qrzeg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "19.1.1",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.1.1.tgz",
      "integrity": "sha512-ePapxDL7qrgqSF67s0h9m412d9DbXyC1n59O2st+9rjuuamWsZuD2w55rqY12CbzsZ7uVXb5Nw0gEp9Z8MMutQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "csstype": "^3.0.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "19.1.1",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-19.1.1.tgz",
      "integrity": "sha512-jFf/woGTVTjUJsl2O7hcopJ1r0upqoq/vIOoCj0yLh3RIXxWcljlpuZ+vEBRXsymD1jhfeJrlyTy/S1UW+4y1w==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^19.0.0"
      }
    },
    "node_modules/@types/resolve": {
      "version": "1.20.2",
      "resolved": "https://registry.npmjs.org/@types/resolve/-/resolve-1.20.2.tgz",
      "integrity": "sha512-60BCwRFOZCQhDncwQdxxeOEEkbc5dIMccYLwbxsS4TUNeVECQ/pBJ0j09mrHOl/JJvpRPGwO9SvE4nR2Nb/a4Q==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/aggregate-error": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/aggregate-error/-/aggregate-error-3.1.0.tgz",
      "integrity": "sha512-4I7Td01quW/RpocfNayFdFVk1qSuoh0E7JrbRJ16nH01HhKFQ88INq9Sd+nd72zqRySlr9BmDA8xlEJ6vJMrYA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "clean-stack": "^2.0.0",
        "indent-string": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-regex": {
      "version": "6.4.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.4.0.tgz",
      "integrity": "sha512-KzTVk2tCWAHtYrvvvaP8bJKJq2pVinhLcGEQdtLIYPbmNGNyYe8QwNaTUYQp2J7/vIsUKt5QCqAfUkYyG9DkOw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/ansi-styles": {
      "version": "6.2.3",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.3.tgz",
      "integrity": "sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/array-union": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/array-union/-/array-union-2.1.0.tgz",
      "integrity": "sha512-HGyxoOTYUyCM6stUe6EJgnd4EoewAI7zMdfqO+kGjnlZmBDz/cR5pf8r/cR4Wq60sL/p0IkcjUEEPwS3GFrIyw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/brace-expansion": {
      "version": "2.1.7",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.1.7.tgz",
      "integrity": "sha512-uZbew1NqdmPDTMJ8ah1y+b+9QEJrfkXFk3RcTQw3X0jW/xRUvFKsg1CfQdSYGdTbXZWExtU3J3ccxtnfw1Fi0g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/clean-stack": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz",
      "integrity": "sha512-4diC9HaTE+KRAMWhDhrGOECgWZxoevMc5TlkObMqNSsVU62PYzXZ/SMTjzyGAFF1YusgxGcSWTEXBhp0CPwQ1A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/commondir": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz",
      "integrity": "sha512-W9pAhw0ja1Edb5GVdIF1mjZw/ASI0AlShXM83UUGe2DVr5TdAPEA1OA8m/g8zWp9x6On7gqufY+FatDbC3MDQg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/deepmerge": {
      "version": "4.3.1",
      "resolved": "https://registry.npmjs.org/deepmerge/-/deepmerge-4.3.1.tgz",
      "integrity": "sha512-3sUqbMEc77XqpdNO7FRyRog+eW3ph+GYCbj+rK+uYyRMuwsVy0rMiVtPn+QJlKFvWP/1PYpapqYn0Me2knFn+A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/del": {
      "version": "6.1.1",
      "resolved": "https://registry.npmjs.org/del/-/del-6.1.1.tgz",
      "integrity": "sha512-ua8BhapfP0JUJKC/zV9yHHDW/rDoDxP4Zhn3AkA6/xT6gY7jYXJiaeyBZznYVujhZZET+UgcbZiQ7sN3WqcImg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "globby": "^11.0.1",
        "graceful-fs": "^4.2.4",
        "is-glob": "^4.0.1",
        "is-path-cwd": "^2.2.0",
        "is-path-inside": "^3.0.2",
        "p-map": "^4.0.0",
        "rimraf": "^3.0.2",
        "slash": "^3.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/dir-glob": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/dir-glob/-/dir-glob-3.0.1.tgz",
      "integrity": "sha512-WkrWp9GR4KXfKGYzOLmTuGVi1UWFfws377n9cc55/tb6DuqyF6pcQ5AbiHEshaDpY9v6oaSr2XCDidGmMwdzIA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "path-type": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/eastasianwidth": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/eastasianwidth/-/eastasianwidth-0.2.0.tgz",
      "integrity": "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/emoji-regex": {
      "version": "9.2.2",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz",
      "integrity": "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/estree-walker": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-2.0.2.tgz",
      "integrity": "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fastq": {
      "version": "1.20.3",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.20.3.tgz",
      "integrity": "sha512-XKv5nnLs6nLF71NgiKJLIZFLkPyIEuOselLG7ujZnGrRfQK8HpvY+WqKhAJUAdLomwVHErVS4LfxFlPq0/FTAw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/foreground-child": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/foreground-child/-/foreground-child-3.3.1.tgz",
      "integrity": "sha512-gIXjKqtFuWEgzFRJA9WCQeSJLZDjgJUOMCMzxtvFq/37KojM1BFGufqsCy0r4qSQmYLsZYMeyRqzIWOMup03sw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "cross-spawn": "^7.0.6",
        "signal-exit": "^4.0.1"
      },
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/glob": {
      "version": "10.5.0",
      "resolved": "https://registry.npmjs.org/glob/-/glob-10.5.0.tgz",
      "integrity": "sha512-DfXN8DfhJ7NH3Oe7cFmu3NCu1wKbkReJ8TorzSAFbSKrlNaQSKfIzqYqVY8zlbs2NLBbWpRiU52GX2PbaBVNkg==",
      "deprecated": "Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "foreground-child": "^3.1.0",
        "jackspeak": "^3.1.2",
        "minimatch": "^9.0.4",
        "minipass": "^7.1.2",
        "package-json-from-dist": "^1.0.0",
        "path-scurry": "^1.11.1"
      },
      "bin": {
        "glob": "dist/esm/bin.mjs"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/globby": {
      "version": "11.1.0",
      "resolved": "https://registry.npmjs.org/globby/-/globby-11.1.0.tgz",
      "integrity": "sha512-jhIXaOzy1sb8IyocaruWSn1TjmnBVs8Ayhcy83rmxNJ8q2uWKCAj3CnJY+KpGSXCueAPc0i05kVvVKtP1t9S3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "array-union": "^2.1.0",
        "dir-glob": "^3.0.1",
        "fast-glob": "^3.2.9",
        "ignore": "^5.2.0",
        "merge2": "^1.4.1",
        "slash": "^3.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/graceful-fs": {
      "version": "4.2.11",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
      "integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/hasown": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz",
      "integrity": "sha512-T2UbfbBEF32wiepXIsMlTW9+dDYC6wMh/t/vYA4tuOMKqWz/n3vr1NFSxQiyP+zk2mXsoMA/i/7qV6LKut1t1A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ignore": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz",
      "integrity": "sha512-hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 4"
      }
    },
    "node_modules/indent-string": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz",
      "integrity": "sha512-EdDDZu4A2OyIK7Lr/2zG+w5jmbuk1DVBnEwREQvBzspBJkCEbRa8GxU1lghYcaGJCnRWibjDXlq779X1/y5xwg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/inflight": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
      "integrity": "sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==",
      "deprecated": "This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "once": "^1.3.0",
        "wrappy": "1"
      }
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/is-core-module": {
      "version": "2.17.0",
      "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.17.0.tgz",
      "integrity": "sha512-J/vG0zBCbIKOQFfufSwyXdMrsohyJIUNkrnmo6WZGzoM7tr/lsbfW5b2BvisL6zsyMzK9UxV9L6c7AoFbyXHOA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hasown": "^2.0.4"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
      "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-module": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-module/-/is-module-1.0.0.tgz",
      "integrity": "sha512-51ypPSPCoTEIN9dy5Oy+h4pShgJmPCygKfyRCISBI+JoWT/2oJvK8QPxmwv7b/p239jXrm9M1mlQbyKJ5A152g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/is-path-cwd": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/is-path-cwd/-/is-path-cwd-2.2.0.tgz",
      "integrity": "sha512-w942bTcih8fdJPJmQHFzkS76NEP8Kzzvmw92cXsazb8intwLqPibPPdXf4ANdKV3rYMuuQYGIWtvz9JilB3NFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/is-path-inside": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/is-path-inside/-/is-path-inside-3.0.3.tgz",
      "integrity": "sha512-Fd4gABb+ycGAmKou8eMftCupSir5lRxqf4aD/vd0cD2qc4HL07OjCeuHMr8Ro4CoMaeCKDB0/ECBOVWjTwUvPQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-reference": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/is-reference/-/is-reference-1.2.1.tgz",
      "integrity": "sha512-U82MsXXiFIrjCK4otLT+o2NA2Cd2g5MLoOVXUZjIOhLurrRxpEXzI8O0KZHr3IjLvlAH1kTPYSuqer5T9ZVBKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "*"
      }
    },
    "node_modules/is-what": {
      "version": "5.5.7",
      "resolved": "https://registry.npmjs.org/is-what/-/is-what-5.5.7.tgz",
      "integrity": "sha512-b8A+OE0RcNFy/+qmts8Uv+vumkUZHwIa80YMZBfh6+b75Oq2J8qR3v+/F5vKq4TNNiurrgrE7+XsOa8+1y4lYw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/mesqueeb"
      }
    },
    "node_modules/isexe": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
      "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/jackspeak": {
      "version": "3.4.3",
      "resolved": "https://registry.npmjs.org/jackspeak/-/jackspeak-3.4.3.tgz",
      "integrity": "sha512-OGlZQpz2yfahA/Rd1Y8Cd9SIEsqvXkLVoSw/cgwhnhFMDbsQFeZYoJJ7bIZBS9BcamUW96asq/npPWugM+RQBw==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "@isaacs/cliui": "^8.0.2"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      },
      "optionalDependencies": {
        "@pkgjs/parseargs": "^0.11.0"
      }
    },
    "node_modules/lru-cache": {
      "version": "10.4.3",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-10.4.3.tgz",
      "integrity": "sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/magic-string": {
      "version": "0.30.21",
      "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.21.tgz",
      "integrity": "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.5"
      }
    },
    "node_modules/merge-anything": {
      "version": "6.0.9",
      "resolved": "https://registry.npmjs.org/merge-anything/-/merge-anything-6.0.9.tgz",
      "integrity": "sha512-Mr75kWbk3zeccaJ/mFYYCl7RINFbWIvi4pqGKQ7CAlpWw48aHWxwg19HmEIWpad0Z5+vbSEhMxQoyO1oms0ovQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-what": "^5.5.7"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/mesqueeb"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/micromatch/node_modules/picomatch": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.2.tgz",
      "integrity": "sha512-V7+vQEJ06Z+c5tSye8S+nHUfI51xoXIXjHQ99cQtKUkQqqO1kO/KCJUfZXuB47h/YBlDhah2H3hdUGXn8ie0oA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/minimatch": {
      "version": "9.0.9",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-9.0.9.tgz",
      "integrity": "sha512-OBwBN9AL4dqmETlpS2zasx+vTeWclWzkblfZk7KTA5j3jeOONz/tRCnZomUyvNg83wL5Zv9Ss6HMJXAgL8R2Yg==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "brace-expansion": "^2.0.2"
      },
      "engines": {
        "node": ">=16 || 14 >=14.17"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/minipass": {
      "version": "7.1.3",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-7.1.3.tgz",
      "integrity": "sha512-tEBHqDnIoM/1rXME1zgka9g6Q2lcoCkxHLuc7ODJ5BxbP5d4c2Z5cGgtXAku59200Cx7diuHTOYfSBD8n6mm8A==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "engines": {
        "node": ">=16 || 14 >=14.17"
      }
    },
    "node_modules/once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "wrappy": "1"
      }
    },
    "node_modules/p-map": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/p-map/-/p-map-4.0.0.tgz",
      "integrity": "sha512-/bjOqmgETBYB5BoEeGVea8dmvHb2m9GLy1E9W43yeyfP6QQCZGFNa+XRceJEuDB6zqr+gKpIAmlLebMpykw/MQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "aggregate-error": "^3.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/package-json-from-dist": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/package-json-from-dist/-/package-json-from-dist-1.0.1.tgz",
      "integrity": "sha512-UEZIS3/by4OC8vL3P2dTXRETpebLI2NiI5vIrjaD/5UtrkFX/tNbwjTSRAGC/+7CAo2pIcBaRgWmcBBHcsaCIw==",
      "dev": true,
      "license": "BlueOak-1.0.0"
    },
    "node_modules/path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/path-key": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
      "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/path-parse": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
      "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/path-scurry": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/path-scurry/-/path-scurry-1.11.1.tgz",
      "integrity": "sha512-Xa4Nw17FS9ApQFJ9umLiJS4orGjm7ZzwUrwamcGQuHSzDyth9boKDaycYdDcZDuqYATXw4HFXgaqWTctW/v1HA==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "lru-cache": "^10.2.0",
        "minipass": "^5.0.0 || ^6.0.2 || ^7.0.0"
      },
      "engines": {
        "node": ">=16 || 14 >=14.18"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/path-type": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz",
      "integrity": "sha512-gDKb8aZMDeD/tZWs9P6+q0J9Mwkdl6xMV8TjnGP3qJVJ06bdMgkbBlLU8IdfOsIsFz2BW1rNVT3XuNEl8zPAvw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/picomatch": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.7.tgz",
      "integrity": "sha512-qcJu88Q2IWqJsDD529JKMdwGm/dvInW4HvQnRwiH9JtihJvzGOscDtHE3x1pBKeUOTysQ8kVmLnJ2kJu7yhcGA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/react": {
      "version": "19.1.1",
      "resolved": "https://registry.npmjs.org/react/-/react-19.1.1.tgz",
      "integrity": "sha512-w8nqGImo45dmMIfljjMwOGtbmC/mk4CMYhWIicdSflH91J9TyCyczcPFXJzrZ/ZXcgGRFeP6BU0BEJTw6tZdfQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-icons": {
      "version": "5.7.0",
      "resolved": "https://registry.npmjs.org/react-icons/-/react-icons-5.7.0.tgz",
      "integrity": "sha512-LBLy340Rzqy6+/yVhZKT3B/QpP1BZaesGqasf09HPOBzRarcDIFH0WwXlXQfE7q7ipxK4MSiC5DIBWURCny6fw==",
      "license": "MIT",
      "peerDependencies": {
        "react": "*"
      }
    },
    "node_modules/resolve": {
      "version": "1.22.13",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.13.tgz",
      "integrity": "sha512-Dj/cW9zBV2aRj6XzCxuGIs3ESZKv02jixne3q6jFZYZ3/Tg09gHHviSMDL4kObh9pqSahdRHEnDoaP2gn8YLhA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "is-core-module": "^2.17.0",
        "path-parse": "^1.0.7",
        "supports-preserve-symlinks-flag": "^1.0.0"
      },
      "bin": {
        "resolve": "bin/resolve"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "iojs": ">=1.0.0",
        "node": ">=0.10.0"
      }
    },
    "node_modules/rimraf": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz",
      "integrity": "sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==",
      "deprecated": "Rimraf versions prior to v4 are no longer supported",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "glob": "^7.1.3"
      },
      "bin": {
        "rimraf": "bin.js"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/rimraf/node_modules/brace-expansion": {
      "version": "1.1.21",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.21.tgz",
      "integrity": "sha512-9zeA+KLZNNzglF2TPKRQEDyx6Yby7daAkuy8MiPzpXPsYDWi/DRM8jmwUDxokQjYqBpv5DgPiwD4h4ZZSy1Ujw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/rimraf/node_modules/glob": {
      "version": "7.2.3",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.2.3.tgz",
      "integrity": "sha512-nFR0zLpU2YCaRxwoCJvL6UvCH2JFyFVIvwTLsIf21AuHlMskA1hhTdk+LlYJtOlYt9v6dvszD2BGRqBL+iQK9Q==",
      "deprecated": "Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "fs.realpath": "^1.0.0",
        "inflight": "^1.0.4",
        "inherits": "2",
        "minimatch": "^3.1.1",
        "once": "^1.3.0",
        "path-is-absolute": "^1.0.0"
      },
      "engines": {
        "node": "*"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/rimraf/node_modules/minimatch": {
      "version": "3.1.5",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.5.tgz",
      "integrity": "sha512-VgjWUsnnT6n+NUk6eZq77zeFdpW2LWDzP6zFGrCbHXiYNul5Dzqk2HHQ5uFH2DNW5Xbp8+jVzaeNt94ssEEl4w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "brace-expansion": "^1.1.7"
      },
      "engines": {
        "node": "*"
      }
    },
    "node_modules/rollup": {
      "version": "4.65.0",
      "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.65.0.tgz",
      "integrity": "sha512-QVCvQUTGDN6JRwi3jVGCY3H4aTHvi9rX0LyoBMkGUvdh/Z6O51CzcLz85BWZaTCDGhl6ySGqYZs+xI1jmPqGcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "1.0.9"
      },
      "bin": {
        "rollup": "dist/bin/rollup"
      },
      "engines": {
        "node": ">=18.0.0",
        "npm": ">=8.0.0"
      },
      "optionalDependencies": {
        "@napi-rs/lzma-linux-x64-gnu": "1.5.1",
        "@rollup/rollup-android-arm-eabi": "4.65.0",
        "@rollup/rollup-android-arm64": "4.65.0",
        "@rollup/rollup-darwin-arm64": "4.65.0",
        "@rollup/rollup-darwin-x64": "4.65.0",
        "@rollup/rollup-freebsd-arm64": "4.65.0",
        "@rollup/rollup-freebsd-x64": "4.65.0",
        "@rollup/rollup-linux-arm-gnueabihf": "4.65.0",
        "@rollup/rollup-linux-arm-musleabihf": "4.65.0",
        "@rollup/rollup-linux-arm64-gnu": "4.65.0",
        "@rollup/rollup-linux-arm64-musl": "4.65.0",
        "@rollup/rollup-linux-loong64-gnu": "4.65.0",
        "@rollup/rollup-linux-loong64-musl": "4.65.0",
        "@rollup/rollup-linux-ppc64-gnu": "4.65.0",
        "@rollup/rollup-linux-ppc64-musl": "4.65.0",
        "@rollup/rollup-linux-riscv64-gnu": "4.65.0",
        "@rollup/rollup-linux-riscv64-musl": "4.65.0",
        "@rollup/rollup-linux-s390x-gnu": "4.65.0",
        "@rollup/rollup-linux-x64-gnu": "4.65.0",
        "@rollup/rollup-linux-x64-musl": "4.65.0",
        "@rollup/rollup-openbsd-x64": "4.65.0",
        "@rollup/rollup-openharmony-arm64": "4.65.0",
        "@rollup/rollup-win32-arm64-msvc": "4.65.0",
        "@rollup/rollup-win32-ia32-msvc": "4.65.0",
        "@rollup/rollup-win32-x64-gnu": "4.65.0",
        "@rollup/rollup-win32-x64-msvc": "4.65.0",
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/rollup-plugin-delete": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/rollup-plugin-delete/-/rollup-plugin-delete-2.2.0.tgz",
      "integrity": "sha512-REKtDKWvjZlbrWpPvM9X/fadCs3E9I9ge27AK8G0e4bXwSLeABAAwtjiI1u3ihqZxk6mJeB2IVeSbH4DtOcw7A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "del": "^6.1.1"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "rollup": "*"
      }
    },
    "node_modules/rollup-plugin-external-globals": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/rollup-plugin-external-globals/-/rollup-plugin-external-globals-0.11.0.tgz",
      "integrity": "sha512-LR+sH2WkgWMPxsA5o5rT7uW7BeWXSeygLe60QQi9qoN/ufaCuHDaVOIbndIkqDPnZt/wZugJh5DCzkZFdSWlLQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.1.0",
        "estree-walker": "^3.0.3",
        "is-reference": "^3.0.2",
        "magic-string": "^0.30.10"
      },
      "peerDependencies": {
        "rollup": "^2.25.0 || ^3.3.0 || ^4.1.4"
      }
    },
    "node_modules/rollup-plugin-external-globals/node_modules/estree-walker": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-3.0.3.tgz",
      "integrity": "sha512-7RUKfXgSMMkzt6ZuXmqapOurLGPPfgj6l9uRZ7lRGolvk0y2yocc35LdcxKC5PQZdn2DMqioAQ2NoWcrTKmm6g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "^1.0.0"
      }
    },
    "node_modules/rollup-plugin-external-globals/node_modules/is-reference": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/is-reference/-/is-reference-3.0.3.tgz",
      "integrity": "sha512-ixkJoqQvAP88E6wLydLGGqCJsrFUnqoH6HnaczB8XmDH1oaWU+xxdptvikTgaEhtZ53Ky6YXiBuUI2WXLMCwjw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "^1.0.6"
      }
    },
    "node_modules/rollup-plugin-import-assets": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/rollup-plugin-import-assets/-/rollup-plugin-import-assets-1.1.1.tgz",
      "integrity": "sha512-u5zJwOjguTf2N+wETq2weNKGvNkuVc1UX/fPgg215p5xPvGOaI6/BTc024E9brvFjSQTfIYqgvwogQdipknu1g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "rollup-pluginutils": "^2.7.1",
        "url-join": "^4.0.1"
      },
      "peerDependencies": {
        "rollup": ">=1.9.0"
      }
    },
    "node_modules/rollup-pluginutils": {
      "version": "2.8.2",
      "resolved": "https://registry.npmjs.org/rollup-pluginutils/-/rollup-pluginutils-2.8.2.tgz",
      "integrity": "sha512-EEp9NhnUkwY8aif6bxgovPHMoMoNr2FulJziTndpt5H9RdwC47GSGuII9XxpSdzVGM0GWrNPHV6ie1LTNJPaLQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "estree-walker": "^0.6.1"
      }
    },
    "node_modules/rollup-pluginutils/node_modules/estree-walker": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-0.6.1.tgz",
      "integrity": "sha512-SqmZANLWS0mnatqbSfRP5g8OXZC12Fgg1IwNtLsyHDzJizORW4khDfjPqJZsemPWBB2uqykUah5YpQ6epsqC/w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "queue-microtask": "^1.2.2"
      }
    },
    "node_modules/shebang-command": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
      "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "shebang-regex": "^3.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/shebang-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
      "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/signal-exit": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-4.1.0.tgz",
      "integrity": "sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/slash": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/slash/-/slash-3.0.0.tgz",
      "integrity": "sha512-g9Q1haeby36OSStwb4ntCGGGaKsaVSjQ68fBxoQcutl5fS1vuY18H3wSt3jFyFtrkx+Kz0V1G85A4MyAdDMi2Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/string-width": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-5.1.2.tgz",
      "integrity": "sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eastasianwidth": "^0.2.0",
        "emoji-regex": "^9.2.2",
        "strip-ansi": "^7.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/string-width-cjs": {
      "name": "string-width",
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/string-width-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/string-width-cjs/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/string-width-cjs/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.2.0.tgz",
      "integrity": "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^6.2.2"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/strip-ansi?sponsor=1"
      }
    },
    "node_modules/strip-ansi-cjs": {
      "name": "strip-ansi",
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/supports-preserve-symlinks-flag": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
      "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD"
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/url-join": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/url-join/-/url-join-4.0.1.tgz",
      "integrity": "sha512-jk1+QP6ZJqyOiuEI9AEWQfju/nB2Pw466kbA0LEZljHwKeMgd9WrAEgEGxjPDD2+TNbbb37rTyhEfrCXfuKXnA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/which": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
      "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "isexe": "^2.0.0"
      },
      "bin": {
        "node-which": "bin/node-which"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/wrap-ansi": {
      "version": "8.1.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-8.1.0.tgz",
      "integrity": "sha512-si7QWI6zUMq56bESFvagtmzMdGOtoxfR+Sez11Mobfc7tm+VkUckk9bW2UeffTGVUbOksxmSw0AA2gs8g71NCQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^6.1.0",
        "string-width": "^5.0.1",
        "strip-ansi": "^7.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/wrap-ansi-cjs": {
      "name": "wrap-ansi",
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
      "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.0.0",
        "string-width": "^4.1.0",
        "strip-ansi": "^6.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/wrap-ansi-cjs/node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "dev": true,
      "license": "ISC"
    }
  }
}

````

## package.json

Ruta: `MenuVersion2/decky-ps5-dashboard/package.json` · Bytes: 739 · SHA-256: `ced8a1eb902ffaaeb0cf3a96c3e61f5590702911e8e84081a74651cf63af22a1`

````text
{
  "name": "ps5-dashboard",
  "version": "1.10.0",
  "description": "Makes SteamOS Game Mode look and feel like the PlayStation 5 home screen",
  "type": "module",
  "scripts": {
    "build": "rollup -c",
    "watch": "rollup -c -w",
    "typecheck": "tsc --noEmit"
  },
  "license": "MIT",
  "devDependencies": {
    "@decky/rollup": "^1.0.2",
    "@decky/ui": "^4.16.0",
    "@types/react": "19.1.1",
    "@types/react-dom": "19.1.1",
    "react": "19.1.1",
    "rollup": "^4.53.3",
    "typescript": "^5.6.2"
  },
  "dependencies": {
    "@decky/api": "^1.1.3",
    "react-icons": "^5.3.0",
    "tslib": "^2.7.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/kromossomom-debug/decky-ps5-dashboard.git"
  }
}

````

## plugin.json

Ruta: `MenuVersion2/decky-ps5-dashboard/plugin.json` · Bytes: 523 · SHA-256: `9d3338fa143b8a77173f27eba288b562462963ea7f227c4f7e18418bcea59cdb`

````text
{
  "name": "PS5 Dashboard",
  "author": "kromossomo",
  "flags": [],
  "api_version": 1,
  "publish": {
    "tags": [
      "theme",
      "style",
      "playstation",
      "ps5",
      "hltb"
    ],
    "description": "The PlayStation 5 home screen for SteamOS Game Mode: a game row on top, full-screen art, a white Play button, HowLongToBeat and achievement cards, and PS5 colors everywhere.",
    "image": "https://raw.githubusercontent.com/kromossomom-debug/decky-ps5-dashboard/main/docs/screenshots/home.jpg"
  }
}

````

## ps5-dashboard.zip

Ruta: `MenuVersion2/decky-ps5-dashboard/ps5-dashboard.zip` · Bytes: 73472 · SHA-256: `764951db3858f42ed7fe12c0925557c1c1b51640a5554d7ff218edfad734381e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## rollup.config.js

Ruta: `MenuVersion2/decky-ps5-dashboard/rollup.config.js` · Bytes: 74 · SHA-256: `95e1c5a32396bed80b2d4148507520b9504e277ff954e993979679b14336ea45`

````text
import deckyPlugin from "@decky/rollup";

export default deckyPlugin({});

````

## tsconfig.json

Ruta: `MenuVersion2/decky-ps5-dashboard/tsconfig.json` · Bytes: 498 · SHA-256: `fa7f552df07f3bb2fded576b1ddd9b41284ef93df89b252baafb472c062c0662`

````text
{
  "compilerOptions": {
    "outDir": "dist",
    "module": "ESNext",
    "target": "ES2020",
    "jsx": "react-jsx",
    "declaration": false,
    "moduleResolution": "node",
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "esModuleInterop": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noImplicitAny": true,
    "strict": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}

````

