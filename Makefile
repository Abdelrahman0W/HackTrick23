include .env
export

RESET = \033[0m
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
BLUE = \033[0;34m

BASE_DIR = $(shell pwd)
PORT = 8000

local:
	@echo -e "$(RED)== TODO ==$(RESET)"

submit:
	@echo -e "$(RED)== TODO ==$(RESET)"

genmaze:
	@echo -e "$(RED)== TODO ==$(RESET)"

render:
	@echo -e "$(GREEN)== Starting Maze Renderer... ==$(RESET)"
	@python ./renderer.py $(PORT)
