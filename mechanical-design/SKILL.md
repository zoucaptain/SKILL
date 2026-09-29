---
name: mechanical-design
description: 机械设计综合知识库。基于《机械设计手册》第六版5卷，涵盖传动、轴承、连接件、结构材料、润滑密封等。用于查询设计参数、选型计算、强度校核。触发词：齿轮、轴承、螺栓、键、销、润滑、密封、公差、疲劳、强度、弹簧、联轴器、离合器、制动器、液压、气动、机架、减振。
version: 1.0.0
---

# 机械设计综合知识库

基于《机械设计手册》第六版（共5卷，总计约8500页）提取的综合知识库。

## 数据源

| 卷次 | 主题范围 | 页数 |
|------|---------|------|
| 第1卷 | 一般设计资料、机械制图、极限与配合、工程材料、机构、产品结构设计 | 2017页 |
| 第2卷 | 连接与紧固、轴及其连接、轴承、起重运输机械零部件 | 1693页 |
| 第3卷 | 润滑与密封、弹簧、螺旋传动、带链传动、齿轮传动 | 1640页 |
| 第4卷 | 多点啮合柔性传动、减速器变速器、电机电液推杆、振动控制、机架设计 | 1316页 |
| 第5卷 | 液压传动、液压控制、气压传动 | 1846页 |

知识库引用文件位于 `references/` 目录下，按主题分类存储。

## 知识架构

### 1. 传动系统 (`references/transmission/`)
- **齿轮传动** (`transmission/gear-transmission.md`) — 渐开线圆柱齿轮、圆弧圆柱齿轮、锥齿轮、蜗杆传动、行星齿轮传动、少齿差行星齿轮、销齿传动、活齿传动、点线啮合齿轮、塑料齿轮
- **带传动与链传动** (`transmission/belt-chain-transmission.md`) — V带、平带、同步带、滚子链、齿形链
- **螺旋传动** (`transmission/screw-transmission.md`) — 滑动螺旋、滚珠螺旋、静压螺旋
- **摩擦轮传动** (`transmission/friction-wheel.md`)
- **减速器与变速器** (`transmission/reducers-variators.md`) — 齿轮减速器、蜗杆减速器、行星减速器、无级变速器
- **电机与执行器** (`transmission/motors-actuators.md`) — 常用电机、电器、电动/液压推杆、升降机
- **机构分析与设计** (`transmission/mechanisms.md`) — 机构分析方法、基本机构设计、组合机构

### 2. 轴承与轴系 (`references/bearings-shafts/`)
- **滚动轴承** (`bearings-shafts/rolling-bearings.md`) — 深沟球、角接触、圆锥滚子、推力轴承等选型、寿命计算、游隙配合
- **滑动轴承** (`bearings-shafts/sliding-bearings.md`) — 径向滑动、推力滑动、气体/液体润滑轴承
- **直线运动滚动部件** (`bearings-shafts/linear-bearings.md`) — 直线导轨、直线轴承、滚珠丝杠
- **轴设计** (`bearings-shafts/shaft-design.md`) — 轴强度计算、刚度校核、临界转速、曲轴、软轴
- **联轴器** (`bearings-shafts/couplings.md`) — 刚性、弹性、液力、电磁联轴器
- **离合器** (`bearings-shafts/clutches.md`) — 机械、电磁、液力、气动离合器
- **制动器** (`bearings-shafts/brakes.md`) — 块式、带式、盘式、锥形制动器

### 3. 连接件 (`references/fasteners/`)
- **螺纹连接** (`fasteners/threaded-fasteners.md`) — 螺纹类型、螺栓强度计算、预紧力、防松设计
- **销、键、花键** (`fasteners/rivets-pins-keys-splines.md`) — 圆柱销、圆锥销、平键、半圆键、花键
- **过盈连接** (`fasteners/interference-fit.md`) — 过盈配合计算、胀紧连接、型面连接、粘接

