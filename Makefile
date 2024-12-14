# Runs the code for custom input tests
run:
	python3 src/main.py

# Cleans the project directory of temporary files
clean:
	rm -rf src/components/__pycache__
	rm -rf src/.DS_Store
	rm -rf .DS_Store
	rm -rf src/__pycache__

# Runs the tests for the project
test:
	python3 src/tests.py