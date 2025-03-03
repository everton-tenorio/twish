.PHONY: venv install clean

venv:
	python3.11 -m venv venv

install: venv
	. venv/bin/activate && pip install -r requirements.txt && deactivate

clean:
	rm -rf venv
