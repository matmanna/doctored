---
layout: page
title: About
description: Features of the Doctored Theme
footnotes: false
toc: true
---

<!-- This file is auto-generated based on a markdown file in _drafts. Do not edit directly. -->

## Introduction

> [!IMPORTANT]
> The Doctored theme is still very much a work-in-progress, so expect breaking features and lots of bugs!

## Inspiration

The idea for doctored was taken from seeing so many amazing blogs which have their own distinctive, refined personalities. I wanted to combine these and make something sophisticated.

## Features

### markdown/post/page rendering:

- Footnotes & Sidenotes
- GFM Admonitions
- Live, Floating, linked Table Of Contents
- Anchor links

### site

- UI modes and bold colorthemes
  - Dark/light/system mode toggle and dropdown
  - Customizable color themes (22 [colors](tailwindcss.com/docs/colors)!)
- Tailwind styling
- FontAwesome icons
- Scroll to top button
- Navbar and Footer
- Sticky header on posts
- Git site statistics
- RSS [feed]({{ '/feed.xml' | relative_url }})
- [sitemap]({{ '/sitemap.xml' | relative_url }})

### pages

- Homepage (index)
- About Page
- Post Pages
- Blog Page
- 404 Page
- Now Page
- Projects Page

## Todo

### new pages

- Contact Form

### post/page features:

- Mermaid diagrams
- Dialogue chains
- Quote-ables
- expandable annotations
- Nice images with captions
- Code blocks (with origins)
  - Syntax highlighting
  - GitHub gists?
  - Jekyll with Agda: https://github.com/paolobrasolin/jekyll-agda

### site updates:

- Webring & 88x31 section
- Post series (with pages)
- search
- page hover embeds
- microblog?
- backlinks
- FAQ section type
- Comments (giscus?)
- page network diagram

### metadata stuff:

- robots.txt
- update README/home/marketing
  - add demo site links (under projects)
    - technical product site (projects) ⚙️
      - the doctored documentation site!!
    - individual portolio/blog 👋
    - digital garden 🪴
      - inspired by quartz for obsidian
  - advertise "skins" better
  - advertise the ability to "doctor"/customize/fudge/adjust/forge/alter/modify/tailor to specific needs
    - adaptable/flexible

### code/dx stuff:

 - Demo Video
 - pnpm
 - page section customizability through config
   - cards/rows/etc similar to lualine syntax
- customization of small details
  - icons (anchors, open in new)
  - site fonts
  - link formats
  - secondary colors?
  - status of 
    - footnote
    - sidenote
    - search
    - TOC/moving TOC
    - git metadata
    - page progressbar
  - nav
    - tabs/language (blog/posts/updates/talks/notes/now/projects/contact/about)
    - topbar vs sidebar
- GitHub-wiki-based documentation of all config options
