# 群体服务覆盖与对外披露：资料契约

`population` 每条是同一期同一人口标识的资格事实，`groups` 是分号分隔的重点群体集合。`internal` 和 `public` 分别是辖区补访与公开统计用途许可；两者不能互代。仅 `reached` 且 `verified=1` 计为真实触达；同人有多条记录时按人去重。`progress` 的 `state=failed` 代表确认尝试失败，`unknown` 为结果不明。`areas` 使用父级包含子级的关系。同一期覆盖总体中的人数可按规则报 `all`、`reached`、`not_reached`；最后一类仅指当前没有核实触达，内部仍区分尝试及缺失状态。
`catalog` 的 `groups` 表示交集，`*` 表示不限定；公开受众只知道目录的逻辑关系、结构零、公开总体上界（`policies`）、已公布值和允许比较的更正关系，不知道内部人员明细或未公开服务事实。公开更正使用 `links`：对 `north` 区全部目录范围，`changed_at_most=1` 指更正前后至多一人改变资格、群体或触达三者之一；其余人属于原单元且状态相同。`released` 列的是已可取得的公开事实；`proposal` 为未确认草案，可通过 `alternate` 指向允许的替代口径。`sensitive=1` 且真实人数小于 `minimum_values` 的单元按该政策保护。比例若公开，采用精确人数/分母派生，与可逆的原人数同样计入披露。

## 输入表

- `areas.csv`：`area`、`parent`
- `population.csv`：`period`、`version`、`person`、`area`、`groups`、`internal`、`public`
- `progress.csv`：`period`、`version`、`person`、`state`、`verified`
- `jurisdictions.csv`：`staff`、`area`、`start`、`end`
- `catalog.csv`：`cell`、`area`、`groups`、`status`、`sensitive`、`structural_zero`
- `policies.csv`：`period`、`audience`、`minimum_values`、`population_upper_bound`
- `links.csv`：`period`、`before`、`after`、`area`、`changed_at_most`
- `released.csv`：`bulletin`、`audience`、`period`、`version`、`cell`、`count`、`at`
- `proposal.csv`：`id`、`audience`、`period`、`version`、`cell`、`alternate`、`presentation`
