# Recreate Petport design journey

Animated storyboard made from the existing team wireframes in this repository. It is a design walkthrough, not a recording of a deployed application. The Figma prototype remains linked below.

Run from the repository root in a separate Python 3.11+ environment:

~~~bash
python -m venv .venv-demo
source .venv-demo/bin/activate
python -m pip install -r scripts/demo-requirements.txt
python scripts/render_demo.py
~~~

Output: docs/media/petport-journey.gif. On Windows, activate with .venv-demo/Scripts/activate.

Sources: assets/home.png, assets/pet-details.png and the application/confirmation panels in wireframe.png. The script crops those existing screens, places them in a storyboard and adds transitions. It does not simulate working form submissions or claim a live implementation.

Team/source attribution remains in the main README and original project files. The demo adds presentation assets, not new product functionality.
