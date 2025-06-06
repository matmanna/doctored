# 🎩 Doctored

[![wakatime](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86.svg)](https://wakatime.com/badge/user/7482ea9d-3085-4e9b-95ad-1ca78a14d948/project/f57b75b4-8209-4d96-bb52-b673574bed86) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/joshpinto6/doctored/jekyll.yml)

A  blog theme prioritizing uniqueness, technical complexity, and sophistication.

📱 **Demo Deployment:** https://joshpinto6.github.io/doctored

## 💬 About

Made entirely by me using Jekyll and Tailwind following the [Tonic](https://tonic.hackclub.com) starter guide and [template](https://github.com/hackclub/tonic-starter). No other jekyll theme really felt like it matched what I would have wanted so I created my own!

**💫 Feature highlights:**

- 20+ color schemes and dark/light/system modes
- Projects, blog, now, and contact pages
- GFM support (tables, admonitions, etc.)
- Git metadata access
- RSS feed & sitemap
- Responsive nav, footer sections

## 📸 Demo Images:

| Light | Dark |
| --- | --- |
| Home Page |
| ![image](https://github.com/user-attachments/assets/94738de9-6e5a-4a84-bcca-5ff49b35f04c) | ![image](https://github.com/user-attachments/assets/e838e82f-f90b-4863-b5fb-33a5626c26c5) |
| About Page |
| ![image](https://github.com/user-attachments/assets/424ad4f2-dd78-4928-b7f9-71160fccee6c) | ![image](https://github.com/user-attachments/assets/4702d27b-274a-4dff-ac10-a9eb34376fd8) |
| Projects Page |
| ![image](https://github.com/user-attachments/assets/9d915ad0-5108-4b6e-a558-6849b90187a0) | ![image](https://github.com/user-attachments/assets/f67b8aef-49de-4559-b793-b925cbae3d73) |
| Blog Page |
| ![image](https://github.com/user-attachments/assets/9b9db8f2-2566-4c8e-bcde-372eb3f45721) | ![image](https://github.com/user-attachments/assets/8c6a2dc9-88e4-45cc-a27a-ebcec00aa8e4) |
| Blog Post |
| ![image](https://github.com/user-attachments/assets/25fd4795-2eff-4cd1-8997-26bbbc65f6f5) | ![image](https://github.com/user-attachments/assets/dd8d8970-cc65-4b27-8c1b-5d04914c2ee5) |
| Now Page |
| ![image](https://github.com/user-attachments/assets/271a300f-65e5-4a46-b62a-139ce1e5b0b9) | ![image](https://github.com/user-attachments/assets/c3c7bd74-ce5f-401f-983e-d9dc395efc16) |

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