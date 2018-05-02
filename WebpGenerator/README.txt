1. 检查是否已安装Java环境

$ java -version

java version "1.8.0_91"
Java(TM) SE Runtime Environment (build 1.8.0_91-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.91-b14, mixed mode)


2. 执行方式: java -jar webpgen.jar [原png档目录] [每一祯的显示时间(ms)] [画质区间]
例: 每一祯100ms, 产生画质3~8之间的动画档  (画质参数最小为1最大为10)

3.cd 到Webp資料夾位置

$ java -jar webpgen.jar /Users/jc.wang/Pictures/CARS_02/PNG 80 5-8


Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C50_A50.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C50_A60.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C50_A70.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C50_A80.webp .......Done
...
...
...
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C80_A50.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C80_A60.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C80_A70.webp .......Done
Generating /Users/jc.wang/Pictures/CARS_02/PNG/output/anim/Anim_C80_A80.webp .......Done


4. 产生的结果会置于 [原png档目录]/output/anim  之下, result.html 可查看所有产出结果
   目前非所有浏览器都支援WebP格式, 建议使用 Google Chrome / Opera / 360极速浏览器(windows下)

[注意]
1. png档案目录及档名建议勿使用中文名
2. 建议将动画的档案大小控制: 小/中/大 500K/1MB/2MB
3. ALPHA及渐层色明显影响动画品质及档案大小



