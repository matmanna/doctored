# 🎩 Doctored

[![Gem Version](https://badge.fury.io/rb/gemspec.svg)](https://rubygems.org/gems/jekyll-theme-doctored)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![wakatime](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86.svg)](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86) 
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/matmanna/doctored/jekyll.yml)


A  blog theme prioritizing uniqueness, technical complexity, and sophistication.

**🧪 Demo Deployment:** https://matmanna.github.io/doctored

## 🌟 Overview

Made using Jekyll and Tailwind following the [Tonic](https://tonic.hackclub.com) starter guide and [template](https://github.com/hackclub/tonic-starter). No other jekyll theme really felt like it matched what I would have wanted so I created my own!

**💫 Features:**

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

## 💾 Installation Instructions

> [!NOTE]
> Additional installation/usage instructions are WIP

To add to an existing Jekyll site using the packaged gem (recommended):

1. add the `gem "jekyll-theme-doctored` dependency to your `Gemfile`
2. run `bundle install`
3. add `theme: jekyll-theme-doctored` to your Jekyll `_config.yml`
4. follow the usage instructions below to serve (or continue customizing) your site!

## ⌨️ Usage

### ▶️ Running

Run `npm install` and `npm run dev` to develop. Run `npm run build` to build. Postinstall and other scripts have been configured to use `bundle install`, `bundle exec jekyll serve --watch`, and `bundle exec jekyll build` respectively.

### 🖼️ Formatting posts

If you want to use sidenotes in your posts/pages, begin by copying the `utils/postMarkdown.py` script and creating a `_drafts` directory within your project.

To post a new post, run `python utils/postMarkdown.py _drafts/_posts/example-001.md`, which will  format and copy it to `_posts/` (or root if page!)

- **Foot/sidenotes:**

  To add a foot/side note, include the following in your draft markdown:
  ```html
  <small>Richly-formatted (html) content of note</small>
  ```

## 🙌 Contributing

Please create Issues and PRs for bugs/feature requests and updated code respectively. 

### 📜 License

Doctored is licensed under the MIT, which means you can do (almost) anything with it!!
