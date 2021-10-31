install:
	$(info Installing requirements)
	pip3 install -r requirements.txt
	$(info Requirements installed successfully)

format:
	$(info Formatting code)
	pip3 install black
	black src/
	
run:
	$(info Starting Copy Paste Anything)
	python3 src/driver.py

run-no-copy:
	$(info Starting Copy Paste Anything in no-copy mode)
	python3 src/driver.py --no-copy

help:
	python3 src/driver.py --help
