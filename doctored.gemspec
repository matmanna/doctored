# coding: utf-8
# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name = "doctored"
  spec.version = "0.1.3"
  spec.authors = ["matmanna"]
  spec.email = [""]
  spec.license = "MIT"

  spec.summary = "🎩 A blog theme prioritizing uniqueness, complexity, and sophistication. "
  spec.description = " Doctored is a jekyll theme built with tailwind CSS which enables the ceration of static, yet highly advanced, blogs, digital gardens, documentation, and portfolio websites."
  spec.homepage = "https://matmanna.github.io/doctored"

  spec.files = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|_config\.yml|404\.md|package\.json|postcss\.config\.js|tailwind\.config\.js)ay!i) }

  spec.add_runtime_dependency "jekyll", ">= 3.9.0"
  spec.add_dependency 'jekyll-postcss', '~> 0.5.0'

  spec.add_development_dependency "bundler"
end
