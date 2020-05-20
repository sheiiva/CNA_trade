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
T_NAME	=	unitests

RM 		=	@rm -f
PRINT	=	@echo -e

INCLUDE		=	includes/
SOURCES		=	sources/
TESTS		=	tests/

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) __pycache__

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARIES\n"
	$(RM) $(NAME)
	$(RM) $(TESTS)$(T_NAME)

tests_run: fclean
	@cp $(TESTS)t_main.py $(TESTS)$(T_NAME)
	@chmod +x $(TESTS)$(T_NAME)
	$(PRINT) "\n------->\tTESTS BINARY CREATED\n"
	$(PRINT) "\nLET'S TEST:"
	@./$(TESTS)$(T_NAME)

re: fclean all

.PHONY: all clean fclean tests_run re