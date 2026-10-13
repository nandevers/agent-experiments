# Agent experiments for credit analysis

Notebook prototypes exploring how language models can query synthetic lending data, select analytical metrics, and draft credit-policy analysis.

The project connects SQL-based data access with a stateful analytical workflow. It is a research and learning repository; production deployment, business impact, and regulatory validation have not been established here.

## Why this problem matters

Credit analysis requires connecting a business question to the available data, choosing appropriate metrics, checking whether the evidence is sufficient, and communicating the result. These experiments explore where an LLM can assist that process and which decisions still require explicit review.

## Repository guide

| File | Purpose |
| --- | --- |
| [credit/data_mock.ipynb](credit/data_mock.ipynb) | Creates mock banking data in SQLite, including customer, account, product, transaction, installment, and cost-of-capital tables. |
| [credit/basic_sql_agent.ipynb](credit/basic_sql_agent.ipynb) | Introduces a LangChain SQL agent for natural-language questions over the mock database. |
| [credit/complex_sql_agent.ipynb](credit/complex_sql_agent.ipynb) | Extends SQL exploration to multi-step questions and inspection of intermediate query results. |
| [credit/policy_maker_agent.ipynb](credit/policy_maker_agent.ipynb) | Defines a LangGraph workflow for identifying analytical objectives, selecting metrics, retrieving information, assessing sufficiency, and generating a report. |
| [credit/README.md](credit/README.md) | Describes the intended policy-maker product requirements. Treat these as proposed capabilities and targets rather than implemented guarantees. |

## Workflow under exploration

Business question → extract parameters → define objectives → assess available evidence → propose and select metrics → query and analyze data → assess sufficiency → generate a report or request further analysis.

The policy-maker notebook represents this process as a state graph, with an analytical loop before report generation.

## Technical components

- Python and Jupyter notebooks.
- SQLite for synthetic relational datasets.
- LangChain for SQL-agent experiments.
- LangGraph for the policy-analysis workflow.
- OpenAI chat-model calls in the existing notebooks.
- Pandas, Faker, Pydantic, and Loguru where used by individual notebooks.

## Reproducibility notes

Review the notebook code before running it. This repository does not yet include a pinned dependency environment or a verified end-to-end run procedure.

The SQL examples refer to `mock_bank_data.sqlite`, which the mock-data notebook creates. The policy-maker notebook instead refers to `synthetic_data.db`; that database is not included in the tracked repository. Align the workflow with an appropriate synthetic schema before attempting that experiment.

The notebooks use older LangChain import paths and model identifiers. Compatibility and model availability must be checked in the intended runtime. SQLite is part of Python's standard library.

API-backed notebook execution can incur model usage costs. Configure credentials in your own environment and use synthetic data for these experiments.

## What would make this a stronger benchmark

These are proposed extensions, not completed features:

1. A pinned environment and repeatable synthetic dataset.
2. A versioned question set with independently calculated SQL answers.
3. Measurements of answer correctness, unsupported claims, latency, and model cost.
4. Read-only SQL access, bounded analytical loops, and explicit failure handling.
5. A trace showing the evidence behind every report claim.
6. Documented human review and deployment criteria.

An LLM's statement that an analysis is sufficient is a workflow signal; it does not establish the correctness of the underlying data or conclusion.

## Author and context

[Fernando Barbosa](https://www.linkedin.com/in/fernando-barbosa-ds/) is a Lead Scientist at FICO. His professional work includes customer AI requirements and solution architecture for credit underwriting and credit limit management.

This repository documents personal research prototypes for financial analysis. The professional role and the maturity of this public project are described separately.

Related writing: [Medium](https://fernando-liaison.medium.com/).

This is a personal repository. It does not imply endorsement by an employer.

## License

See [LICENSE](LICENSE) for the repository's CC0 1.0 license.
