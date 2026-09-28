---
name: electrical-properties
description: 低温材料电性能知识库。涵盖材料电性能基础、低温测量方法、典型材料数据、外部效应（磁场/应力/AC）。用于查询材料电参数、低温测试方法、合金电阻行为。
version: 1.0.0
source: "NBS Technical Note 1053 — F.R. Fickett (1982)"
---

# 材料电性能 Skill — Electrical Properties at Low Temperature

> 来源：**F. R. Fickett**, *Electrical Properties of Materials and Their Measurement at Low Temperatures*, NBS Technical Note 1053, March 1982.

## 知识架构

```
electrical-properties/
├── SKILL.md                     # 本文件 — 入口 & 使用指南
└── references/
    ├── 01-basics.md             # Ch1: 低温电阻基础概念
    ├── 02-measurement.md        # Ch2: 实验技术与测量方法
    ├── 03-pure-metals.md        # Ch3: 纯金属电阻率
    ├── 04-alloys.md             # Ch4: 合金电阻率
    ├── 05-external-effects.md   # Ch5: 外部电阻机制（磁场/压力/应力）
    ├── 06-ac-properties.md      # Ch6: 交流电阻率与介电材料
    └── 07-data-tables.md        # Ch7: 具体金属与合金数据表
```

## 使用指南

### 何时触发

- 查询某金属/合金在低温下的电阻率或 RRR
- 询问低温电性能测量方法（DC/AC/涡流）
- 需要了解杂质、缺陷、尺寸效应对电阻的影响
- 磁场中的电阻变化（磁阻效应）
- AC 条件下的趋肤效应、涡流损耗
- 低温结构合金选型

### 使用方式

1. 根据问题类型，`read` 对应 `references/` 文件
2. 数据表格类查询 → `07-data-tables.md`
3. 测量方法类 → `02-measurement.md`
4. 理论机制类 → `03-pure-metals.md` / `04-alloys.md` / `05-external-effects.md`
5. 如需原始文献，参考各章节末尾的 References（源自原书 170+ 篇文献）

### 重要提醒

- **低温度电阻率没有"通用值"**：纯金属的低温电阻率对杂质/缺陷极度敏感。同一牌号的铜，4K 电阻率可相差 10 倍以上。**如低温电阻是关键参数，必须实测具体材料。**
- 原书数据多来自文献图表提取，数值仅供定性参考。精确数据应查阅原始文献。
- 本书不涵盖超导体、半导体或大多数绝缘体。

### 原书基本信息

| 项目 | 值 |
|------|------|
| 作者 | F. R. Fickett |
| 机构 | National Bureau of Standards (NBS), Boulder, Colorado |
| 出版 | NBS Technical Note 1053, March 1982 |
| 页数 | 76 pages |
| 范围 | 金属与合金的低温电阻，重点是技术应用材料 |
