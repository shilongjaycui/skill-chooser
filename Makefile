install:
	pip install --upgrade pip
	
	pip install notion-client

test-client:
	python src/skill_chooser/client.py