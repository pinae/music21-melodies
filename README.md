# music21-melodies
Using the python library music21

## Requirements

* [Musescore](https://musescore.org/)
* Python 3.10, see [Python downloads](https://www.python.org/downloads/). You can try a different version of Python, change the [Pipfile](Pipfile) acccordingly.
* [pip](https://pip.pypa.io/en/stable/getting-started/)
* [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
* Install the needed packages `pipenv install`
* Configure music21
  * [Original documentation](https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html)
  * However, this project runs in a virtual Python environment. So you have to do it differently. Run the installation in the virtual environment: `pipenv run python -m music21.configure`
  * This might actually be quite slow to start. 
  * You should configure Musescore as an XML reader.
* Run the Jupyter notebook: `pipenv run jupyter notebook`. A browser should open and you should be good to go.
  * At the top, you have to select that you trust the notebook. Otherwise it is unable to run Muse
