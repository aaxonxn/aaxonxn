# Contributing to the Profile Repository

First off, thank you for considering contributing to this repository! 

## Code of Conduct
This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs
If you find a visual glitch, an unresponsive widget, or broken rendering in `dark.svg` or `light.svg`, please create an issue using the Bug Report template. Include:
*   Your browser and operating system.
*   Whether you are using GitHub Dark Mode or Light Mode.
*   Screenshots of the issue.

### Suggesting Enhancements
If you have ideas to improve the architectural flow or UI design of the profile, please use the Feature Request template. Ensure your suggestion aligns with the established "Premium AI Engineer" design language.

### Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added or changed the SVG layout, ensure you modify `scripts/build_svgs.py` rather than hardcoding changes into the XML directly.
3. Update the README.md if applicable.
4. Issue that pull request!

## Project Structure
*   `README.md`: The main entrypoint. Uses standard markdown and `picture` tags.
*   `scripts/`: Python builder scripts for generating the SVGs.
*   `assets/`: Raw generated SVGs and base64 portraits.
*   `.github/`: Actions and templates.
