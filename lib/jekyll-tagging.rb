# frozen_string_literal: true

# Compatibility shim for Jekyll's theme dependency loader, which requires
# gems by name ("jekyll-tagging") instead of file path ("jekyll/tagging").
require "jekyll/tagging"
