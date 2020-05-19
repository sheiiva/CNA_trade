##
## EPITECH PROJECT, 2019
## TRADE
## File description:
## Makefile
##

NAME =	trade


RM 		=	@rm -f
PRINT	=	@echo -e

SOURCES		=	sources/

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) __pycache__

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARY\n"
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re