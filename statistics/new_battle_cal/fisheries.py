from read_config.read_config import *

class Fisheries:
    def __init__(self,fish_id):        
        self.fish_id = fish_id
        self.fishery_id = 0
        self.fishery_info = {}

        for fishery_id, fishery_info in fisheries_data.items():
            if 'fish' in fishery_info:
                if fish_id in fishery_info['fish']:
                    self.fishery_id = fishery_id
                    self.fishery_info = fishery_info

    def get_fishery_info(self):
        return self.fishery_info
    
    def get_tension_reel(self):
        return self.fishery_info['tensionReel'] if 'tensionReel' in self.fishery_info else 0
# 示例使用
if __name__ == "__main__":
    fisheries = Fisheries("302001")
    print(fisheries.get_fishery_info())
