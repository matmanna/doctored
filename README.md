# 🎩 Doctored

A  blog theme prioritizing uniqueness, technical complexity, and sophistication.

📱 **Demo Site:** https://joshpinto6.github.io/doctored

## 📸 Demo Image:

![image](https://github.com/user-attachments/assets/63dea5ba-0c15-4e69-bfd8-b0234f1ebe2f)

## 💬 About

Made entirely by me using Jekyll and Tailwind following the [Tonic](https://tonic.hackclub.com) starter guide and template. 

Feature highlights:
- 20+ color schemes
- Dark/light mode
- GFM support (tables, admonitions, etc.)

## ⌨️ Usage

> [!NOTE]
> Developing a site with doctored requires having ruby, bundle, python, node.js, and npm installed. 

Run `npm install` and `npm run dev` to develop. Run `npm run build` to build

To post a new post, run `npm run post markdown_file_path_in__drafts`, which formats it with side/foot notes & a table of contents then moves it to `_posts/` (or root if page!)

Based on [@JacobU](https://github.com/jacobu)'s `postMarkdown` python script, doctored supports writing your posts/pages in a simple markdown file within `_drafts` before running the `post` script to format it in the following ways:

- **Foot/sidenotes:**

  To add a foot/side note, include the following in your draft markdown:
  ```html
  <small>Richly-formatted (html) content of note</small>
  ```

- **Table of contents:**

  To disable a table of contents for a page/post, include `toc: false` in markdown frontmatter (enabled by default). This table of contents will be based on all the markdown headings (#, ##, ###, etc.) in your file.