# Agent Skills

集中管理日常开发、项目交付和 GitHub 个人主页设计所用的技能。每个技能保留独立目录、完整引用与许可证，可按任务单独读取或安装。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [github-profile-polish](skills/github-profile-polish/SKILL.md) | GitHub 个人主页 README 的四种排版、明暗预览、公开作品与贡献展示 |
| [workspace-delivery](skills/workspace-delivery/SKILL.md) | CRM / Go 全栈项目的规格、票据、实现、审查与提交 |
| [typescript-pro](skills/typescript-pro/SKILL.md) | TypeScript 类型设计、类型安全和复杂泛型 |
| [sql-pro](skills/sql-pro/SKILL.md) | SQL、数据库结构、查询优化和迁移 |
| [playwright-expert](skills/playwright-expert/SKILL.md) | 浏览器交互与端到端验证 |
| [vercel-react-best-practices](skills/vercel-react-best-practices/SKILL.md) | React / Next.js 的渲染、数据请求与性能 |

## GitHub 主页技能做什么

`github-profile-polish` 面向 **个人账号主页**。账号为 `USERNAME` 时，主页内容来自公开同名仓库 `USERNAME/USERNAME` 的 `README.md`，并不是所有项目的 README。

支持编辑排版、终端、卡片与极简四种风格，以及亮暗双版、本地预览和可选公开贡献展示。先生成预览再决定是否发布；本机预览不会自动修改 GitHub 主页。使用方式见技能内的 [首次使用说明](skills/github-profile-polish/references/first-run.md)。

```sh
python skills/github-profile-polish/scripts/build_profile.py --gallery ./style-preview
```

该命令只离线比较样式；示例文案不能当作个人成果发布。自己的预览建议输出到忽略目录 `.local/`。

## 目录与使用

```text
agent-skills/
├── skills/              # 可公开、可单独安装的完整技能
├── third-party/         # 第三方许可与来源声明
├── docs/                # 目录规则、来源与维护状态
├── local-only/          # 本机专用技能入口，Git 忽略
└── .local/              # 本机清单、迁移记录和预览，Git 忽略
```

按任务选择一个技能，让助手读取对应 `SKILL.md`，或安装到所用工具支持的技能目录。不要一次运行所有技能，也不要仅复制 `SKILL.md` 而丢掉其引用、脚本和许可。

本工作区的旧 `.agents/skills` 作为兼容发现入口，开发项目仍按各自规则使用适用子集。原工具管理的技能和私人技能通过本机目录索引管理，不改全局配置，不自动公开。

根目录 MIT 许可适用于本仓原创说明与入口；第三方技能以各自许可为准，详见 [来源说明](docs/SOURCES.md)。
