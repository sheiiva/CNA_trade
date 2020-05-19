#!/usr/bin/env python3
#coding: utf-8

def main():
    
    file = open("../../output.txt","w") 

    while (1):
        try:
            inp = input()
        except EOFError:
            break
        except InterruptedError:
            break
        except ValueError:
            break
        else:
            file.write("{}\n".format(inp))

    file.close()

if __name__ == "__main__":
    main()
