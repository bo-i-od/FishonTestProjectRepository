 struct TIMER_MAIN
{

	int id;
	string name;          // ģ������
	int timerID;          // ��ʱ��ID
	string timerName;	  // ��ʱ�������߻���ע��
    int cycleType;	      // ѭ������ 1-�̶� 2-ÿ�� 3-ÿ�� 4-ÿ�� 5-����ʱ

   
    // cycleTypeΪ:1-�̶� yyyy-MM-dd HH:mm:ss 
    
    // cycleTypeΪ:2-ÿ�� 0000-00-00 HH:mm:ss 
    //                    0000-MM-00 HH:mm:ss  ĳ�µ�ÿ��
    //                    yyyy-MM-00 HH:mm:ss  ĳ��ĳ�µ�ÿ��
    //                    yyyy-00-00 HH:mm:ss  ĳ���ÿ��
    
    // cycleTypeΪ:3-ÿ�� 0000-00-00 HH:mm:ss 
    //                    0000-MM-00 HH:mm:ss  ĳ�µ�ÿ��
    //                    yyyy-MM-00 HH:mm:ss  ĳ��ĳ�µ�ÿ��
    //                    yyyy-00-00 HH:mm:ss  ĳ���ÿ��

    // cycleTypeΪ:4-ÿ�� 0000-00-00 HH:mm:ss  
    //                    yyyy-00-00 HH:mm:ss  ĳ���ÿ��
	string openTime;	  // [����ʱ��] ��yyyy ��MM ��dd ʱHH ��mm ��ss    cycleTypeΪ:1-�̶� yyyy-MM-dd HH:mm:ss    cycleTypeΪ:2-ÿ�� 0000-00-00 HH:mm:ss    0000-MM-00 HH:mm:ss  ĳ�µ�ÿ��    yyyy-MM-00 HH:mm:ss  ĳ��ĳ�µ�ÿ��    yyyy-00-00 HH:mm:ss    ĳ���ÿ��    cycleTypeΪ:3-ÿ�� 0000-00-00 HH:mm:ss    0000-MM-00 HH:mm:ss  ĳ�µ�ÿ��    yyyy-MM-00 HH:mm:ss    ĳ��ĳ�µ�ÿ��    yyyy-00-00 HH:mm:ss    ĳ���ÿ�� 
	int openWeek;         // [����ʱ��]�ܲ��� �ܼ�1-7�е�һ��
	string endTime;       // [����ʱ��] openTimeʲô��ʽ,�˴�����ʲô��ʽ,����һ��
	int endWeek;	      // [����ʱ��]�ܲ��� �ܼ�1-7�е�һ��
	int duration;	      // [5-����ʱ]�ĳ���ʱ��,��λ��
};

TIMER_MAIN timer_main[];
#pragma import("TIMER_MAIN.data.txt")



