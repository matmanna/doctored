---
layout: page
title: Welcome to my Theme
description: The home page for the Doctored blog theme.
permalink: /
---

## Recent Projects

<ul class="px-0 flex mt-3 flex-col gap-3 not-prose">
	{% assign recent_projects = site.projects | sort: "start_date" | reverse %}
	{% for project in recent_projects limit:5 %}
	{% include post-card.html entry=project kind='project' %}
	{% endfor %}
</ul>

## Recent Blog Posts

<ul class="px-0 flex mt-3 flex-col gap-3 not-prose">
	{% for post in site.posts limit:3 %}
	{% include post-card.html entry=post kind='post' %}
	{% endfor %}
</ul>

<!-- This file is auto-generated based on a markdown file in _drafts. Do not edit directly. -->

a couple of _the_ most common questions<small>These are also some of the most common questions that <a href="https://en.wikipedia.org/wiki/Five_Ws">journalists</a> have!</small>[^1] you might have.

## What?

- A jekyll theme which prioritizes uniqueness, technical complexity, and sophistication<small>While this could be redundant, it describes the the theme's vibe.</small>[^2]

## Recent Projects

<ul class="px-0 flex mt-3 flex-col gap-3 not-prose">
	{% assign recent_projects = site.projects | sort: "start_date" | reverse %}
	{% for project in recent_projects limit:4 %}
	{% include post-card.html entry=project kind='project' %}
	{% endfor %}
</ul>

## Recent Blog Posts

<ul class="px-0 flex mt-3 flex-col gap-3 not-prose">
	{% for post in site.posts limit:3 %}
	{% include post-card.html entry=post kind='post' %}
	{% endfor %}
</ul>

- **For a full list of features, see [/about]({{ '/about' | relative_url }}).**
- **For code, usage instructions, and (limited) docs, see [:github]({{ site.github }}).**

## Why?

Because there is no theme quite like what I would want.

## How?

Doctored uses the following technologies:

1. Jekyll, which enables markdown-powered static sites
2. Tailwind CSS<small>Requiring node, this struck a balance between maintainability and bloat.</small>[^3], which makes styling so much easier!

## Where?

Right here, of course! But it can also be on your website: Instructions coming soon.

## Who?

- The theme was made by [me]() with heavy inspiration taken from some blogs I like [links pending].
- and [this blog post](https://danilafe.com/blog/blog_microfeatures/) by Daniel Fedorin on microfeatures.
- Also quite inspired by Mani Kumar's Xterm [theme](https://manid2.github.io/hugo-xterm/) for Hugo.
- Lastly, big thanks to [Kieren J. Underwood](https://github.com/JacobU/markdown-jekyll-preprocessor/tree/master), [Kaushik Gopal](https://kau.sh/blog/jekyll-footnote-tufte-sidenote/), and [Dave Liepmann](https://edwardtufte.github.io/tufte-css/) and for their contributions to markdown-based sidenotes for Jekyll (and the massively-inspiring Tufte CSS respectively)!
- Several awesome jekyll pure-liquid snippets by [Vladimir Jimenez](https://github.com/allejo) [specifically: jekyll-yamlfy, jekyll-toc, and jekyll-anchor-headings]

## When?

The version of the site you're viewing now was built on {{ site.git.last_commit.commit_date }}


## Footnotes 
[^1]: These are also some of the most common questions that <a href="https://en.wikipedia.org/wiki/Five_Ws">journalists</a> have!
[^2]: While this could be redundant, it describes the the theme's vibe.
[^3]: Requiring node, this struck a balance between maintainability and bloat.
