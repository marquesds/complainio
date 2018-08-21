serve: clean
	quart run

clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete
	rm -f .coverage
	rm -f pylint.out

test: clean
	nosetests -s --rednose

coverage: clean
	nosetests --with-coverage --cover-package=complainio

bandit: clean
	bandit -r complainio
