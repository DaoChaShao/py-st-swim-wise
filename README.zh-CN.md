<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**项目简介**
---

**SwimWise（泳智控）**是一款将**现代运动科学理论（ACWR）**与**大语言模型（LLM）**深度融合的数字化游泳智能训练管理平台。
系统通过连接智能穿戴多模态数据，实现微观层面的**“疲劳控险”**与宏观层面的**“赛季目标达成”**，打造千人千面的“AI 游泳科学家”。

**数据描述**
---

本研究使用的是来自 Kaggle 的
多模态可穿戴游泳运动
**数据集 ([Multimodal Wearable Swimming Dataset](https://www.kaggle.com/datasets/programmer3/multimodal-wearable-swimming-dataset))**
。该数据集记录了多名游泳运动员在 28 天周期内的连续监测数据，旨在通过可穿戴设备采集的多模态生理与训练指标，评估运动员的日常训练负荷、身体恢复状态以及潜在的运动损伤风险。

在数据预处理与监控阶段，我们基于原始数据衍生了以下运动科学核心指标：

+ **Daily Load (当日负荷)**: 训练时长 × 训练强度 ($Training\_Duration\_Min \times Training\_Intensity$)。
+ **Acute Training Load (ATL / 急性训练负荷)**: 运动员过去 7 天的 Daily Load 滚动平均值。
+ **Chronic Training Load (CTL / 慢性训练负荷)**: 运动员过去 28 天的 Daily Load 滚动平均值。
+ **ACWR (急慢性期工作负荷比)**: 急性负荷 / 慢性负荷 (ATL / CTL)，用于预测运动员的疲劳程度和受伤风险。

**隐私声明**
---

本应用程序旨在处理您提供的数据以生成定制化的建议和结果。您的隐私至关重要。

**我们不会收集、存储或传输您的个人信息或数据。** 所有处理都在您的设备本地进行（在浏览器或运行时环境中），*
*数据永远不会发送到任何外部服务器或第三方。**

- **本地处理：** 您的数据永远不会离开您的设备。整个分析和生成过程都在本地进行。
- **无数据保留：** 由于没有数据传输，因此不会在任何服务器上存储数据。关闭应用程序通常会清除任何临时本地数据。
- **透明度：** 整个代码库都是开源的。我们鼓励您随时审查[代码](./)以验证您的数据处理方式。

总之，您始终完全控制和拥有自己的数据。

**许可声明**
---

本项目是开源的，可在 [BSD-3-Clause 许可证](LICENCE) 下使用。

简单来说，这是一个非常宽松的许可证，允许您几乎出于任何目的自由使用此代码，包括在专有项目中，只要您包含原始的版权和许可证声明。

欢迎随意分叉、修改并在此作品基础上进行构建！我们只要求您在适当的地方给予认可。

**环境设置**
---

本项目使用 **Python 3.12** 和 [uv](https://docs.astral.sh/uv/) 进行快速的依赖管理和虚拟环境处理。所需的 Python
版本会自动从 [.python-version](.python-version) 文件中检测到。

1. **安装 uv**：  
   如果您还没有安装 `uv`，可以使用以下命令安装：
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # 此安装方法适用于 macOS 和 Linux。
    ```
   或者，您可以运行以下 PowerShell 命令来安装：
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    # 此安装方法适用于 Windows。
    ```

   **💡 推荐**：为了获得最佳体验，请将 `uv` 作为独立工具安装。避免在 `pip` 或 `conda` 环境中安装，以防止潜在的依赖冲突。
2. **初始化 uv**：
   运行以下命令来初始化 `uv`：
    ```bash
    uv init
    ```
   如果在初始化过程中遇到任何问题，请先删除原有的 `pyproject.toml` 文件。
3. **添加依赖**：

- 添加主要（生产）依赖：
    ```bash
    uv add <package_name>
    # 这会自动更新 pyproject.toml 并安装包
    ```
- 添加开发依赖：
    ```bash
    uv add <package_name> --group dev
    # 示例：uv add ruff --group dev
    # 这会自动将包添加到 [project.optional-dependencies.dev] 部分
    ```
- 添加其他类型的可选依赖（例如测试、文档）：
    ```bash
    uv add <package_name> --group test
    uv add <package_name> --group docs
    ```
- 从 `requirements.txt` 文件导入依赖：
    ```bash
    uv add -r requirements.txt
    # 这会从 requirements.txt 读取包并将其添加到 pyproject.toml
    ```
- 从当前依赖生成 `requirements.txt` 文件：
    ```bash
    # 这会将所有依赖（包括可选依赖）导出到 requirements-all.txt
    uv pip compile pyproject.toml --all-extras -o requirements.txt
    ```

4. **移除依赖**

- 移除主要（生产）依赖：
    ```bash
    uv remove <package_name>
    # 这会自动更新 pyproject.toml 并移除包
    ```
- 移除开发依赖：
    ```bash
    uv remove <package_name> --group dev
    # 示例：uv remove ruff --group dev
    # 这会从 [project.optional-dependencies.dev] 部分移除包
    ```
- 移除其他类型的可选依赖：
    ```bash
    uv remove <package_name> --group test
    uv remove <package_name> --group docs
    ```

5. **管理环境**

- 使用添加/移除命令后，同步环境：
    ```bash
    uv sync
    ```

**更新日志**
---

本项目使用 [git-changelog](https://github.com/pawamoy/git-changelog)
基于 [Conventional Commits](https://www.conventionalcommits.org/) 自动生成和维护更新日志。

1. **安装**
   ```bash
   pip install git-changelog
   # 或使用 uv 将其添加为开发依赖
   uv add git-changelog --group dev
   ```
2. **验证安装**
   ```bash
   pip show git-changelog
   # 或专门检查版本
   pip show git-changelog | grep Version
   ```
3. **配置**
   确保您在项目根目录有一个正确配置的 `pyproject.toml` 文件。配置应将 Conventional Commits 指定为更新日志样式。以下是示例配置：
   ```toml
   [tool.git-changelog]
   version = "0.1.0"
   style = "conventional-commits"
   output = "CHANGELOG.md"
   ```
4. **生成更新日志**
   ```bash
   git-changelog --output CHANGELOG.md
   # 或者使用 uv 运行
   uv run git-changelog --output CHANGELOG.md
   ```
   此命令会根据您的 git 历史记录创建或更新 `CHANGELOG.md` 文件。
5. **推送更改**
   ```bash
   git push origin main
   ```
   或者，使用您 IDE 的 Git 界面（例如，在许多编辑器中的 `Git → Push`）。
6. **注意**：

- 更新日志是根据您的提交消息遵循 Conventional Commits 规范自动生成的。
- 每当您想要更新更新日志时（通常在发布之前或进行重大更改之后），运行生成命令。
