import pygame

TEXT_SPACE_WIDTH = 60
TEXT_SPACE_HEIGHT = 60
MARGIN = 10
FONT_SIZE = 30

class Interface:
    def __init__(self, screen, machine):
        self.screen = screen
        self.machine = machine
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.final_msn = None
        self.final_msn_color = None

    def draw(self):
        self.screen.fill((30, 30, 30))
        fita = self.machine.fita
        pos = self.machine.current
        screen_width = self.screen.get_width()
        center = screen_width // 2

        visibles = 15
        start = pos - visibles // 2
        end = pos + visibles // 2 + 1

        for i in range(start, end):
            if i < 0 or i >= len(fita):
                symbol = '_'
            else:
                if fita[i] is not None:
                    symbol = fita[i] 
                else:
                    symbol = '_'

            deslocamento = (i - pos) * (TEXT_SPACE_WIDTH + MARGIN)
            x = center + deslocamento
            y = 200

            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, TEXT_SPACE_WIDTH, TEXT_SPACE_HEIGHT))
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, TEXT_SPACE_WIDTH, TEXT_SPACE_HEIGHT), 2)

            texto = self.font.render(symbol, True, (0, 0, 0))
            self.screen.blit(texto, (x + 20, y + 15))

            if i == pos:
                pygame.draw.polygon(self.screen, (255, 0, 0), [
                    (x + 10, y - 20),
                    (x + 30, y),
                    (x + 50, y - 20)
                ])

        state = self.machine.q.getName()
        state_text = self.font.render(f"Estado: {state}", True, (255, 255, 255))
        self.screen.blit(state_text, (30, 30))

        if self.final_msn:
            final_text = self.font.render(self.final_msn, True, self.final_msn_color)
            self.screen.blit(final_text, (30, 70))


    def define_final_msn(self):
        if self.machine.q.isFinal:
            self.final_msn = f"Reconheceu: {self.machine.w}"
            self.final_msn_color = (0, 255, 0)
        else:
            self.final_msn = f"Não reconheceu: {self.machine.w}"
            self.final_msn_color = (255, 0, 0)