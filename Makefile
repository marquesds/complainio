serve: clean
	quart run

clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete
	rm -f .coverage
	rm -f pylint.out

test: clean
	ENVIRONMENT=Testing nosetests -s --rednose

coverage: clean
	ENVIRONMENT=Testing nosetests --with-coverage --cover-package=complainio

bandit: clean
	bandit -r complainio
