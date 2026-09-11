# InsightFlow visual system

The interface is intentionally desktop-first and premium, inspired by liquid-glass mobile finance design without cloning a mobile layout.

- Deep violet-black canvas with slow ambient color fields.
- Layered translucent surfaces instead of flat cards.
- Subtle 1px highlights and restrained inner shadows to sell depth.
- Purple is used for state and focus, not as a neon decoration.
- Motion is short and low-amplitude: entry blur/fade, hover lift, ambient drift and data drawing.
- System/SF-style typography keeps it sharp without bundling external font assets.
- Cards are intentionally asymmetric in information density to avoid template-dashboard repetition.

The visual primitives live in `frontend/app/globals.css`; reusable structure is kept in `components/ui`.
