WAVE_URL:=https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-darwin-amd64.tar.gz #wave server
wave:
	wget -O wave.tgz $(WAVE_URL)
	tar xzf wave.tgz
	mv wave-*-*-* wave
	rm -rf wave.tgz

venv:
	python3 -m venv venv
	./venv/bin/python3 -m pip install --upgrade pip

.PHONY: setup
setup: venv
	./venv/bin/pip3 install -r requirements.txt

.PHONY: setup-test
setup-test:
	@./venv/bin/pip3 install -r requirements-test.txt
	./venv/bin/playwright install

.PHONY: test
test:
	@PYTHONPATH=. ./venv/bin/pytest --no-header tests/unit

.PHONY: test-e2e
test-e2e:
	@PYTHONPATH=. ./venv/bin/pytest --headed --slowmo 200 tests/e2e/

.PHONY: run-app
run-app:
	./venv/bin/wave run app.main

.PHONY: test-style
test-style:
	@./venv/bin/flake8

.PHONY: format
format:
	./venv/bin/isort --skip venv --skip wave --skip wave-apps .
	./venv/bin/black --exclude='(venv|wave|wave-app)' .