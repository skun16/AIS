from dash import Dash, dcc, html
import feffery_maplibre as fml
import feffery_antd_components as fac
import feffery_utils_components as fuc

from app.core.config import settings


def create_dash_app() -> Dash:
    dash_app = Dash(
        __name__,
        title=settings.app_name,
        suppress_callback_exceptions=True,
        assets_folder="assets",
    )

    dash_app.layout = fac.AntdLayout(
        [
            fac.AntdHeader(
                fac.AntdSpace(
                    [
                        fac.AntdText("企业级地理数据智能平台", strong=True, style={"fontSize": 18}),
                        fac.AntdTag("现代化", color="blue"),
                        fac.AntdTag("中文", color="green"),
                    ],
                    size=8,
                    align="center",
                ),
                style={"background": "#0b1d39", "padding": "0 24px"},
            ),
            fac.AntdContent(
                [
                    fac.AntdRow(
                        [
                            fac.AntdCol(
                                fac.AntdCard(
                                    [
                                        fac.AntdTitle("欢迎", level=4),
                                        fac.AntdParagraph(
                                            "平台集成企业微信登录、权限管理、地理空间分析、数据看板、"
                                            "大模型问答与多智能体编排等能力。"
                                        ),
                                        fac.AntdSpace(
                                            [
                                                fac.AntdButton("进入数据看板", type="primary"),
                                                fac.AntdButton("打开地理分析"),
                                                fac.AntdButton("启动智能体编排"),
                                            ],
                                            wrap=True,
                                        ),
                                    ]
                                ),
                                span=8,
                            ),
                            fac.AntdCol(
                                fac.AntdCard(
                                    [
                                        fac.AntdTitle("实时运营看板", level=4),
                                        dcc.Graph(
                                            figure={
                                                "data": [
                                                    {
                                                        "type": "bar",
                                                        "x": ["项目", "数据源", "用户", "智能体"],
                                                        "y": [12, 58, 340, 6],
                                                    }
                                                ],
                                                "layout": {"height": 260, "margin": {"l": 30, "r": 10}},
                                            }
                                        ),
                                    ]
                                ),
                                span=8,
                            ),
                            fac.AntdCol(
                                fac.AntdCard(
                                    [
                                        fac.AntdTitle("RAG & 问答", level=4),
                                        fac.AntdParagraph(
                                            "结合企业知识库与外部数据，提供可追溯、可解释的智能问答。"
                                        ),
                                        fac.AntdTimeline(
                                            [
                                                fac.AntdTimelineItem("接入文档与地图数据"),
                                                fac.AntdTimelineItem("向量化索引与权限过滤"),
                                                fac.AntdTimelineItem("多智能体协同推理"),
                                            ]
                                        ),
                                        fac.AntdInput(
                                            placeholder="请输入问题，例如：本周新增项目的空间分布？",
                                        ),
                                        fac.AntdButton("智能检索", type="primary", style={"marginTop": 8}),
                                    ]
                                ),
                                span=8,
                            ),
                        ],
                        gutter=16,
                    ),
                    fac.AntdDivider(),
                    fac.AntdCard(
                        [
                            fac.AntdTitle("地图可视化", level=4),
                            fml.MapContainer(
                                [
                                    fml.RasterLayer(
                                        id="base-layer",
                                        tileUrlTemplate="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                    )
                                ],
                                center=[116.3974, 39.9093],
                                zoom=10,
                                style={"height": "360px", "borderRadius": 12},
                            ),
                            fuc.FefferyMarkdown(
                                "**能力建议**：支持多源数据叠加、时空分析、热力图与轨迹回放。",
                                style={"marginTop": 12},
                            ),
                        ]
                    ),
                ],
                style={"padding": "24px"},
            ),
        ],
        style={"minHeight": "100vh", "background": "#f5f7fb"},
    )

    return dash_app
