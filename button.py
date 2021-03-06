import pygame


# класс кнопки
class Button:
    def __init__(self, surface, x, y, name, activated=False, color=(230, 230, 230), isactive=True):
        self.active = isactive
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.checkbox_obj = pygame.Rect(self.x, self.y, 0, 0)
        self.checkbox_outline = self.checkbox_obj.copy()
        self.checked = activated
        self.name = name
        self.hold = False

    def render(self):
        if self.checked:
            font = pygame.font.Font(None, 24)
            text = font.render(self.name, True, (0, 0, 0))
            text_x = self.x
            text_y = self.y
            text_w = text.get_width()
            text_h = text.get_height()
            rect = pygame.draw.rect(self.surface, (130, 130, 130), (text_x - 7, text_y - 7,
                                                                    text_w + 16, text_h + 12), 0)
            self.checkbox_obj = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
            self.surface.blit(text, (text_x, text_y))
        elif self.hold:
            font = pygame.font.Font(None, 24)
            text = font.render(self.name, True, (0, 0, 0))
            text_x = self.x
            text_y = self.y
            text_w = text.get_width()
            text_h = text.get_height()
            pygame.draw.rect(self.surface, (190, 190, 190), (text_x - 7, text_y - 7,
                                                             text_w + 16, text_h + 12), 0)
            self.surface.blit(text, (text_x, text_y))
        else:
            font = pygame.font.Font(None, 24)
            text = font.render(self.name, True, (0, 0, 0))
            text_x = self.x
            text_y = self.y
            text_w = text.get_width()
            text_h = text.get_height()
            rect = pygame.draw.rect(self.surface, self.color, (text_x - 7, text_y - 7,
                                                               text_w + 16, text_h + 12), 0)
            self.checkbox_obj = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
            self.surface.blit(text, (text_x, text_y))

    def update(self, event_object, others=None):
        if event_object.type == pygame.MOUSEBUTTONUP and self.active:
            x, y = event_object.pos
            px, py, w, h = self.checkbox_obj
            if px < x < px + w and py < y < py + h:
                self.checked = not self.checked
        if event_object.type == pygame.MOUSEMOTION and self.active:
            x, y = event_object.pos
            px, py, w, h = self.checkbox_obj
            if px < x < px + w and py < y < py + h:
                self.hold = True
            else:
                self.hold = False

    def is_checked(self):
        if self.checked is True:
            return True
        else:
            return False
