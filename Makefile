#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/20/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#


NAME 	=	trade

RM 		=	@rm -f
PRINT	=	@echo -e

INCLUDE		=	includes/
SOURCES		=	sources/
TESTS		=	tests/


TESTS_SRC	=	$(TESTS)t_Rate.py			\
				$(TESTS)t_Candle.py			\
				$(TESTS)t_Logger.py			\
				$(TESTS)t_Stack.py			\
				$(TESTS)t_Transaction.py	\
				$(TESTS)t_Utilities.py


$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) -r __pycache__
	$(RM) -r $(INCLUDE)__pycache__
	$(RM) -r $(SOURCES)__pycache__
	$(RM) -r $(TESTS)__pycache__
	$(RM) .coverage
	$(RM) -r .pytest_cache

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARIES\n"
	$(RM) $(NAME)

tests_run: fclean
	$(PRINT) "\nLET'S TEST:\n"
	@python -m pytest -v $(TESTS_SRC) --cov=$(SOURCES)

re: fclean all

.PHONY: all clean fclean tests_run re