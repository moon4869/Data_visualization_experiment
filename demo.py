from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Radar
from pyecharts.charts import HeatMap
from pyecharts.charts import Parallel
from pyecharts import options as opts

# 柱状图代码
bar = Bar()
bar.add_xaxis(['2012', '2013', '2014', '2015', '2016', '2017', '2018'])
bar.add_yaxis("USA", [58, 57, 53, 55, 55, 54, 51])
bar.add_yaxis("United Kingdom", [8, 7, 7, 7, 7, 7, 8])
bar.add_yaxis("France", [5, 5, 4, 4, 4, 4, 4])
bar.add_yaxis("Japan", [5, 6, 8, 7, 6, 6, 3])
bar.add_yaxis("Canada", [3, 4, 3, 3, 3, 3, 4])
bar.add_yaxis("China", [0, 0, 2, 2, 2, 2, 2])
bar.set_global_opts(title_opts=opts.TitleOpts(title='CWUR前一百在榜大学'))
bar.render(path="CWUR前一百在榜大学.html")

# 饼图代码
x_data = ["USA", "United Kingdom", "France", "Japan", "China",
          "Others", "Canada", "Germany", "Israel", "Netherlands", "Sweden"]
y_data = [51, 8, 4, 3, 2, 16, 4, 3, 3, 3, 3]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])
(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="国家",
        data_pair=data_pair,
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="2018年cwur不同国家前百在榜大学数",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("2018年cwur不同国家前百在榜大学数.html")
)


# 雷达图代码
v1 = [[53, 53, 133, 64, 121, 44]]
v2 = [[53, 52, 130, 89, 113, 28]]
v3 = [[73, 63, 158, 65, 156, 30]]

(
    Radar(init_opts=opts.InitOpts(width="1600px",
                                  height="1000px", bg_color="#CCCCCC"))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="校友就业", max_=80),
            opts.RadarIndicatorItem(name="刊物", max_=80),
            opts.RadarIndicatorItem(
                name="影响", max_=160),
            opts.RadarIndicatorItem(name="引文", max_=100),
            opts.RadarIndicatorItem(name="广泛影响", max_=160),
            opts.RadarIndicatorItem(name="专利", max_=60),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    .add(
        series_name="2015",
        data=v3,
        linestyle_opts=opts.LineStyleOpts(color="#91C7AE", width=2),
    )
    .add(
        series_name="2016",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000", width=2),
    )
    .add(
        series_name="2017",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#5CACEE", width=2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="清华大学具体得分排名情况"),
        legend_opts=opts.LegendOpts()
    )
    .render("清华大学具体得分情况.html")
)


# 热力图代码
cn = [
    [58, 57, 53, 55, 55, 54, 51],
    [8, 7, 7, 7, 7, 7, 8],
    [5, 5, 4, 4, 4, 4, 4],
    [5, 6, 8, 7, 6, 6, 3],
    [0, 0, 2, 2, 2, 2, 2],
    [3, 4, 3, 3, 3, 3, 4],
    [3, 2, 4, 2, 2, 2, 3],
    [4, 4, 3, 3, 3, 3, 3],
    [2, 1, 1, 2, 2, 2, 3],
    [1, 1, 2, 1, 1, 1, 3]
]
xn = [x for x in range(10)]
yn = [y for y in range(7)]
country = ['USA', 'UK', 'France', 'Japan', 'China',
           'Canada', 'Germany', 'Israel', 'Netherlands', 'Sweden']
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
data = []
for x in xn:
    for y in yn:
        data.append([x, y, cn[x][y]])

(
    HeatMap(init_opts=opts.InitOpts(width="1440px", height="720px"))
    .add_xaxis(xaxis_data=country)
    .add_yaxis(
        series_name="前百在榜数",
        yaxis_data=years,
        value=data,
        label_opts=opts.LabelOpts(
            is_show=True, color="#fff", position="inside", horizontal_align="50%"
        ),
    )
    .set_series_opts()
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="category",
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=0, max_=10, is_calculable=True, orient="horizontal", pos_left="center"
        ),
    )
    .render("不同国家前百在榜大学数.html")
)


# 平行坐标图代码
data = [
    [1, 1, 1, 1, 1, 1, 1],
    [2, 8, 2, 2, 3, 2, 3],
    [3, 2, 12, 3, 2, 3, 2],
    [4, 3, 10, 6, 7, 17, 13],
    [5, 7, 14, 9, 6, 4, 9],
    [6, 13, 6, 10, 12, 13, 14],
    [7, 6, 24, 5, 4, 7, 7],
    [8, 11, 13, 8, 17, 11, 16],
    [9, 4, 15, 4, 26, 23, 39],
    [10, 9, 27, 11, 10, 32, 18]
]

(
    Parallel()
    .add_schema(
        [
            {"dim": 0, "name": "排名"},
            {"dim": 1, "name": "教育质量"},
            {"dim": 2, "name": "校友就业"},
            {"dim": 3, "name": "教师质量"},
            {"dim": 4, "name": "影响"},
            {"dim": 5, "name": "引文"},
            {"dim": 6, "name": "广泛影响"},
        ]
    )
    .add("parallel", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="2017cwur前10大学具体得分排名"))
    .render("2017cwur前10大学具体得分排名.html")
)