### 4. 结构材料与设计 (`references/materials-structure/`)
- **工程材料** (`materials-structure/engineering-materials.md`) — 黑色金属、有色金属、非金属材料性能与选用
- **公差与配合** (`materials-structure/tolerances-fits.md`) — 极限与配合、几何公差、表面粗糙度
- **疲劳与强度** (`materials-structure/fatigue-strength.md`) — 强度理论、刚度计算、疲劳寿命、耐磨性设计
- **结构设计准则** (`materials-structure/structural-design-criteria.md`) — 强度、刚度、耐磨、防腐、精度、人机工程、绿色设计
- **制造工艺性** (`materials-structure/manufacturing-processes.md`) — 铸造、锻造、冲压、焊接、热处理、表面技术

### 5. 润滑与密封 (`references/lubrication-sealing/`)
- **润滑** (`lubrication-sealing/lubrication.md`) — 润滑方法、润滑装置、润滑剂选型（油脂、润滑油、固体润滑）
- **密封** (`lubrication-sealing/sealing.md`) — 静密封、动密封、机械密封、油封、密封件

### 6. 弹簧 (`references/springs/`)
- **弹簧设计** (`springs/spring-design.md`) — 圆柱螺旋弹簧、碟形弹簧、环形弹簧、片弹簧、板弹簧、扭杆弹簧、橡胶弹簧、空气弹簧、波纹管、膜片、压力弹簧管

### 7. 液压与气动 (`references/hydraulic-pneumatic/`)
- **液压传动** (`hydraulic-pneumatic/hydraulic.md`) — 液压系统设计、液压泵/马达、液压缸、液压阀、液压回路
- **液压控制** (`hydraulic-pneumatic/hydraulic-control.md`) — 伺服阀、比例阀、电液伺服系统
- **气压传动** (`hydraulic-pneumatic/pneumatic.md`) — 气动系统、气缸、气动阀、真空元件、气动回路

### 8. 机架与振动 (`references/frames-vibration/`)
- **机架设计** (`frames-vibration/frame-design.md`) — 梁、柱、桁架、框架设计与计算
- **振动控制** (`frames-vibration/vibration-control.md`) — 线性/非线性振动、减振设计、振动测量、临界转速

## 使用指南

### 触发场景
当用户提出以下类型的问题时，激活本 Skill：
- 查询齿轮参数（模数、压力角、齿数、变位系数、强度计算）
- 轴承选型（载荷计算、寿命校核、游隙选择、配合选择）
- 螺栓连接设计（预紧力、强度校核、防松方案）
- 轴系设计（直径计算、强度校核、临界转速）
- 联轴器/离合器/制动器选型
- 材料选择与热处理
- 公差配合查询与选择
- 润滑剂选型与密封方案
- 弹簧设计与计算
- 液压/气动系统设计
- 机架结构设计与振动分析

### 工作流程
1. **识别主题**：根据用户问题确定知识分类
2. **定位参考文件**：从 `references/` 目录找到对应主题文件
3. **提取知识**：阅读参考文件中的相关内容（公式、表格、设计流程）
4. **综合回答**：结合《手册》数据给出计算步骤、选型建议或设计参数
5. **标注来源**：回答中注明引用的卷次和页码范围

### 回答原则
- 优先使用《机械设计手册》第六版中的公式、图表、标准数据
- 涉及计算时，列出完整计算步骤和公式来源
- 选型类问题给出推荐范围并说明理由
- 如涉及安全系数、许用应力等，注明适用条件
- 当参考文件内容被截断时（单文件上限约80KB），说明可能还有更多详细内容

### 注意事项
- 本知识库基于《机械设计手册》第六版提取，数据仅供设计参考
- 涉及国家标准（GB/T）的数据，以最新有效版本为准
- 实际工程设计应结合具体工况、安全规范和行业标准
- 关键受力部件的设计建议进行有限元分析或试验验证

## 参考文件索引

完整文件列表见 `references/` 目录，共30个分类知识文件，总数据量约5.9MB。
