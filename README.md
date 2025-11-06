# 🎩 Doctored

[![wakatime](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86.svg)](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/matmanna/doctored/jekyll.yml)

A  blog theme prioritizing uniqueness, technical complexity, and sophistication.

**Demo Deployment:** https://matmanna.github.io/doctored

## 🌟 Overview

Made using Jekyll and Tailwind following the [Tonic](https://tonic.hackclub.com) starter guide and [template](https://github.com/hackclub/tonic-starter). No other jekyll theme really felt like it matched what I would have wanted so I created my own!

**💫 Feature highlights:**

- 20+ color schemes & dark/light/system modes
- Projects, blog, now, and contact pages
- GFM support (tables, admonitions, etc.)
- Git metadata access
- Floating Table of Contents
- Side & foot notes
- RSS feed & sitemap
- Responsive nav, footer sections

## 📸 Demo Images:

| <img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/a130fd59-c673-4f4a-a676-3fd0bfb2473b" /> | <img width="1914" height="1018" alt="image" src="https://github.com/user-attachments/assets/2eeb6c33-fe38-46a4-8d54-c1fad985ed3b" /> |
| ----- | ---- |
| <img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/0919fd1d-2ed2-4ded-829a-6b504f939515" /> | <img width="1917" height="1014" alt="image" src="https://github.com/user-attachments/assets/dadb5548-a2c0-4f22-a2e1-6b2f67bd29f9" /> |

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

## 🙌 Contributing

Please create Issues and PRs for bugs/feature requests and updated code respectively. 

### 📜 License

Doctored is licensed under the MIT, which means you can do (almost) anything with it!!
