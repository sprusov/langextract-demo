.PHONY: install dev lint test run clean docker-build docker-run docker-shell

install:
	pip install .

dev:
	pip install -r requirements.txt

lint:
	ruff langextract_demo

test:
	pytest tests

run:
	python -m langextract_demo.extractor

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +

docker-build:
	docker-compose build

docker-run:
	docker-compose up

docker-shell:
	docker-compose run --rm langextract /bin/bash
