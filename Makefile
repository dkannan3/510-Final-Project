run:
	python3 src/main.py

clean:
	rm -rf src/components/__pycache__
	rm -rf src/.DS_Store
	rm -rf .DS_Store
	rm -rf src/__pycache__

test:
	python3 src/tests.py