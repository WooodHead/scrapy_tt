class CatMatch(object):
    def __init__(self):
        self.en_cat = {
            'IrDA 收发器模块': 'Sensors/Transducers',
            'LVDT 变送器（线性可变差动变压器）': 'Sensors/Transducers',
            '专用传感器': 'Sensors/Transducers',
            '传感器 - 配件': 'Sensors/Transducers',
            '传感器接口 - 接线盒': 'Sensors/Transducers',
            '传感器电缆 - 配件': 'Sensors/Transducers',
            '位置传感器 - 角，线性位置测量': 'Sensors/Transducers',
            '光传感器  - 光电，工业': 'Sensors/Transducers',
            '光学传感器 - 光断续器 - 槽型 - 晶体管输出': 'Sensors/Transducers',
            '光学传感器 - 光断续器 - 槽型 - 逻辑输出': 'Sensors/Transducers',
            '光学传感器 - 光电检测器 - 逻辑输出': 'Sensors/Transducers',
            '光学传感器 - 光电检测器 - 遥控接收器': 'Sensors/Transducers',
            '光学传感器 - 光电检测器 - CdS 单元': 'Sensors/Transducers',
            '光学传感器 - 反射式 - 模拟输出': 'Sensors/Transducers',
            '光学传感器 - 反射式 - 逻辑输出': 'Sensors/Transducers',
            '光学传感器 - 测距': 'Sensors/Transducers',
            '光学传感器 - 环境光，IR，UV 传感器': 'Sensors/Transducers',
            '光学传感器 - 鼠标': 'Sensors/Transducers',
            '光学传感器 - 光电二极管': 'Sensors/Transducers',
            '光学传感器 - 光电晶体管': 'Sensors/Transducers',
            '冲击传感器': 'Sensors/Transducers',
            '力传感器': 'Sensors/Transducers',
            '压力传感器，变送器': 'Sensors/Transducers',
            '图像传感器，相机': 'Sensors/Transducers',
            '多功能': 'Sensors/Transducers',
            '太阳能电池': 'Sensors/Transducers',
            '应变计': 'Sensors/Transducers',
            '弯曲传感器': 'Sensors/Transducers',
            '接近/占位传感器 - 成品': 'Sensors/Transducers',
            '接近传感器': 'Sensors/Transducers',
            '放大器': 'Sensors/Transducers',
            '气体传感器': 'Sensors/Transducers',
            '浮子，液位传感器': 'Sensors/Transducers',
            '温度传感器 - NTC 热敏电阻器': 'Sensors/Transducers',
            '温度传感器 - PTC 热敏电阻器': 'Sensors/Transducers',
            '温度传感器 - RTD（电阻温度检测器）': 'Sensors/Transducers',
            '温度传感器 - 模拟和数字输出': 'Sensors/Transducers',
            '温度传感器 - 温控器 - 固态': 'Sensors/Transducers',
            '温度传感器 - 温控器 - 机械式': 'Sensors/Transducers',
            '温度传感器 - 热电偶，温度探头': 'Sensors/Transducers',
            '湿度，湿敏传感器': 'Sensors/Transducers',
            '灰尘传感器': 'Sensors/Transducers',
            '电容式触摸传感器，接近传感器 IC': 'Sensors/Transducers',
            '电流变送器': 'Sensors/Transducers',
            '磁性传感器 - 位置，接近，速度（模块）': 'Sensors/Transducers',
            '磁性传感器 - 开关（固态）': 'Sensors/Transducers',
            '磁性传感器 - 线性，罗盘（IC）': 'Sensors/Transducers',
            '磁性传感器 - 罗盘，磁场（模块）': 'Sensors/Transducers',
            '磁性器件 - 传感器匹配式': 'Sensors/Transducers',
            '磁性器件 - 多用途': 'Sensors/Transducers',
            '编码器': 'Sensors/Transducers',
            '超声波接收器/发射器': 'Sensors/Transducers',
            '运动传感器 - IMU（惯性测量装置）': 'Sensors/Transducers',
            '运动传感器 - 倾斜开关': 'Sensors/Transducers',
            '运动传感器 - 倾角仪': 'Sensors/Transducers',
            '运动传感器 - 光学': 'Sensors/Transducers',
            '运动传感器 - 加速计': 'Sensors/Transducers',
            '运动传感器 - 振动': 'Sensors/Transducers',
            '运动传感器 - 陀螺仪': 'Sensors/Transducers',
            '颜色传感器': 'Sensors/Transducers',
            'LED - 垫片，支座': 'Optoelectronics',
            'LED - 灯更换': 'Optoelectronics',
            'LED - 电路板指示器，阵列，发光条，条形图': 'Optoelectronics',
            'LED LED 散热产品': 'Optoelectronics',
            'LED 指示 - 分立': 'Optoelectronics',
            'LED 照明 - COB，引擎，模块': 'Optoelectronics',
            'LED 照明 - 彩色': 'Optoelectronics',
            'LED 照明 - 白色': 'Optoelectronics',
            'LED 照明套件': 'Optoelectronics',
            '光学 - 光导管': 'Optoelectronics',
            '光学 - 反射镜': 'Optoelectronics',
            '光学 - 镜头': 'Optoelectronics',
            '光学元件 - 非接触式荧光粉光源': 'Optoelectronics',
            '光纤 - 发射器 - 离散式': 'Optoelectronics',
            '光纤 - 发射器 - 驱动器集成电路': 'Optoelectronics',
            '光纤 - 开关，多路复用器，多路分解器': 'Optoelectronics',
            '光纤 - 接收器': 'Optoelectronics',
            '光纤 - 收发器模块': 'Optoelectronics',
            '光纤 - 衰减器': 'Optoelectronics',
            '反相器': 'Optoelectronics',
            '可寻址，专用': 'Optoelectronics',
            '显示器模块 - LCD，OLED 字符和数字': 'Optoelectronics',
            '显示器模块 - LED 字符与数字': 'Optoelectronics',
            '显示器模块 - LED 点阵和簇': 'Optoelectronics',
            '显示器模块 - 真空荧光（VFD）': 'Optoelectronics',
            '显示器边框，透镜': 'Optoelectronics',
            '显示器，监视器 - 接口控制器': 'Optoelectronics',
            '智能，智慧，发光二极管，显示器，图形': 'Optoelectronics',
            '氙气灯照明': 'Optoelectronics',
            '激光二极管': 'Optoelectronics',
            '灯 - 冷阴极荧光（CCFL） 和 UV': 'Optoelectronics',
            '灯 - 白炽灯，氖灯': 'Optoelectronics',
            '电致发光': 'Optoelectronics',
            '红外，UV，可见光发射器': 'Optoelectronics',
            '触摸屏覆盖层': 'Optoelectronics',
            '配件': 'Optoelectronics',
            '面板指示器，指示灯': 'Optoelectronics',
            ' 二极管 - 可变电容（变容器，可变电抗器）': 'Diodes',
            '二极管 - 射频': 'Diodes',
            '二极管 - 整流器 - 单': 'Diodes',
            '二极管 - 整流器 - 阵列': 'Diodes',
            '二极管 - 桥式整流器': 'Diodes',
            '二极管 - 齐纳 - 单': 'Diodes',
            '二极管 - 齐纳 - 阵列 ': 'Diodes',
            '晶体管 - FET，MOSFET - 单': 'Crystals/Resonators',
            '晶体管 - FET，MOSFET - 射频': 'Crystals/Resonators',
            '晶体管 - FET，MOSFET - 阵列': 'Crystals/Resonators',
            '晶体管 - IGBT - 模块': 'Crystals/Resonators',
            '晶体管 - IGBT - 阵列': 'Crystals/Resonators',
            '晶体管 - JFET': 'Crystals/Resonators',
            '晶体管 - UGBT，MOSFET - 单': 'Crystals/Resonators',
            '晶体管 - 双极 (BJT) - 单': 'Crystals/Resonators',
            '晶体管 - 双极 (BJT) - 单，预偏置': 'Crystals/Resonators',
            '晶体管 - 双极 (BJT) - 射频': 'Crystals/Resonators',
            '晶体管 - 双极 (BJT) - 阵列': 'Crystals/Resonators',
            '晶体管 - 双极 (BJT) - 阵列 - 预偏置': 'Crystals/Resonators',
            '晶体管 - 可编程单结': 'Crystals/Resonators',
            '晶体管 - 特殊用途': 'Crystals/Resonators',
            '晶闸管 - DIAC，SIDAC': 'Diodes',
            '晶闸管 - SCR': 'Diodes',
            '晶闸管 - SCR - 模块': 'Diodes',
            '晶闸管 - TRIAC ': 'Diodes',
            '专用变压器': 'Transformers',
            '开关转换器，SMPS 变压器': 'Transformers',
            '电流互感器': 'Transformers',
            '电源变压器': 'Transformers',
            '脉冲变压器': 'Transformers',
            '隔离式，非隔离式自耦变压器 - 升压，降压': 'Transformers',
            '音频变压器': 'Transformers',
            'USB 闪存驱动器': 'Memory',
            '专用': 'Memory',
            '固态硬盘（SSD）': 'Memory',
            '存储卡': 'Memory',
            '存储器 - 模块 ': 'Memory',
            'RF 其它 IC 和模块': 'RF and Microwave',
            'RF 前端（LNA + PA）': 'RF and Microwave',
            'RF 功率分配器/分线器': 'RF and Microwave',
            'RF 双工器': 'RF and Microwave',
            'RF 发射器': 'RF and Microwave',
            'RF 天线': 'RF and Microwave',
            'RF 定向耦合器': 'RF and Microwave',
            'RF 屏蔽': 'RF and Microwave',
            'RF 开关': 'RF and Microwave',
            'RF 接收器': 'RF and Microwave',
            'RF 接收器，发射器及收发器的成品装置': 'RF and Microwave',
            'RF 收发器 IC': 'RF and Microwave',
            'RF 收发器模块': 'RF and Microwave',
            'RF 放大器': 'RF and Microwave',
            'RF 检测器': 'RF and Microwave',
            'RF 混频器': 'RF and Microwave',
            'RF 电源控制器 IC': 'RF and Microwave',
            'RF 解调器': 'RF and Microwave',
            'RF 评估和开发套件，板': 'RF and Microwave',
            'RF 调制器': 'RF and Microwave',
            'RFI 和 EMI - 屏蔽和吸收材料': 'RF and Microwave',
            'RFI 和 EMI - 触头、簧片和衬垫': 'RF and Microwave',
            'RFID 发射应答器，标签': 'RF and Microwave',
            'RFID 天线': 'RF and Microwave',
            'RFID 评估和开发套件及电路板': 'RF and Microwave',
            'RFID 读取模块': 'RF and Microwave',
            'RFID配件': 'RF and Microwave',
            'RFID，RF 接入，监控 IC': 'RF and Microwave',
            'RF配件': 'RF and Microwave',
            '平衡-不平衡变压器': 'RF and Microwave',
            '衰减器': 'RF and Microwave',
            '控制器 - PLC 模块': 'Microcontrollers and Processors',
            '控制器 - 处理，温度': 'Microcontrollers and Processors',
            '控制器 - 机械安全': 'Microcontrollers and Processors',
            '控制器 - 液体，液面': 'Microcontrollers and Processors',
            '控制器 - 电缆组件': 'Microcontrollers and Processors',
            '控制器 - 可编程逻辑（PLC）': 'Microcontrollers and Processors',
            '控制器 - 配件 ': 'Microcontrollers and Processors',
            '机器视觉 - 控制/处理 ': 'Microcontrollers and Processors',
            '照明控制': 'Microcontrollers and Processors',
            '照明控制 - 配件': 'Microcontrollers and Processors',
            '机器视觉 - 摄像头/传感器': 'Sensors/Transducers',
            '机器视觉 - 照明': 'Sensors/Transducers',
            '机器视觉 - 配件': 'Sensors/Transducers',
            '机器视觉 - 镜头': 'Sensors/Transducers',
            '气动，液压 ': 'Sensors/Transducers',
            '监视器 - 电流/电压 - 继电器输出': 'Sensors/Transducers',
            '监视器 - 电流/电压传感器 ': 'Sensors/Transducers',
            'DIP 开关': 'Switches',
            '可编程显示器开关': 'Switches',
            '可配置开关元件 - 照明光源': 'Switches',
            '可配置开关元件 - 触点块': 'Switches',
            '可配置开关元件 - 透镜': 'Switches',
            '可配置开关元件，主体': 'Switches',
            '导航开关，操纵杆': 'Switches',
            '小键盘开关': 'Switches',
            '快动，限位开关': 'Switches',
            '拨动开关': 'Switches',
            '拨轮开关': 'Switches',
            '按钮开关': 'Switches',
            '按钮开关 - 霍尔效应': 'Switches',
            '摇臂开关': 'Switches',
            '旋转开关': 'Switches',
            '滑动开关': 'Switches',
            '磁簧开关': 'Switches',
            '触摸开关': 'Switches',
            '选择器开关': 'Switches',
            '配件 - 套管，密封件': 'Switches',
            '配件 - 帽盖': 'Switches',
            '键锁开关': 'Switches',
            'UV抹除器': 'Programmable Logic',
            '可编程适配器，插座': 'Programmable Logic',
            '编程器，仿真器和调试器': 'Programmable Logic',
            '评估和演示板和套件': 'Programmable Logic',
            '评估板 -  模数转换器（ADC）': 'Programmable Logic',
            '评估板 - 嵌入式 - MCU，DSP': 'Programmable Logic',
            '评估板 - 嵌入式 - 复杂逻辑器件（FPGA，CPLD）': 'Programmable Logic',
            '评估板 - 扩充板': 'Programmable Logic',
            '评估板 - 数模转换器 （DAC）': 'Programmable Logic',
            '评估板 - 线性稳压器': 'Transformers',
            '评估板 - 运算放大器': 'Amplifier Circuits',
            '评估板 - 音频放大器': 'Amplifier Circuits',
            '评估板 -  DC/DC 与 AC/DC（离线）SMPS': 'Programmable Logic',
            '评估板 -  LED 驱动器': 'Drivers And Interfaces',
            '评估板 - 传感器 ': 'Sensors/Transducers',
            'VCO（压控振荡器）': 'Crystals/Resonators',
            '可编程振荡器': 'Crystals/Resonators',
            '引脚可配置/可选择振荡器': 'Crystals/Resonators',
            '振荡器': 'Crystals/Resonators',
            '插口和绝缘体': 'Crystals/Resonators',
            '晶体': 'Crystals/Resonators',
            '独立编程器': 'Crystals/Resonators',
            '谐振器': 'Crystals/Resonators',
            '万用表': 'Sensors/Transducers',
            '万用表 - 专用': 'Sensors/Transducers',
            '函数发生器': 'Sensors/Transducers',
            '可调变压器': 'Sensors/Transducers',
            '泄漏检测器': 'Sensors/Transducers',
            '测试夹 - IC': 'Sensors/Transducers',
            '测试夹 - 抓取器，钩': 'Sensors/Transducers',
            '测试夹 - 短头鳄鱼夹，鳄鱼夹，重型': 'Sensors/Transducers',
            '测试引线 - BNC 接口': 'Sensors/Transducers',
            '测试引线 - 热电偶，温度探头': 'Sensors/Transducers',
            '测试引线 - 跳线，专用型': 'Sensors/Transducers',
            '测试引线 - 香蕉，量表接口': 'Sensors/Transducers',
            '测试引线，探针 - 示波器': 'Sensors/Transducers',
            '测试探头 - 套件，分类': 'Sensors/Transducers',
            '测试探头尖': 'Sensors/Transducers',
            '测试点': 'Sensors/Transducers',
            '温度计': 'Sensors/Transducers',
            '电源 - 测试，工作台': 'Sensors/Transducers',
            '设备 - 电气检测仪，电流探头': 'Sensors/Transducers',
            '设备 - 示波器': 'Sensors/Transducers',
            '设备 - 组合套件': 'Sensors/Transducers',
            '频谱分析器': 'Sensors/Transducers',
            'DSL 滤波器': 'Filters',
            'EMI/RFI 滤波器（LC，RC 网络）': 'Filters',
            'RF 滤波器': 'Filters',
            'SAW 滤波器': 'Filters',
            '共模扼流圈': 'Filters',
            '单片晶体': 'Filters',
            '电力线滤波器模块': 'Filters',
            '螺旋形滤波器': 'Filters',
            '铁氧体圆盘和平板': 'Filters',
            '铁氧体磁珠和芯片': 'Filters',
            '铁氧体磁芯 - 电缆与接线': 'Filters',
            '陶瓷滤波器': 'Filters',
            '馈通式电容器': 'Capacitors',
            '刻度盘': 'Sensors/Transducers',
            '可调功率电阻': 'Resistors',
            '微调电位计': 'Sensors/Transducers',
            '拨轮式电位计': 'Sensors/Transducers',
            '操纵杆电位计': 'Sensors/Transducers',
            '数值显示器电位计': 'Sensors/Transducers',
            '旋转式电位计，变阻器': 'Resistors',
            '滑动电位计 ': 'Sensors/Transducers',
            '云母和 PTFE 电容器': 'Capacitors',
            '双电层电容器 (EDLC)，超级电容器': 'Capacitors',
            '微调器，可变电容器': 'Capacitors',
            '氧化铌电容器': 'Capacitors',
            '电容器网络，阵列': 'Capacitors',
            '硅电容器': 'Capacitors',
            '薄膜电容器': 'Capacitors',
            '钽 - 聚合物电容器': 'Capacitors',
            '钽电容器': 'Capacitors',
            '铝 - 聚合物电容器': 'Capacitors',
            '铝电解电容器': 'Capacitors',
            '陶瓷电容器': 'Capacitors',
            '可调电感器': 'Inductors',
            '固定值电感器': 'Inductors',
            '延迟线': 'Inductors',
            '无线充电线圈': 'Inductors',
            '阵列，信号变压器': 'Inductors',
            '充电电池（次级侧）': 'Power Circuits',
            '点烟器配件': 'Power Circuits',
            '电池充电器': 'Power Circuits',
            '电池座，夹，触点': 'Power Circuits',
            '电池组': 'Power Circuits',
            'AC AC 壁式适配器': 'Power Circuits',
            'AC DC 可配置电源机架': 'Power Circuits',
            'AC DC 可配置电源模块': 'Power Circuits',
            'AC DC 台式，壁式适配器': 'Power Circuits',
            'AC DC 转换器': 'Power Circuits',
            'AC-DC 可配置电源（工厂组装）': 'Power Circuits',
            'LED 驱动器': 'Drivers And Interfaces',
            '以太网供电（PoE）': 'Batteries',
            '直流转换器 ': 'Batteries',
            '保护软管，实心管，衬套': 'Connector Support',
            '光纤电缆': 'Connector Support',
            '冷缩带，套管': 'Connector Support',
            '套管，索环': 'Connector Support',
            '布线管，配线管道': 'Connector Support',
            '接地编织线，微调': 'Connector Support',
            '热收缩套，帽盖': 'Connector Support',
            '热缩布': 'Connector Support',
            '热缩管': 'Connector Support',
            '热缩裹包': 'Connector Support',
            '焊接套管': 'Connector Support',
            '电缆扎带 - 支座和附件': 'Connector Support',
            '电缆扎带和电缆系带': 'Connector Support',
            '电缆拉柄与支持握柄': 'Connector Support',
            '电缆支撑与紧固件': 'Connector Support',
            '线槽，走线系统 - 配件 - 盖子': 'Connector Support',
            '线槽，走线系统 - 附件': 'Connector Support',
            '缆线固定扣': 'Connector Support',
            '螺线形绕线，伸缩套管': 'Connector Support',
            '配线箱，保护': 'Connector Support',
            'PTC 可复位保险丝': 'Circuit Protection',
            'TVS - 二极管': 'Circuit Protection',
            'TVS - 变阻器，MOV': 'Circuit Protection',
            'TVS - 晶闸管': 'Circuit Protection',
            'TVS - 混合技术': 'Circuit Protection',
            '保险丝': 'Circuit Protection',
            '保险丝座': 'Circuit Protection',
            '接地故障电路断路器（GFCI）': 'Circuit Protection',
            '断路器': 'Circuit Protection',
            '断连开关元件': 'Circuit Protection',
            '气体放电管避雷器（GDT）': 'Circuit Protection',
            '涌入电流限制器（ICL）': 'Circuit Protection',
            '温度保险丝，断路器': 'Circuit Protection',
            '照明保护': 'Circuit Protection',
            '电气，专用熔丝': 'Circuit Protection',
            '电涌抑制 IC ': 'Circuit Protection',
            '专用型电阻器': 'Resistors',
            '底座安装电阻器': 'Resistors',
            '电阻器网络，阵列': 'Resistors',
            '芯片电阻 - 表面安装': 'Resistors',
            '通孔电阻器 ': 'Resistors',
            'I/O 继电器模块 - 输入': 'Relays',
            'I/O 继电器模块 - 输出': 'Relays',
            'I/O 继电器模块机架': 'Relays',
            '信号继电器，高达 2 A': 'Relays',
            '功率继电器，高于 2 A': 'Relays',
            '固态继电器': 'Relays',
            '继电器插座': 'Relays',
            '输入/输出继电器模块 - 模拟 ': 'Relays',
            'D 形连接器 - 并口': 'Connectors',
            'D-Sub 连接器': 'Connectors',
            'D-Sub，D 形连接器 - 后壳，罩': 'Connectors',
            'D-Sub，D 形连接器 - 外壳': 'Connectors',
            'D-Sub，D 形连接器 - 端接器': 'Connectors',
            'D-Sub，D 形连接器 - 触头': 'Connectors',
            'D-Sub，D 形连接器 - 适配器': 'Connectors',
            'D-Sub，D 形连接器 - 配件': 'Connectors',
            'D-Sub，D 形连接器 - 配件 - 顶丝': 'Connectors',
            'FFC，FPC（扁平柔性）连接器': 'Connectors',
            'FFC，FPC（扁平柔性）连接器 - 外壳': 'Connectors',
            'FFC，FPC（扁平柔性）连接器 - 触头': 'Connectors',
            'FFC，FPC（扁平柔性）连接器 - 配件': 'Connectors',
            'Keystone - 插件': 'Connectors',
            'Keystone - 配件': 'Connectors',
            'Keystone - 面板，框架': 'Connectors',
            'LGH 连接器': 'Connectors',
            'USB，DVI，HDMI 连接器': 'Connectors',
            'USB，DVI，HDMI 连接器 - 适配器': 'Connectors',
            'USB，DVI，HDMI 连接器 - 配件': 'Connectors',
            '光伏（太阳能板）连接器': 'Connectors',
            '光伏（太阳能板）连接器 - 触头': 'Connectors',
            '光伏（太阳能板）连接器 - 配件': 'Connectors',
            '光纤连接器': 'Connectors',
            '光纤连接器 - 外壳': 'Connectors',
            '光纤连接器 - 适配器': 'Connectors',
            '光纤连接器 - 配件': 'Connectors',
            '刀片式电源连接器': 'Connectors',
            '刀片式电源连接器 - 触头': 'Connectors',
            '刀片式电源连接器 - 配件': 'Connectors',
            '刀片式电源连接器 -  外壳': 'Connectors',
            '分路器，跳線': 'Connectors',
            '卡边缘连接器 - 外壳': 'Connectors',
            '卡边缘连接器 - 触头': 'Connectors',
            '卡边缘连接器 - 边缘板连接器': 'Connectors',
            '卡边缘连接器 - 适配器': 'Connectors',
            '卡边缘连接器 - 配件': 'Connectors',
            '同轴连接器（RF）': 'Connectors',
            '同轴连接器（RF） - 端接器': 'Connectors',
            '同轴连接器（RF） - 触头': 'Connectors',
            '同轴连接器（RF） - 适配器': 'Connectors',
            '同轴连接器（RF） - 配件': 'Connectors',
            '固态照明连接器': 'Connectors',
            '固态照明连接器 - 触头': 'Connectors',
            '固态照明连接器 - 配件': 'Connectors',
            '圆形连接器': 'Connectors',
            '圆形连接器 - 后壳和电缆夹': 'Connectors',
            '圆形连接器 - 外壳': 'Connectors',
            '圆形连接器 - 触头': 'Connectors',
            '圆形连接器 - 适配器': 'Connectors',
            '圆形连接器 - 配件': 'Connectors',
            '在系列适配器之间': 'Connectors',
            '套管 - 电源连接器': 'Connectors',
            '套管 - 配件': 'Connectors',
            '套管 - 音频连接器': 'Connectors',
            '套管 - 音频适配器': 'Connectors',
            '存储器连接器 - PC 卡 - 适配器': 'Connectors',
            '存储器连接器 - PC 卡插槽': 'Connectors',
            '存储器连接器 - 直列式模块插座': 'Connectors',
            '存储器连接器 - 配件': 'Connectors',
            '接线 - 触点': 'Connectors',
            '接线座 - Din 轨道，通道': 'Connectors',
            '接线座 - 接头，插头和插口': 'Connectors',
            '接线座 - 配件': 'Connectors',
            '接线座 - 配件 - 导线金属环': 'Connectors',
            '接线座 - 配件 - 标记条': 'Connectors',
            '接线座 - 配件 - 跳线': 'Connectors',
            '接线座 - 配电': 'Connectors',
            '接线座 - 隔板块': 'Connectors',
            '接线条和转动板': 'Connectors',
            '接线板 - 专用': 'Connectors',
            '接线板 - 接口模块': 'Connectors',
            '接线板 - 线至板': 'Connectors',
            '接线板 - 适配器': 'Connectors',
            '接线板 - 面板安装': 'Connectors',
            '插接式连接器': 'Connectors',
            '插接式连接器 - 配件': 'Connectors',
            '模块化连接器 - 接线块': 'Connectors',
            '模块化连接器 - 接线块 - 配件': 'Connectors',
            '模块化连接器 - 插头': 'Connectors',
            '模块化连接器 - 插头外壳': 'Connectors',
            '模块化连接器 - 插孔': 'Connectors',
            '模块化连接器 - 磁性插孔': 'Connectors',
            '模块化连接器 - 适配器': 'Connectors',
            '模块化连接器 - 配件': 'Connectors',
            '用于 IC 的插座，晶体管': 'Connectors',
            '用于 IC 的插座，晶体管 - 适配器': 'Connectors',
            '用于 IC 的插座，晶体管 - 配件': 'Connectors',
            '电源接入连接器 - 输入，输出，模块': 'Connectors',
            '电源接入连接器 - 配件': 'Connectors',
            '矩形连接器 - 外壳': 'Connectors',
            '矩形连接器 - 弹簧式': 'Connectors',
            '矩形连接器 - 板垫片，叠接器（板对板）': 'Connectors',
            '矩形连接器 - 板载，直接线对板': 'Connectors',
            '矩形连接器 - 自由悬挂，面板安装': 'Connectors',
            '矩形连接器 - 触头': 'Connectors',
            '矩形连接器 - 适配器': 'Connectors',
            '矩形连接器 - 配件': 'Connectors',
            '矩形连接器 - 针座，专用引脚': 'Connectors',
            '矩形连接器 - 针座，公插针': 'Connectors',
            '矩形连接器 - 针座，插座，母插口': 'Connectors',
            '矩形连接器 - 阵列，边缘型，夹层式（板对板）': 'Connectors',
            '端子 - PC 引脚插座，插座连接器': 'Connectors',
            '端子 - PC 引脚，单接线柱连接器': 'Connectors',
            '端子 - 专用连接器': 'Connectors',
            '端子 - 刀式连接器': 'Connectors',
            '端子 - 外壳，套': 'Connectors',
            '端子 - 套管，子弹式连接器': 'Connectors',
            '端子 - 快速连接，快速断开连接器': 'Connectors',
            '端子 - 焊片连接器': 'Connectors',
            '端子 - 环形连接器': 'Connectors',
            '端子 - 电线引脚连接器': 'Connectors',
            '端子 - 电线接头连接器': 'Connectors',
            '端子 - 矩形连接器': 'Connectors',
            '端子 - 磁线连接器': 'Connectors',
            '端子 - 箔片连接器': 'Connectors',
            '端子 - 线对板连接器': 'Connectors',
            '端子 - 螺纹连接器': 'Connectors',
            '端子 - 转塔连接器': 'Connectors',
            '端子 - 适配器': 'Connectors',
            '端子 - 配件': 'Connectors',
            '端子 - 铲形连接器': 'Connectors',
            '端子接线盒系统': 'Connectors',
            '背板连接器 - ARINC': 'Connectors',
            '背板连接器 - ARINC 插件': 'Connectors',
            '背板连接器 - Hard Metric，标准': 'Connectors',
            '背板连接器 - 专用': 'Connectors',
            '背板连接器 - 外壳': 'Connectors',
            '背板连接器 - 触头': 'Connectors',
            '背板连接器 - 配件': 'Connectors',
            '背板连接器 - DIN 41612': 'Connectors',
            '触头 - 引线框': 'Connectors',
            '触点 - 多用途': 'Connectors',
            '连接器，弹簧加载和压力': 'Connectors',
            '重载连接器 - 外壳，盖罩，基底': 'Connectors',
            '重载连接器 - 插件，模块': 'Connectors',
            '重载连接器 - 框架': 'Connectors',
            '重载连接器 - 组件': 'Connectors',
            '重载连接器 - 触头': 'Connectors',
            '重载连接器 - 配件': 'Connectors',
            '香蕉和尖头连接器 - 接线柱': 'Connectors',
            '香蕉和尖头连接器 - 插孔，插头': 'Connectors',
            '香蕉和尖头连接器 - 适配器': 'Connectors',
            '香蕉和尖头连接器 - 配件': 'Connectors',
            '光隔离器 - 三端双向可控硅，SCR输出': 'Logic',
            '光隔离器 - 晶体管，光电输出': 'Logic',
            '光隔离器 - 逻辑输出': 'Logic',
            '数字隔离器': 'Logic',
            '隔离器 - 栅极驱动器 ': 'Logic',
            '逻辑 - FIFO 存储器': 'Logic',
            '逻辑 - 专用逻辑': 'Logic',
            '逻辑 - 信号开关，多路复用器，解码器': 'Logic',
            '逻辑 - 多频振荡器': 'Logic',
            '逻辑 - 奇偶校验发生器和校验器': 'Logic',
            '逻辑 - 栅极和逆变器': 'Logic',
            '逻辑 - 栅极和逆变器 - 多功能，可配置': 'Logic',
            '逻辑 - 比较器': 'Logic',
            '逻辑 - 移位寄存器': 'Logic',
            '逻辑 - 缓冲器，驱动器，接收器，收发器': 'Logic',
            '逻辑 - 触发器': 'Logic',
            '逻辑 - 通用总线函数': 'Logic',
            '逻辑 - 锁销': 'Logic',
            '逻辑 -计数器，除法器': 'Logic',
            '线性 - 放大器 - 专用': 'Logic',
            '线性 - 放大器 - 仪表，运算放大器，缓冲器放大器': 'Logic',
            '线性 - 放大器 - 视频放大器和频缓冲器': 'Logic',
            '线性 - 模拟乘法器，除法器': 'Logic',
            '线性 - 比较器': 'Logic',
            '线性 - 视频处理': 'Logic',
            '线性 - 音頻放大器 ': 'Logic',
            '时钟/计时 - 专用': 'Signal Circuits',
            '时钟/计时 - 可编程计时器和振荡器': 'Signal Circuits',
            '时钟/计时 - 实时时钟': 'Signal Circuits',
            '时钟/计时 - 延迟线': 'Signal Circuits',
            '时钟/计时 - 时钟发生器，PLL，频率合成器': 'Signal Circuits',
            '时钟/计时 - 时钟缓冲器，驱动器 ': 'Signal Circuits',
            '数据采集 - ADCs/DAC - 专用型': 'Microcontrollers and Processors',
            '数据采集 - 数字电位器': 'Microcontrollers and Processors',
            '数据采集 - 数模转换器': 'Microcontrollers and Processors',
            '数据采集 - 模拟前端（AFE）': 'Microcontrollers and Processors',
            '数据采集 - 模数转换器': 'Microcontrollers and Processors',
            '数据采集 - 触摸屏控制器 ': 'Microcontrollers and Processors',
            '嵌入式 - CPLD（复杂可编程逻辑器件）': 'Microcontrollers and Processors',
            '嵌入式 - DSP（数字式信号处理器）': 'Microcontrollers and Processors',
            '嵌入式 - FPGA（现场可编程门阵列）': 'Microcontrollers and Processors',
            '嵌入式 - PLD（可编程逻辑器件）': 'Microcontrollers and Processors',
            '嵌入式 -  微控制器 - 应用特定': 'Microcontrollers and Processors',
            '嵌入式 - 带有微控制器的 FPGA（现场可编程门阵列）': 'Microcontrollers and Processors',
            '嵌入式 - 微处理器': 'Microcontrollers and Processors',
            '嵌入式 - 微控制器': 'Microcontrollers and Processors',
            '嵌入式 - 微控制器，微处理器，FPGA 模块': 'Microcontrollers and Processors',
            '嵌入式 - 片上系统 (SoC) ': 'Microcontrollers and Processors',
            '接口 - I/O 扩展器': 'Drivers And Interfaces',
            '接口 - UART（通用异步接收器/发送器）': 'Drivers And Interfaces',
            '接口 - 专用': 'Drivers And Interfaces',
            '接口 - 串行器，解串行器': 'Drivers And Interfaces',
            '接口 - 传感器和探测器接口': 'Drivers And Interfaces',
            '接口 - 信号终端器': 'Drivers And Interfaces',
            '接口 - 信号缓冲器，中继器，分配器': 'Drivers And Interfaces',
            '接口 - 控制器': 'Drivers And Interfaces',
            '接口 - 模块': 'Drivers And Interfaces',
            '接口 - 模拟开关 - 专用': 'Drivers And Interfaces',
            '接口 - 模拟开关，多路复用器，多路分解器': 'Drivers And Interfaces',
            '接口 - 滤波器 - 有源': 'Drivers And Interfaces',
            '接口 - 电信': 'Drivers And Interfaces',
            '接口 - 直接数字合成（DDS）': 'Drivers And Interfaces',
            '接口 - 编码器，解码器，转换器': 'Drivers And Interfaces',
            '接口 - 编解码器': 'Drivers And Interfaces',
            '接口 - 语音录制和重放': 'Drivers And Interfaces',
            '接口 - 调制解调器 - IC 和模块': 'Drivers And Interfaces',
            '接口 - 驱动器，接收器，收发器 ': 'Drivers And Interfaces',
            'PMIC - AC-DC 转换器，离线开关': 'Power Circuits',
            'PMIC - LED 驱动器': 'Power Circuits',
            'PMIC - OR 控制器，理想二极管': 'Power Circuits',
            'PMIC - PFC（功率因数修正）': 'Power Circuits',
            'PMIC - RMS 至 DC 转换器': 'Power Circuits',
            'PMIC - V/F 和 F/V 转换器': 'Power Circuits',
            'PMIC - 以太网供电（PoE） 控制器': 'Power Circuits',
            'PMIC - 全，半桥驱动器': 'Power Circuits',
            'PMIC - 显示器驱动器': 'Power Circuits',
            'PMIC - 栅极驱动器': 'Power Circuits',
            'PMIC - 激光驱动器': 'Power Circuits',
            'PMIC - 热插拔控制器': 'Power Circuits',
            'PMIC - 热管理': 'Power Circuits',
            'PMIC - 照明，镇流器控制器': 'Power Circuits',
            'PMIC - 电压基准': 'Power Circuits',
            'PMIC - 电机驱动器，控制器': 'Power Circuits',
            'PMIC - 电池充电器': 'Power Circuits',
            'PMIC - 电池管理': 'Power Circuits',
            'PMIC - 电源控制器，监视器': 'Power Circuits',
            'PMIC - 电源管理 - 专用': 'Power Circuits',
            'PMIC - 监控器': 'Power Circuits',
            'PMIC - 稳压器 - DC DC 切换控制器': 'Power Circuits',
            'PMIC - 稳压器 - DC DC 开关稳压器': 'Power Circuits',
            'PMIC - 稳压器 - 专用型': 'Power Circuits',
            'PMIC - 稳压器 - 线性': 'Power Circuits',
            'PMIC - 稳压器 - 线性 + 切换式': 'Power Circuits',
            'PMIC - 稳压器 - 线性稳压器控制器': 'Power Circuits',
            'PMIC - 稳流/电流管理': 'Power Circuits',
            'PMIC - 能量测量': 'Power Circuits',
            'PMIC - 配电开关，负载驱动器 ': 'Power Circuits',
            'AC 风扇': 'Thermal Support Devices',
            'DC 风扇': 'Thermal Support Devices',
            '热 - 垫，片': 'Thermal Support Devices',
            '热 - 液体冷却': 'Thermal Support Devices',
            '热 - 热电，Peltier 模块': 'Thermal Support Devices',
            '热 - 热电，Peltier 组件': 'Thermal Support Devices',
            '热敏 - 散热器': 'Thermal Support Devices',
            '热敏 - 配件': 'Thermal Support Devices',
            '热润滑脂，环氧树脂': 'Thermal Support Devices',
            '风扇 - 护手板，滤波器和套管': 'Thermal Support Devices',
            '风扇 - 配件': 'Thermal Support Devices',
        }

    def catmatch(self, category):
        for k, v in self.en_cat.items():
            if category == k:
                print(v)
                return v


if __name__ == '__main__':
    cat = CatMatch()
    cat.catmatch('芯片电阻 - 表面安装')
    # print(cat)
