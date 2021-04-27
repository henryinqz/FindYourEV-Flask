# Use `git update-index --assume-unchanged run.py` to ignore changes to this file (ex. entering debug mode)
# (to track changes again, use `git update-index --no-assume-unchanged run.py `)
from findyourev import app

if __name__ == "__main__":
    app.run(threaded=True, debug=False)
