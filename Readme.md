# Sculpt Mode Scale Warning 1.2 (Blender Addon)

A simple Blender addon that helps you avoid sculpting issues caused by unapplied object scale.

When entering **Sculpt Mode**, if the selected object's scale is **not applied (not 1.0)**, the addon changes the **viewport background to a bright red**, alerting you visually.

## 🎯 Features

- 🎨 Changes the 3D Viewport background color to red when entering Sculpt Mode with unapplied scale.
- 🧠 Automatically sets the viewport shading background to "Custom", using:
  - Dark gray (`#191919`) as the default background outside of Sculpt Mode.
  - Bright red (`#FF5959`) as a warning when in Sculpt Mode with unapplied scale.
- ⚙️ Lightweight and works silently in the background.

## 🧪 How it works

1. When you enter Sculpt Mode:
   - If the object's scale is unapplied, the background turns red (`#FF5959`).
   - If the scale is applied, the background stays dark gray (`#191919`).
2. The addon checks and adjusts the background automatically, so it continues to work even if you change workspaces (e.g., switching from the Layout tab to Sculpting).

## ⚠️ Requirements

- Blender **4.5 or higher**.

The addon requires the **Viewport Shading > Background** setting to be **Custom** (not "Theme" or "World").  
This setting is handled automatically by the addon.

## 📦 Installation

1. Download the `.py` file or `.zip` package.
2. In Blender, go to `Edit > Preferences > Add-ons > Install`.
3. Select the file and enable the addon.
4. Done! It works automatically in the background.

## 💡 Tip

To apply scale manually, use `Ctrl + A` → "Scale" in Object Mode.

## 📄 License

Free to use and modify for personal or commercial use. Attribution appreciated but not required.

---

Idea by Luga3D — Code brewed with ChatGPT ☕.

