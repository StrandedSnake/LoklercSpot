# LoklercSpot — Dynamic Island for Hyprland

> A dynamic island implementation for Hyprland, built with Quickshell and QML.  
> Based on [nixos-configuration](https://github.com/ilyamiro/nixos-configuration) by ilyamiro

---

## Preview

<!-- Add your screenshots here -->
<!-- ![preview](assets/preview.png) -->

---

## Features

**Contextual content** — automatically switches based on system state:
- 🎵 Music player (album art, title, artist, progress bar)
- 🎙️ Discord voice call (live timer, mute button)
- 🔴 Screen recording indicator
- 🔔 Notifications with expand-to-read
- 🕐 Clock + weather (default state)

**Dual bubble** — Discord call pill appears alongside music player simultaneously  
**App Launcher** — island morphs into Spotlight-style launcher with fuzzy search and icons  
**Clipboard Viewer** — cliphist-based history with image/text detection  
**VPN badge** — lock icon with snap-shut animation  
**Pet pill** — animated cat reacts to music and notifications  

---

## Stack

| Component     | Technology              |
|---------------|-------------------------|
| Shell         | Quickshell              |
| Language      | QML                     |
| Compositor    | Hyprland                |
| IPC           | inotifywait on /tmp/qs_* |
| Music         | playerctl               |
| Weather       | wttr.in                 |
| Clipboard     | cliphist + wl-copy      |
| Notifications | custom daemon           |

---

## Dependencies

```
quickshell
inotify-tools
playerctl
cliphist
wl-clipboard
python3
gtk-launch
flatpak (optional)
```

**Fonts:** JetBrains Mono, Iosevka Nerd Font

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/StrandedSnake/LoklercSpot
cd LoklercSpot

# 2. Run the install script
chmod +x install.sh
./install.sh
```

---

## Keybinds

### Window Management

| Bind | Action |
|------|--------|
| Super + Q | Close window (or close QS panel) |
| Super + Shift + F | Toggle floating |
| Super + F | Fullscreen |
| Super + Arrows | Move focus |
| Super + Ctrl + Arrows | Move window |
| Super + Shift + Arrows | Resize window |
| Super + Mouse1 (drag) | Move window |
| Super + Mouse2 (drag) | Resize window |

### Apps

| Bind | Action |
|------|--------|
| Super + T | Terminal |
| Super + E | Browser (Zen / Chromium fallback) |
| Super + N | Nautilus file manager |
| Alt + Tab | Window switcher (Rofi) |

### LoklercSpot Panels

| Bind | Action |
|------|--------|
| Super + Space | App Launcher |
| Super + C | Clipboard Viewer |
| Super + M | Music popup |
| Super + V | Volume popup |
| Super + B | Battery popup |
| Super + W | Wallpaper picker |
| Super + S | Calendar |
| Super + Shift + T | Focus time |
| Super + H | Guide |
| Super + A | Notification center |

### Workspaces

| Bind | Action |
|------|--------|
| Super + 1-9, 0 | Switch to workspace |
| Super + Shift + 1-9, 0 | Move window to workspace |

### Media

| Bind | Action |
|------|--------|
| Super + P | Play / Pause |
| Media Play/Pause key | Play / Pause |
| Media Next key | Next track |
| Media Prev key | Previous track |
| Media Stop key | Stop |

### System

| Bind | Action |
|------|--------|
| Super + L | Lock screen |
| Power button | Lock screen |
| Print | Screenshot (region) |
| Shift + Print | Screenshot + edit |
| Super + Print | Full screenshot |
| Super + Shift + Print | Full screenshot + edit |
| Brightness Up/Down | Adjust brightness |
| Volume Up/Down | Adjust volume |
| Mute | Toggle mute |
| Mic Mute | Toggle mic mute |
| Caps Lock | Toggle caps lock |

---

## Architecture

Each component is a separate `PanelWindow`. IPC works via `inotifywait` on `/tmp/qs_*` files — no sockets, no daemons.

The island hides itself when the launcher opens via `/tmp/qs_launcher_state`, creating a morph illusion since both windows share the same top-center position.

---

## Credits

- [ilyamiro](https://github.com/ilyamiro) — original nixos-configuration
- [Quickshell](https://quickshell.outfoxxed.me/) — shell framework

---

## License

See [LICENSE](LICENSE).
