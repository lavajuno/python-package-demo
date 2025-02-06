build: clean
	python3 -m build

test:
	python3 -m unittest tests.test_demo

clean:
	rm -f dist/*
