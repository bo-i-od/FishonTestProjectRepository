
struct FISH_BAG
{

    int id;
    string name;          // 模板名称
    int itemTpId;             // 索引id（物品ID）
    int fishCardCount;           // 可以开出卡包的数量
    int fishBagFishery;    // 所属渔场
    int fishBagType;        // 1-普通 2-hidden 3-boss
};

FISH_BAG fish_bag[];
#pragma import("FISH_BAG.data.txt")

