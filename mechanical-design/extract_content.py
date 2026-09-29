"""Extract content from 机械设计手册 第六版 (5 volumes) and organize into knowledge base files."""
import fitz, os, sys, json, re, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = r"C:\Users\yanyan.zou\.openclaw\workspace\skills\mechanical-design\references"

volumes = [
    {"file": r"C:\Users\yanyan.zou\Desktop\机械设计手册\机械设计手册 第六版 第1卷.PDF", "name": "vol1"},
    {"file": r"C:\Users\yanyan.zou\Desktop\机械设计手册\机械设计手册 第六版 第2卷.PDF", "name": "vol2"},
    {"file": r"C:\Users\yanyan.zou\Desktop\机械设计手册\-机械设计手册 第六版 第3卷.PDF", "name": "vol3"},
    {"file": r"C:\Users\yanyan.zou\Desktop\机械设计手册\-机械设计手册 第六版 第4卷.PDF", "name": "vol4"},
    {"file": r"C:\Users\yanyan.zou\Desktop\机械设计手册\-机械设计手册 第六版 第5卷.PDF", "name": "vol5"},
]

# Define sections to extract: (output_file, volume_index, start_page, end_page, title)
sections = [
    # Volume 1: Materials, tolerances, mechanisms, structural design
    ("materials-structure/engineering-materials.md", 0, 1143, 1652, "常用机械工程材料"),
    ("materials-structure/tolerances-fits.md", 0, 951, 1123, "极限与配合、几何公差、表面结构"),
    ("materials-structure/structural-design-criteria.md", 0, 1919, 2011, "机械产品结构设计准则"),
    ("materials-structure/fatigue-strength.md", 0, 1935, 1972, "强度、刚度、疲劳寿命、耐磨性设计准则"),
    ("materials-structure/manufacturing-processes.md", 0, 228, 728, "铸造、锻造、焊接、热处理、表面技术"),
    ("transmission/mechanisms.md", 0, 1655, 1916, "机构分析与设计"),

    # Volume 2: Fasteners, shafts, bearings, couplings
    ("fasteners/threaded-fasteners.md", 1, 26, 216, "螺纹及螺纹连接"),
    ("fasteners/rivets-pins-keys-splines.md", 1, 216, 302, "铆钉、销、键和花键连接"),
    ("fasteners/interference-fit.md", 1, 302, 381, "过盈连接、胀紧连接、粘接"),
    ("bearings-shafts/shaft-design.md", 1, 384, 436, "轴、曲轴和软轴"),
    ("bearings-shafts/couplings.md", 1, 436, 614, "联轴器"),
    ("bearings-shafts/clutches.md", 1, 614, 743, "离合器"),
    ("bearings-shafts/brakes.md", 1, 743, 834, "制动器"),
    ("bearings-shafts/sliding-bearings.md", 1, 837, 1034, "滑动轴承"),
    ("bearings-shafts/rolling-bearings.md", 1, 1034, 1338, "滚动轴承"),
    ("bearings-shafts/linear-bearings.md", 1, 1338, 1379, "直线运动滚动功能部件"),

    # Volume 3: Lubrication, sealing, springs, transmissions
    ("lubrication-sealing/lubrication.md", 2, 27, 276, "润滑方法、装置、润滑剂"),
    ("lubrication-sealing/sealing.md", 2, 276, 506, "密封与密封件"),
    ("springs/spring-design.md", 2, 509, 726, "弹簧设计（螺旋弹簧、碟形弹簧、橡胶弹簧等）"),
    ("transmission/screw-transmission.md", 2, 729, 786, "螺旋传动"),
    ("transmission/friction-wheel.md", 2, 786, 801, "摩擦轮传动"),
    ("transmission/belt-chain-transmission.md", 2, 804, 942, "带传动、链传动"),
    ("transmission/gear-transmission.md", 2, 954, 1639, "齿轮传动（渐开线齿轮、锥齿轮、蜗杆、行星齿轮等）"),

    # Volume 4: Reducers, motors, vibration, frames
    ("transmission/reducers-variators.md", 3, 118, 549, "减速器、变速器"),
    ("transmission/motors-actuators.md", 3, 552, 875, "常用电机、电器、电动液压推杆与升降机"),
    ("frames-vibration/vibration-control.md", 3, 880, 1111, "机械振动的控制及利用"),
    ("frames-vibration/frame-design.md", 3, 1117, 1315, "机架设计"),

    # Volume 5: Hydraulic and pneumatic
    ("hydraulic-pneumatic/hydraulic.md", 4, 29, 828, "液压传动"),
    ("hydraulic-pneumatic/hydraulic-control.md", 4, 831, 1271, "液压控制"),
    ("hydraulic-pneumatic/pneumatic.md", 4, 1275, 1846, "气压传动"),
]

def extract_text(doc, start_page, end_page, max_chars=80000):
    """Extract text from a page range, with char limit."""
    texts = []
    total = 0
    # PDF page numbers are 0-indexed in PyMuPDF
    for pg in range(start_page - 1, min(end_page, doc.page_count)):
        page = doc[pg]
        t = page.get_text("text")
        if t.strip():
            texts.append(f"\n--- 第{pg+1}页 ---\n")
            texts.append(t)
            total += len(t)
            if total > max_chars:
                texts.append(f"\n... [内容截断，共 {pg+1} 页已提取] ...")
                break
    return "\n".join(texts)

for out_path, vol_idx, start, end, title in sections:
    vol = volumes[vol_idx]
    doc = fitz.open(vol["file"])
    actual_pages = doc.page_count
    actual_end = min(end, actual_pages)
    
    print(f"Extracting: {title} (vol{vol_idx+1}, pp.{start}-{actual_end}) -> {out_path}")
    
    text = extract_text(doc, start, actual_end)
    
    # Create header
    header = f"# {title}\n\n"
    header += f"> 来源：《机械设计手册》第六版 第{vol_idx+1}卷，第{start}-{actual_end}页\n\n"
    header += f"## 目录\n"
    
    # Get TOC entries for this range
    toc = doc.get_toc()
    relevant_toc = [item for item in toc if start <= item[2] <= actual_end]
    for level, ttitle, tpage in relevant_toc:
        indent = "  " * (level - 1)
        header += f"{indent}- {ttitle} (p.{tpage})\n"
    header += "\n---\n"
    
    full_content = header + text
    
    full_path = os.path.join(BASE, out_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8-sig") as f:
        f.write(full_content)
    
    print(f"  -> {len(full_content):,} chars, {len(full_content)/1024:.0f} KB")
    doc.close()

print("\nDone! All sections extracted.")
