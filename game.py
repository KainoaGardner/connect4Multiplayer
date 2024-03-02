import pygame.key

from settings import *

class Game:
    def __init__(self):
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]

        self.colorDict = {0:"#2d3436",1:"#e74c3c",2:"#f1c40f"}
        self.turn = 1
        self.myTurn = 1
        self.opponentTurn = 2
        self.player1Win = False
        self.player2Win = False
        self.winningTiles = []

        self.pressed = False

    def displayBoard(self):
        pygame.draw.rect(screen,"#0984e3",(0,TILESIZE,WIDTH,HEIGHT - TILESIZE))
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pygame.draw.circle(screen,self.colorDict.get(self.board[r][c]),(c * TILESIZE + TILESIZE // 2,r * TILESIZE + TILESIZE // 2 + TILESIZE),TILESIZE //2  - 5)

    def displayDropPiece(self):
        if len(self.winningTiles) <= 0:
            mos = pygame.mouse.get_pos()
            xTile = mos[0] // TILESIZE
            if 0 <= mos[0] < WIDTH:
                pygame.draw.circle(screen,self.colorDict.get(self.turn),(xTile * TILESIZE + TILESIZE // 2,TILESIZE // 2),TILESIZE//2)

            if pygame.mouse.get_pressed()[0] and self.pressed == False and len(self.winningTiles) == 0:
                self.pressed = True
                self.dropPiece(xTile)

            if pygame.mouse.get_pressed()[0] == False and self.pressed == True:
                self.pressed = False

        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.pressed == False:
                self.pressed = True
                self.reset()
            if key[pygame.K_SPACE] == False and self.pressed == True:
                self.pressed = False
    def dropPiece(self,xTile):
        for r in range(len(self.board)):
            if self.board[0][xTile] != 0:
                break
            if self.board[r][xTile] != 0:
                self.board[r-1][xTile] = self.turn
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                break
            elif self.board[-1][xTile] == 0:
                self.board[-1][xTile] = self.turn
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                break

        if self.checkWin():
            if self.winningTiles[0] == 1:
                self.player1Win = True
            elif self.winningTiles[0] == 2:
                self.player2Win = True
            self.winningTiles = set(self.winningTiles)
            print(self.winningTiles)

    def checkWin(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    if c <= len(self.board[r]) - 4:
                        if self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2] == self.board[r][c + 3]:
                            self.winningTiles.append((r,c))
                            self.winningTiles.append((r,c + 1))
                            self.winningTiles.append((r,c + 2))
                            self.winningTiles.append((r,c + 3))

                    if r <= len(self.board) - 4:
                        if self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c] == self.board[r + 3][c]:
                            self.winningTiles.append((r, c))
                            self.winningTiles.append((r + 1, c))
                            self.winningTiles.append((r + 2, c))
                            self.winningTiles.append((r + 3, c))

                    if c <= len(self.board[r]) - 4 and r <= len(self.board) - 4:
                        if self.board[r][c] == self.board[r + 1][c + 1] == self.board[r + 2][c + 2] == self.board[r + 3][c + 3]:
                            self.winningTiles.append((r, c))
                            self.winningTiles.append((r + 1, c + 1))
                            self.winningTiles.append((r + 2, c + 2))
                            self.winningTiles.append((r + 3, c + 3))

                    if c >= 3 and r <= len(self.board) - 4:
                        if self.board[r][c] == self.board[r + 1][c - 1] == self.board[r + 2][c - 2] == self.board[r + 3][c - 3]:
                            self.winningTiles.append((r, c))
                            self.winningTiles.append((r + 1, c - 1))
                            self.winningTiles.append((r + 2, c - 2))
                            self.winningTiles.append((r + 3, c - 3))

        return len(self.winningTiles) > 0

    def highlightWin(self):
        if len(self.winningTiles) > 0:
            for tile in self.winningTiles:
                pygame.draw.circle(screen,"#ecf0f1",(tile[1] * TILESIZE + TILESIZE // 2,tile[0] * TILESIZE + TILESIZE // 2 + TILESIZE),TILESIZE //2  - 5,5)

    def reset(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        self.player1Win = False
        self.player2Win = False
        self.winningTiles = []
        self.turn = 1

    def update(self):
        self.displayDropPiece()
        self.displayBoard()
        self.highlightWin()


game = Game()
