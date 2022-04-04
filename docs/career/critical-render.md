# Critical Render Path

DOMContentLoaded ->

DOM -> CSSOM -> Render Tree -> Layout -> Paint

JavaScript requires the HTML and CSS data to be parsed before it can start loading so we want the JS to run last. This is why we run the script tags at the bottom of the HTML body and we run the CSS in the head element of our HTML document
- HTML: Load style tag in the `<head>`, load `<script>` tag at the end of the body

CSS is render blocking because the document is waiting for all the styles to load before it renders
- CSS: 
  - Only load whatever is needed
  - Incorporate above the fold loading
    - This means needed to load as the page is opened

[Table of Contents](../index.md)
