RAW_DATA_PATH = raw_data/game_info.csv
PROCESSED_DATA = processed_data/rawg_data_cleaned.csv

install:
	pip install --upgrade pip && pip install -r requirements.txt

process: $(RAW_DATA_PATH)
	python3 data_cleansing_with_matrix.py $(RAW_DATA_PATH)

datavisual: $(PROCESSED_DATA)
	python3 MR_visualization.py $(PROCESSED_DATA)
	python3 Visualization_interactive.py

#without the argument, it will use the default path
test:
	python3 MR_visualization.py 
	python3 Visualization_interactive.py

clean: 
	rm -rf *.png 

.PHONY: install process datavisual test clean

