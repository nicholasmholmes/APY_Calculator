import pygame

INITIAL_INFO_Y = 50
RESULT_INFO_Y = 300
RESULT_INFO_X = 350
FINAL_TOTAL_X = 550
FPS = 30


class APYCalculator:
    def __init__(self):
        self.screen = None
        self.font = None
        self.small_font = None
        self.clock = pygame.time.Clock()
        self.input_boxes = []
        self.active_box = None
        self.results_text = None
        self.show_results = False

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 24)
        self.create_input_boxes()
        self.move_initial_info()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                for box in self.input_boxes:
                    box.handle_event(event)

            self.screen.fill((255, 255, 255))
            self.draw_input_boxes()

            if self.are_all_boxes_filled():
                self.calculate_apy()
                self.show_results = True
            else:
                self.show_results = False

            self.draw_title()
            if self.show_results:
                self.draw_results()

            pygame.display.flip()
            self.clock.tick(FPS)

    def draw_title(self):
        title_text = self.font.render("APY Calculator", True, (0, 0, 128))
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, INITIAL_INFO_Y))
        self.screen.blit(title_text, title_rect)

    def create_input_boxes(self):
        y = INITIAL_INFO_Y

        current_amount_box = InputBox(50, y, 200, 32, "Current Balance: $")
        self.input_boxes.append(current_amount_box)

        apy_rate_box = InputBox(50, y + 40, 200, 32, "APY Interest Rate %: ")
        self.input_boxes.append(apy_rate_box)

        accrual_frequency_box = InputBox(50, y + 80, 200, 32, "Accrual Frequency(monthly/yearly): ")
        self.input_boxes.append(accrual_frequency_box)

        deposit_frequency_box = InputBox(50, y + 120, 200, 32, "Deposit Frequency(weekly/monthly/yearly): ")
        self.input_boxes.append(deposit_frequency_box)

        deposit_amount_box = InputBox(50, y + 160, 200, 32, "Deposit Amount: $")
        self.input_boxes.append(deposit_amount_box)

    def draw_input_boxes(self):
        for box in self.input_boxes:
            box.draw(self.screen)
            if box is self.active_box:
                pygame.draw.rect(self.screen, (0, 0, 0), box.rect, 2)

    def move_initial_info(self):
        for box in self.input_boxes:
            box.rect.y += INITIAL_INFO_Y

    def are_all_boxes_filled(self):
        for box in self.input_boxes:
            if box.text == '':
                return False
        return True

    def calculate_apy(self):
        # Get user input
        current_amount = float(self.input_boxes[0].text)
        apy_rate = float(self.input_boxes[1].text)
        accrual_frequency = self.input_boxes[2].text
        deposit_frequency = self.input_boxes[3].text
        deposit_amount = float(self.input_boxes[4].text)

        # Calculate APY
        monthly_rate = apy_rate / 100 / 12 if accrual_frequency == "yearly" else apy_rate / 100

        final_total = current_amount
        total_deposited = 0
        total_earned = 0
        earned_per_month = []

        if deposit_frequency == "yearly":
            final_total += deposit_amount
            total_deposited += deposit_amount

        for month in range(12):
            total_earned_monthly = final_total * monthly_rate
            total_earned += total_earned_monthly
            final_total += total_earned_monthly

            if deposit_frequency == "weekly":
                final_total += deposit_amount * 4
                total_deposited += deposit_amount * 4
            elif deposit_frequency == "monthly":
                final_total += deposit_amount
                total_deposited += deposit_amount

            earned_per_month.append(total_earned_monthly)

        if deposit_frequency == "weekly":
            final_total += deposit_amount * 4
            total_deposited += deposit_amount * 4

        self.results_text = "Amount earned per month:\n"
        for i, earned in enumerate(earned_per_month[:6]):
            self.results_text += f"Month {i + 1}: ${earned:.2f}\n"

        self.results_text += "\n"

        for i, earned in enumerate(earned_per_month[6:]):
            self.results_text += f"Month {i + 7}: ${earned:.2f}\n"

        self.results_text += f"\nTotal deposited: ${total_deposited:.2f}\n"
        self.results_text += f"Total earned: ${total_earned:.2f}\n"
        self.results_text += f"Final balance after 1 year: ${final_total:.2f}"

    def draw_results(self):
        if self.results_text:
            result_lines = self.results_text.split("\n")
            line_height = self.small_font.get_height()

            y = RESULT_INFO_Y
            max_width_1_6 = 0
            max_width_7_12 = 0

            header_line = result_lines[0]
            month_lines_1_6 = result_lines[1:7]
            month_lines_7_12 = result_lines[8:14]
            total_deposited_line = result_lines[15]
            total_earned_line = result_lines[16]
            final_total_line = result_lines[17]

            # Calculate the maximum width of the result lines for months 1-6
            max_width_1_6 = max(
                self.small_font.size(line)[0]
                for line in month_lines_1_6
            )

            # Calculate the maximum width of the result lines for months 7-12
            max_width_7_12 = max(
                self.small_font.size(line)[0]
                for line in month_lines_7_12
            )

            # Calculate the maximum width among months 1-6 and months 7-12
            max_width = max(max_width_1_6, max_width_7_12)

            # Calculate the x-coordinate for months 7-12
            x_7_12 = (self.screen.get_width() - max_width) // 2 + 75

            # Calculate the x-coordinate for months 1-6
            x_1_6 = x_7_12 - max_width - 10

            # Display "total earned per month" title
            earned_text = "Amount Earned per Month:"
            earned_font_size = 24
            earned_font = pygame.font.SysFont(None, earned_font_size, bold=True)
            earned_text_surface = earned_font.render(earned_text, True, (0, 0, 0))
            earned_text_width = earned_text_surface.get_width()
            earned_text_x = (self.screen.get_width() - earned_text_width) // 2
            self.screen.blit(earned_text_surface, (earned_text_x, y))
            y += line_height + 5

            # Display month lines 1-6
            for line in month_lines_1_6:
                text_surface = self.small_font.render(line, True, (0, 0, 0))
                self.screen.blit(text_surface, (x_1_6, y))
                y += line_height + 5

            # Reset y-coordinate for the second set of month lines
            y = RESULT_INFO_Y + line_height + 5

            # Display month lines 7-12
            for line in month_lines_7_12:
                text_surface = self.small_font.render(line, True, (0, 0, 0))
                self.screen.blit(text_surface, (x_7_12, y))
                y += line_height + 5

            # Calculate the y-coordinate for the "total earned per month"
            y_earned = y + line_height * 2

            # Calculate the x-coordinate for the "total earned per month"
            x_total = (self.screen.get_width() - max_width) // 2

            # Display "total earned per month"
            total_earned_font_size = 24
            total_earned_font = pygame.font.SysFont(None, total_earned_font_size, bold=True)
            total_earned_text_surface = total_earned_font.render(total_earned_line, True, (0, 0, 0))
            total_earned_text_width = total_earned_text_surface.get_width()
            total_earned_text_x = (self.screen.get_width() - total_earned_text_width) // 2
            self.screen.blit(total_earned_text_surface, (total_earned_text_x, y_earned))

            # Calculate the y-coordinate for the "total deposited"
            # Calculate the y-coordinate for the "total deposited"
            y_deposited = y_earned + line_height

            # Display "total deposited"
            total_deposited_font_size = 24
            total_deposited_font = pygame.font.SysFont(None, total_deposited_font_size, bold=True)
            total_deposited_text_surface = total_deposited_font.render(total_deposited_line, True, (0, 0, 0))
            total_deposited_text_width = total_deposited_text_surface.get_width()
            total_deposited_text_x = (self.screen.get_width() - total_deposited_text_width) // 2
            self.screen.blit(total_deposited_text_surface, (total_deposited_text_x, y_deposited))

            # Calculate the y-coordinate for the "final total"
            y_final = y_deposited + line_height

            # Display "final total"
            final_total_font_size = 24
            final_total_font = pygame.font.SysFont(None, final_total_font_size, bold=True)
            final_total_text_surface = final_total_font.render(final_total_line, True, (0, 0, 0))
            final_total_text_width = final_total_text_surface.get_width()
            final_total_text_x = (self.screen.get_width() - final_total_text_width) // 2
            self.screen.blit(final_total_text_surface, (final_total_text_x, y_final))


class InputBox:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.highlight_color = pygame.Color('lightblue')
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.label = label
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.active:
                    self.color = self.highlight_color  # Set highlight color when active
                    calculator.active_box = self
                else:
                    self.color = pygame.Color('lightskyblue3')
                    calculator.active_box = None
            else:
                self.active = False
                self.color = pygame.Color('lightskyblue3')

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = pygame.Color('lightskyblue3')
                    calculator.active_box = None
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.rect(screen, self.highlight_color, self.rect)  # Fill the rectangle with highlight color
        self.rect.width = 700
        text_surface = self.font.render(self.label + self.text, True, pygame.Color('black'))  # Set text color to black
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


# Create an instance of the APYCalculator class
calculator = APYCalculator()

# Call the run method to start the calculator
calculator.run()
