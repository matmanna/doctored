# 🎩 Doctored

[![wakatime](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86.svg)](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/joshpinto6/doctored/jekyll.yml)

A  blog theme prioritizing uniqueness, technical complexity, and sophistication.

📱 **Demo Deployment:** https://joshpinto6.github.io/doctored

## 💬 About

Made using Jekyll and Tailwind following the [Tonic](https://tonic.hackclub.com) starter guide and [template](https://github.com/hackclub/tonic-starter). No other jekyll theme really felt like it matched what I would have wanted so I created my own!

**💫 Feature highlights:**

- 20+ color schemes & dark/light/system modes
- Projects, blog, now, and contact pages
- GFM support (tables, admonitions, etc.)
- Git metadata access
- Table of Contents (floating)
- Side & foot notes
- RSS feed & sitemap
- Responsive nav, footer sections

## 📸 Demo Images:




## ⌨️ Usage

> [!IMPORTANT]
> Developing a site with doctored requires having Ruby, RubyGems, GCC, Make Bundle, Python, Node.js, and npm installed on your system.

### ▶️ Running

Run `npm install` and `npm run dev` to develop. Run `npm run build` to build. Postinstall and other scripts have been configured to use `bundle install`, `bundle exec jekyll serve --watch`, and `bundle exec jekyll build` respectively.

### 🖼️ Formatting posts

To post a new post, run `npm run post markdown_file_path_in__drafts`, which formats it with side/foot notes then moves it to `_posts/` (or root if page!)

Based on [@JacobU](https://github.com/jacobu)'s `postMarkdown` python script, doctored supports writing your posts/pages in a simple markdown file within `_drafts` before running the `post` script to format it in the following ways:

- **Foot/sidenotes:**

  To add a foot/side note, include the following in your draft markdown:
  ```html
  <small>Richly-formatted (html) content of note</small>
  ```