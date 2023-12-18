
class Slider:
    def __init__(self, bp, element_slider):
        self.basePage = bp
        self.element_slider = element_slider
        self.slider_position = self.get_slider_position()
        self.slider_size = self.get_slider_size()
        self.slider_direction = self.get_slider_direction()
        self.slider_range = self.get_slider_range()

    def get_slider_position(self):
        return self.basePage.get_position(element_data=self.element_slider)

    def get_slider_size(self):
        return self.basePage.get_size(element_data=self.element_slider)

    def get_slider_direction(self):
        if self.slider_size[0] > self.slider_size[1]:
            return "row"
        return "column"

    def get_slider_range(self):
        if self.slider_direction == "row":
            range_start = self.slider_position[0] - self.slider_size[0] * 0.5
            range_end = self.slider_position[0] + self.slider_size[0] * 0.5
            return range_start, range_end
        range_start = self.slider_position[1] - self.slider_size[1] * 0.5
        range_end = self.slider_position[1] + self.slider_size[1] * 0.5
        return [range_start, range_end]

