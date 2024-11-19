from read_config.read_config import *

class FishTypeClassVisual:
    @staticmethod
    def get_info_by_class_and_type(fish_class, fish_type):
        """
        根据鱼的类别和类型查找对应信息
        :param fish_class: 鱼的类别
        :param fish_type: 鱼的类型
        :return: 找到的对象或 None
        """
        for id, data in fish_typeclass_visual_data.items():
            # print(id)
            if data['fishClass'] == fish_class and data['fishType'] == fish_type:
                return data
        return None 
    
    @staticmethod
    def get_tension_reel_by_class_and_type(fish_class, fish_type):
        data = FishTypeClassVisual.get_info_by_class_and_type(fish_class, fish_type)
        return data['tensionReel'] if data else 0 

    # def display_info(self):
    #     """显示鱼的基本信息"""
    #     info = (
    #         f"鱼的名称: {self.name}\n"
    #         f"鱼的种类: {self.species}\n"
    #         f"鱼的颜色: {self.color}\n"
    #         f"鱼的大小: {self.size}"
    #     )
    #     print(info)

    # def visualize(self):
    #     """简单的可视化方法（文本形式）"""
    #     print(f"{self.color} 的 {self.size} {self.species}（{self.name}）游动中...")

# 示例
if __name__ == "__main__":
    # goldfish = FishTypeClassVisual("金鱼", "鲤科", "金色", "小")
    # goldfish.display_info()
    # goldfish.visualize()
    test =FishTypeClassVisual.get_tension_reel_by_class_and_type("2", "1")
    print(test)