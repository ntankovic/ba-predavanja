"""Use a project-local headless shell without starting the desktop Chrome app."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', str(ROOT / '.tools/playwright-browsers'))


def launch_browser(playwright):
    override = os.environ.get('CHROME_BIN')
    options = {'headless': True}
    if override:
        options['executable_path'] = override
    try:
        return playwright.chromium.launch(**options)
    except Exception as error:
        if "Executable doesn't exist" in str(error):
            raise SystemExit('Headless shell is missing. Run just browser-install with internet access, then repeat this command.') from None
        raise
