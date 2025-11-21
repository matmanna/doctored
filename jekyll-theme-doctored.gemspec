# coding: utf-8
# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name = "jekyll-theme-doctored"
  spec.version = "0.2.1"
  spec.authors = ["matmanna"]
  spec.email = [""]
  spec.license = "MIT"

  spec.summary = "🎩 A blog theme prioritizing uniqueness, complexity, and sophistication. "
  spec.description = " Doctored is a jekyll theme built with tailwind CSS which enables the ceration of static, yet highly advanced, blogs, digital gardens, documentation, and portfolio websites."
  spec.homepage = "https://matmanna.github.io/doctored"

  spec.files = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_data|_layouts|_includes|LICENSE|404\.md|package\.json|tailwind\.config\.js)!) }

  spec.add_runtime_dependency "jekyll", "~> 4"
  spec.add_dependency "webrick", "~> 1.7"

  spec.add_dependency "kramdown-parser-gfm"
  spec.add_dependency "jekyll-gfm-admonitions"
  spec.add_dependency "jekyll-sitemap"
  spec.add_dependency "jekyll-git"
  spec.add_dependency "jekyll-seo-tag"
  spec.add_dependency "jekyll-feed"
  spec.add_development_dependency "bundler"
end
