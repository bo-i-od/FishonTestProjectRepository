import random

class BATTLE_QTE_TYPE:
    LEFT = "LEFT"

class FishCommand:
    @staticmethod
    def EXAMPLE_FORCE_SEQ():
        # Placeholder for EXAMPLE_FORCE_SEQ() implementation
        return []

    @staticmethod
    def EXAMPLE_FORCE_SEQ_LARGE():
        # Placeholder for EXAMPLE_FORCE_SEQ_LARGE() implementation
        return []

    @staticmethod
    def FORCE_SEQ_DIZZY():
        # Placeholder for FORCE_SEQ_DIZZY() implementation
        return []

    @staticmethod
    def BattleRandomRange(min_val, max_val):
        return random.randint(min_val, max_val)

    @staticmethod
    def EXAMPLE_SWIM():
        return {
            "type": "SWIM",
            "timeMS": 1000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            # "buffList": [111, 112, 113]
        }

    @staticmethod
    def EXAMPLE_ESCAPE():
        return {
            "type": "ESCAPE",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ_LARGE(),
            "previewTimeMS": 1000,
            "canCounterTimingMS": [1000, 2000],
            "buffList": [100006]
        }

    @staticmethod
    def EXAMPLE_RUSH():
        return {
            "type": "RUSH",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ_LARGE(),
            "previewTimeMS": 1000,
            "canCounterTimingMS": [1000, 2000],
            "buffList": [100007]
        }

    @staticmethod
    def EXAMPLE_ACCUMULATING():
        return {
            "type": "ACCUMULATING",
            "timeMS": FishCommand.BattleRandomRange(3000, 6000),
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ()
        }

    @staticmethod
    def EXAMPLE_FRENZY():
        return {
            "type": "FRENZY",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ_LARGE(),
            "ultBurstTimeMS": 1000,  # 以暴制暴的窗口时长
            "buffList": [100009]
        }

    @staticmethod
    def EXAMPLE_PLAY_DEAD():
        return {
            "type": "PLAY_DEAD",
            "timeMS": FishCommand.BattleRandomRange(3000, 6000),
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ()
        }

    @staticmethod
    def EXAMPLE_STRUGGLE():
        return {
            "type": "STRUGGLE",
            "timeMS": FishCommand.BattleRandomRange(2000, 5000),
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "previewTimeMS": 1000,
            "canCounterTimingMS": [1000, 2000],  # 弹反时长不可高于状态时长
            "buffList": [100008]
        }

    @staticmethod
    def EXAMPLE_HP_REGENERATE_INFO():
        return {
            "intervalMS": 250,
            "hpRegeneratePermilRange": [100, 250]
        }

    @staticmethod
    def EXAMPLE_DIVE():
        return {
            "type": "DIVE",
            "timeMS": 1000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "previewTimeMS": 500,
            "canCounterTimingMS": [500, 1500],
            "hp_regenerate_info": FishCommand.EXAMPLE_HP_REGENERATE_INFO()
        }

    @staticmethod
    def EXAMPLE_CUT_LINE_INFO():
        return {
            "nextCutLineTimeMS": 1500,
            "nextCutLineSeriesCount": 2,
            "cutLineSeriesIntervalMS": 150
        }

    @staticmethod
    def EXAMPLE_CUT_LINE():
        return {
            "type": "CUT_LINE",
            "timeMS": 5000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "previewTimeMS": 500,
            "canCounterTimingMS": [500, 1500],
            "cutLineInfo": FishCommand.EXAMPLE_CUT_LINE_INFO()
        }

    @staticmethod
    def EXAMPLE_JUMP():
        return {
            "type": "JUMP",
            "timeMS": 2500,
            "qteDelayMS": 500,
            "qte": {
                "type": BATTLE_QTE_TYPE.LEFT,
                "maxTimeMS": 1500,
                "needTimeMS": 1,
                "utlAddValue": 3333334
            }
        }

    @staticmethod
    def EXAMPLE_QTE():
        return {
            "type": "QTE",
            "timeMS": 1000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "qteDelayMS": 500,
            "qte": {
                "type": BATTLE_QTE_TYPE.LEFT,
                "maxTimeMS": 1500,
                "needTimeMS": 1,
                "utlAddValue": 3333334
            }
        }

    @staticmethod
    def DEFAULT_EXHAUSTED():
        return {
            "type": "EXHAUSTED",
            "timeMS": 5000,
            "force_seq": FishCommand.FORCE_SEQ_DIZZY(),
            "buffList": [100005]
        }

    @staticmethod
    def DEFAULT_EXHAUSTED_JUMP():
        return {
            "type": "EXHAUSTED",
            "timeMS": 5000,
            "force_seq": FishCommand.FORCE_SEQ_DIZZY(),
            "buffList": [100005]
        }

    @staticmethod
    def DEFAULT_EXHAUSTED_FRENZY():
        return {
            "type": "EXHAUSTED",
            "timeMS": 5000,
            "force_seq": FishCommand.FORCE_SEQ_DIZZY(),
            "buffList": [100005]
        }

    @staticmethod
    def DEFAULT_DIZZY():
        return {
            "type": "DIZZY",
            "timeMS": 1500,
            "force_seq": FishCommand.FORCE_SEQ_DIZZY(),
            "buffList": [100004]
        }

    # dzl用
    # 常规游动
    @staticmethod
    def SEA_SWIM():
        return {
            "type": "SWIM",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            # "buffList": [111, 112, 113]
        }

    # 冲锋
    @staticmethod
    def SEA_RUSH():
        return {
            "type": "RUSH",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "buffList": [200001]
        }

    # 切线
    @staticmethod
    def SEA_CUT_LINE():
        return {
            "type": "CUT_LINE",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "previewTimeMS": 500,
            "canCounterTimingMS": [500, 1500],
            "cutLineInfo": FishCommand.EXAMPLE_CUT_LINE_INFO()
        }

    # 虚弱
    @staticmethod
    def SEA_EXHAUSTED():
        return {
            "type": "EXHAUSTED",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "buffList": [200002]
        }

    @staticmethod
    def SEA_EMPTY():
        return {
            "type": "EMPTY",
            "timeMS": 3000,
            "force_seq": FishCommand.EXAMPLE_FORCE_SEQ(),
            "buffList": [200002]
        }