 struct TIMER_MAIN
{

	int id;
	string name;          // 模板名称
	int timerID;          // 计时器ID
	string timerName;	  // 计时器名（策划备注）
    int cycleType;	      // 循环类型 1-固定 2-每天 3-每周 4-每月 5-倒计时

   
    // cycleType为:1-固定 yyyy-MM-dd HH:mm:ss 
    
    // cycleType为:2-每天 0000-00-00 HH:mm:ss 
    //                    0000-MM-00 HH:mm:ss  某月的每天
    //                    yyyy-MM-00 HH:mm:ss  某年某月的每天
    //                    yyyy-00-00 HH:mm:ss  某年的每天
    
    // cycleType为:3-每周 0000-00-00 HH:mm:ss 
    //                    0000-MM-00 HH:mm:ss  某月的每周
    //                    yyyy-MM-00 HH:mm:ss  某年某月的每周
    //                    yyyy-00-00 HH:mm:ss  某年的每周

    // cycleType为:4-每月 0000-00-00 HH:mm:ss  
    //                    yyyy-00-00 HH:mm:ss  某年的每月
	string openTime;	  // [开启时间] 年yyyy 月MM 日dd 时HH 分mm 秒ss    cycleType为:1-固定 yyyy-MM-dd HH:mm:ss    cycleType为:2-每天 0000-00-00 HH:mm:ss    0000-MM-00 HH:mm:ss  某月的每天    yyyy-MM-00 HH:mm:ss  某年某月的每天    yyyy-00-00 HH:mm:ss    某年的每天    cycleType为:3-每周 0000-00-00 HH:mm:ss    0000-MM-00 HH:mm:ss  某月的每周    yyyy-MM-00 HH:mm:ss    某年某月的每周    yyyy-00-00 HH:mm:ss    某年的每周 
	int openWeek;         // [开启时间]周参数 周几1-7中的一个
	string endTime;       // [结束时间] openTime什么格式,此处就是什么格式,必须一致
	int endWeek;	      // [结束时间]周参数 周几1-7中的一个
	int duration;	      // [5-倒计时]的持续时间,单位秒
};

TIMER_MAIN timer_main[];
#pragma import("TIMER_MAIN.data.txt")



