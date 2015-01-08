SRC = $(wildcard *.ui)
TEMP = $(SRC:.ui=.py)
TAR = $(TEMP:%.py=ui_%.py)

.PHONY: all clean

all: $(TAR)

ui_%.py : %.ui
	pyuic5 $^ -o $@

clean:
	rm -f $(TAR)
