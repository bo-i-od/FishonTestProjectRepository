from common.basePage import BasePage


def get_flash_card(bp: BasePage, fishery_id=None):
    if fishery_id:
        table_data_object_list = bp.excelTools.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=fishery_id, book_name="COLLECTION_BASE.xlsm")
        if not table_data_object_list:
            return
        collection_chapter_id = table_data_object_list[0]["collectionChapterId"]
        bp.cmd(f"flashcard 1 {collection_chapter_id} 0")
        return
    table_data_object_list = bp.excelTools.get_table_data_object_list(book_name="COLLECTION_BASE.xlsm")
    collection_chapter_id_set = set()
    for table_data_object in table_data_object_list:
        collection_chapter_id = table_data_object["collectionChapterId"]
        if collection_chapter_id in collection_chapter_id_set:
            continue
        bp.cmd(f"flashcard 1 {collection_chapter_id} 0")
        collection_chapter_id_set.add(collection_chapter_id)
        bp.sleep(0.1)




if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    get_flash_card(bp)
    bp.connect_close()

