from display import *

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         mos =

        display()

    pygame.quit()

main()