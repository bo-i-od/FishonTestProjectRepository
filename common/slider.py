from common.basePage import BasePage



class Slider:
    def __init__(self, bp:BasePage, element_slider):
        self.bp = bp
        self.element_slider = element_slider
        self.slider_position = self.get_slider_position()
        self.slider_size = self.get_slider_size()
        self.slider_direction = self.get_slider_direction()
        self.slider_range = self.get_slider_range()

    def get_slider_position(self):
        return self.bp.get_position(element_data=self.element_slider)

    def get_slider_size(self):
        return self.bp.get_size(element_data=self.element_slider)

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

    def get_slide_point_start_and_end(self, slide_range: [float, float]):
        if self.slider_direction == "row":
            point_start_x = self.slider_range[0] + self.slider_size[0] * slide_range[0]
            point_end_x = self.slider_range[0] + self.slider_size[0] * slide_range[1]
            point_start = [point_start_x, self.slider_position[1]]
            point_end = [point_end_x, self.slider_position[1]]
            return point_start, point_end
        point_start_y = self.slider_range[0] + self.slider_size[1] * slide_range[0]
        point_end_y = self.slider_range[0] + self.slider_size[1] * slide_range[1]
        point_start = [self.slider_position[0], point_start_y]
        point_end = [self.slider_position[0], point_end_y]
        return point_start, point_end



